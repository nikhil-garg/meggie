# coding: utf-8

"""
"""

import re
import copy
import logging


import numpy as np
import matplotlib.pyplot as plt

import meggie.code_meggie.general.mne_wrapper as mne

from meggie.code_meggie.analysis.utils import color_cycle

from meggie.ui.utils.decorators import threaded
from meggie.code_meggie.general import fileManager
from meggie.code_meggie.structures.epochs import Epochs
from meggie.code_meggie.structures.events import Events
from meggie.code_meggie.utils.units import get_scaling
from meggie.code_meggie.utils.units import get_unit
from meggie.code_meggie.utils.validators import validate_name


def create_epochs(experiment, params, subject):
    """ Epochs are created in a way that one collection consists of such 
    things that belong together. We wanted multiple collections because 
    MNE Epochs don't allow multiple id's for one event name, so doing 
    subselections for averaging and visualizing purposes from one collection
    is not feasible.
    """
    params_copy = copy.deepcopy(params)
    reject_data = params_copy['reject']

    # convert data from human readable units to standard units
    for key in ['grad', 'mag', 'eog', 'eeg']:
        if key in reject_data:
            reject_data[key] /= get_scaling(key)
    
    raw = subject.get_working_file()
         
    events = []
    event_params = params_copy['events']
    fixed_length_event_params = params_copy['fixed_length_events']
    category = {}

    # event_id should not matter after epochs are created.
    # counter is used so that no collisions would happen.
    event_id_counter = 0

    if len(event_params) > 0:
        for event_params_dic in event_params:
            event_id = event_params_dic['event_id']
            
            category_id = 'id_' + str(event_id)
            if event_params_dic['mask']:
                category_id += '_mask_' + str(event_params_dic['mask'])
            
            category[category_id] = event_id_counter + 1
            new_events = np.array(create_eventlist(
                experiment, event_params_dic, subject))

            if len(new_events) == 0:
                raise ValueError('No events found with selected id.')
            
            new_events[:, 2] = event_id_counter + 1
            events.extend([event for event in new_events])
            event_id_counter += 1
            

    if len(fixed_length_event_params) > 0:
        for idx, event_params_dic in enumerate(fixed_length_event_params):
            category['fixed_' + str(idx + 1)] = event_id_counter + 1
            event_params_dic['event_id'] = event_id_counter + 1
            events.extend(mne.make_fixed_length_events(raw, 
                event_params_dic['event_id'],
                event_params_dic['tmin'],
                event_params_dic['tmax'], 
                event_params_dic['interval']
            ))
            event_id_counter += 1

    if len(events) == 0:
        raise ValueError('Could not create epochs for subject: No events found with given params.')

    if not isinstance(raw, mne.RAW_TYPE):
        raise TypeError('Working file is of wrong type.')

    if params_copy['mag'] and params_copy['grad']:
        params_copy['meg'] = True
    elif params_copy['mag']:
        params_copy['meg'] = 'mag'
    elif params_copy['grad']:
        params_copy['meg'] = 'grad'
    else:
        params_copy['meg'] = False
   
    # find all proper picks, dont exclude bads
    picks = mne.pick_types(raw.info, meg=params_copy['meg'],
                           eeg=params_copy['eeg'], eog=params_copy['eog'],
                           exclude=[])
    
    if len(picks) == 0:
        raise ValueError('Picks cannot be empty. Select picks by ' +
                         'checking the checkboxes.')

    epochs = mne.Epochs(raw, np.array(events), 
        category, params_copy['tmin'], params_copy['tmax'],
        baseline=(params_copy['bstart'], params_copy['bend']),
        picks=picks, reject=params_copy['reject'])
        
    if len(epochs.get_data()) == 0:
        raise ValueError('Could not find any data. Perhaps the ' + 
                         'rejection thresholds are too strict...')

    try:
        validate_name(params.get('collection_name', ''))
    except Exception as exc:
        exc_messagebox(self, exc)
        return

    epochs_object = Epochs(params['collection_name'], subject, params, epochs)
    fileManager.save_epoch(epochs_object, overwrite=True)
    subject.add_epochs(epochs_object)
    
    events = epochs.event_id
    events_str = ''
    for event_name, event_id in events.items():
        events_str += event_name + ' [' + str(len(epochs[event_name])) + ' events found]\n'
    
    return subject.subject_name + ', ' + params['collection_name'] + ':\n' + events_str

def create_eventlist(experiment, params, subject):
    """
    Pick desired events from the raw data.
    """
    stim_channel = subject.find_stim_channel()
    raw = subject.get_working_file()
    e = Events(experiment, raw, stim_channel, params['mask'], params['event_id'])

    return e.events


def draw_evoked_potentials(experiment, evokeds, title=None):
    """
    Draws a topography representation of the evoked potentials.

    """
    layout = fileManager.read_layout(experiment.layout)
    colors = color_cycle(len(evokeds))

    new_evokeds = []
    for evoked_idx, evoked in enumerate(evokeds):
        
        new_evokeds.append(evoked.copy().drop_channels(evoked.info['bads']))

    fig = mne.plot_evoked_topo(new_evokeds, layout,
        color=colors, title=title)

    conditions = [e.comment for e in new_evokeds]
    positions = np.arange(0.025, 0.025 + 0.04 * len(new_evokeds), 0.04)
            
    for cond, col, pos in zip(conditions, colors, positions):
        plt.figtext(0.775, pos, cond, color=col, fontsize=12)
        
    window_title = '_'.join(conditions)
    fig.canvas.set_window_title(window_title)
    fig.show()
    
    def onclick(event):
        channel = plt.getp(plt.gca(), 'title')
        plt.gcf().canvas.set_window_title('_'.join([window_title, channel]))
        plt.show(block=False)

    fig.canvas.mpl_connect('button_press_event', onclick)

