  # -*- coding: utf-8 -*-
 
 
import os,sys
import pickle

import mne
 
from PyQt4 import QtCore,QtGui
 
# Import the pyuic4-compiled main UI module 
import messageBox
from mainWindow_Ui import Ui_MainWindow
from CreateProjectDialog_main import CreateProjectDialog
from UIehd1_main import MainWindow

from experiment import Experiment

#import measurementInfo
 
  # Create a class main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        
        """
        Application main window.  
        """
        
        QtGui.QMainWindow.__init__(self)

        """
        Standard reference to the ui settings file generated by pyuic.
        """
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.widget.hide()
            
            
            
    # Automatically connects to clicked-signal of the button    
    def on_ButtonNewProject_clicked(self):
        """
        Creates a new CreateProjectDialog and shows it
        """       
        self.dialog = CreateProjectDialog(self)
        self.dialog.show()
        
    def on_ButtonOpenProject_clicked(self, checked=None):
        """
        Opens an existing project. Requires the user to choose a directory with
        an included .pro-file.
        """
        
        # Standard workaround for file dialog opening twice
        if checked is None: return 
        
        path = str(QtGui.QFileDialog.getExistingDirectory(
               self, "Select project directory"))
        
        fname = path + '/' + path.split('/')[-1] + '.pro'
        
        # TODO needs exception checking for corrupt/wrong type of file
        if os.path.exists(path) and os.path.isfile(fname):
            output = open(fname, 'rb')
            experiment = pickle.load(output)
            #workaround for setting up the raw object
            experiment.raw_data = mne.fiff.Raw(experiment.raw_data.info.get('filename'))
            self.UIehd = MainWindow(experiment)
            self.UIehd.show()
            self.close()
        
        else:
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText('Project files not found.')
            self.messageBox.show()
            

def main(): 
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()