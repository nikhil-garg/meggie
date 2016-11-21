"""
Created on 13.12.2015

@author: talli
"""

import copy
from sys import exc_info
from inspect import isclass
from inspect import getcallargs

def wrap_mne_call(experiment, mne_func, *args, **kwargs):
    logger = experiment.action_logger
    mne_instance_name = 'unknown_function'

    try:
        # works with classes also (mne.Epochs for example)
        mne_instance_name = mne_func.__name__
    except:
        print 'Logging error: the type of the called mne_func is unknown'

    try:
        logger.logger.info('---------------------------------------')
        result = mne_func(*args, **kwargs)
    except:
        logger.logger.info('ERROR: ' + mne_instance_name)
        exc = exc_info()
        
        try:
            message = str(exc[1].args[0])
        except:
            message = str(exc[1])
        raise exc[0], message, exc[2]

    success_msg = 'SUCCESS: ' + mne_instance_name

    try:
        if isclass(mne_func):
            # deepcopy needed for cleaning the dict
            callargs = copy.deepcopy(result.__dict__)
            callargs = logger.clean_callargs(mne_instance_name, callargs)
        else:
            # TODO: clean callargs
            # callargs_copy = copy.deepcopy(getcallargs(mne_func, *args, **kwargs))
            # callargs = logger.clean_callargs(mne_instance_name, callargs_copy)
            callargs = getcallargs(mne_func, *args, **kwargs)
    except:
        logger.logger.info(''.join([
            success_msg,
            '\nLogging parameters failed: ',
            mne_instance_name
        ]))
        return result

    params_str = ', '.join(['{0} = {1}'.format(str(key), str(value)) 
                           for key, value in callargs.items()])

    working_file = experiment.active_subject.working_file_name

    logger.logger.info('{0}\nFile: {1}\n{2}({3})'.format(
        success_msg, working_file, mne_instance_name, params_str))

    return result