def average_channels(experiment, instance, channels, title, 
                     update_ui=(lambda: None)):
    """
    """
    
    message = "Calculating channel averages for " + title
    logging.getLogger('ui_logger').info(message)

    datalist, epochs_name = _average_channels(experiment,
        instance, channels, do_meanwhile=update_ui)

    fig = plt.figure()
    subject_name = experiment.active_subject.subject_name
    fig.canvas.set_window_title('_'.join([
        epochs_name, 
        'channel_avg', 
        title]))

    fig.suptitle('Channel average for ' + title, y=1.0025)

    # Draw a separate plot for each event type
    for index, (times, event_name, ch_type, data) in enumerate(datalist):
        ca = fig.add_subplot(len(datalist), 1, index + 1) 
        ca.set_title(event_name)

        if event_name.endswith('grad'):
            ch_type = 'grad'
        elif event_name.endswith('mag'):
            ch_type = 'mag'

        label = get_unit(ch_type)
        data *= get_scaling(ch_type)

        ca.plot(times, data)

        ca.set_xlabel('Time (s)')
        ca.set_ylabel(label)

    plt.tight_layout()
    fig.show()

@threaded
def _average_channels(experiment, instance, channels):
    """Performed in a worker thread."""

    meggie_epochs = experiment.active_subject.epochs.get(instance)
    epochs = meggie_epochs.raw
    epochs_name = meggie_epochs.collection_name

    if epochs is None:
        raise Exception('No epochs found.')

    category = epochs.event_id

    evokeds = [epochs[name].average() for name in category.keys()]

    if not list(mne.pick_types(evokeds[0].info, meg=True)):
        raise Exception('Supported only for MEG data')


    datalist = []

    for evoked in evokeds:

        evoked = evoked.copy()

        # remove bad channels, and their pairs
        removed = []
        for ch_idx, ch_name in enumerate(evoked.info['ch_names']):
            if ch_name in evoked.info['bads']:
                if ch_name.endswith('1'):
                    removed.append(ch_name)
                else:
                    ch_group = ch_name[-4:-1]
                    for ch_idx_2, ch_name_2 in enumerate(evoked.info['ch_names']):
                        if ch_name_2[-4:-1] == ch_group and not ch_name_2.endswith('1'):  # noqa
                            if ch_name_2 not in removed:
                                removed.append(ch_name_2)

        grad_idxs = mne.pick_types(evoked.info, meg='grad', 
                                   selection=channels,
                                   exclude=removed)
        mag_idxs = mne.pick_types(evoked.info, meg='mag',
                                  selection=channels,
                                  exclude=removed)

        if len(grad_idxs) > 0:
            grad_data = mne._merge_grad_data(evoked.data[grad_idxs])
            grad_data = np.mean(grad_data, axis=0)

            # Links the event name and the corresponding data
            datalist.append((
                evoked.times, 
                evoked.comment + ' (grad)',
                'grad',
                grad_data
            ))
        if len(mag_idxs) > 0:
            mag_data = evoked.data[mag_idxs]
            mag_data = np.mean(mag_data, axis=0)
            datalist.append((
                evoked.times,
                evoked.comment + ' (mag)', 
                'mag',
                mag_data
            ))

    return datalist, epochs_name

def group_average(experiment, evoked_name, update_ui=(lambda: None)):
    """
    """
    count = 0
    group_info = {}
    for subject in experiment.subjects.values():
        if subject.evokeds.get(evoked_name):
            count += 1
            evoked = subject.evokeds.get(evoked_name)
            group_info[subject.subject_name] = evoked.info

    if count == 0:
        raise ValueError('No evoked responses found from any subject.')
    
    if count > 0 and count < len(experiment.subjects):
        
        message = ("Evoked responses not found from every subject. " + 
                   "(" + str(count) + " responses found.)")
        logging.getLogger('ui_logger').warning(message)
    
    evokeds = _group_average(experiment,
       evoked_name, do_meanwhile=update_ui
    )

    return evokeds, group_info

@threaded
def _group_average(experiment, evoked_name):
    """Performed in a worker thread."""

    subjects = experiment.subjects.values()
    responses = [subject.evokeds.get(evoked_name) for subject in subjects]
    responses = list(filter(bool, responses))

    # assumme all have same same amount of evokeds
    evoked_groups = {}
    
    for response in responses:
        for key, value in response.mne_evokeds.items():
            if evoked_groups.get(key):
                evoked_groups[key].append(value)
            else:
                evoked_groups[key] = [value]

    grand_averages = {}

    for key, evokeds in evoked_groups.items():
        grand_averaged = mne.grand_average(evokeds)
        grand_averaged.comment = key
        grand_averages[key] = grand_averaged

    return grand_averages
