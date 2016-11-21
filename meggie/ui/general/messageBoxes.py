# coding: utf-8

#Copyright (c) <2013>, <Kari Aliranta, Jaakko Lepp�kangas, Janne Pesonen and Atte Rautio>
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met: 
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer. 
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution. 
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The views and conclusions contained in the software and documentation are those
#of the authors and should not be interpreted as representing official policies, 
#either expressed or implied, of the FreeBSD Project.

"""
@author: Kari Aliranta, Jaakko Leppakangas
Contains the shortMessageBox class used for simple messageboxes,and the 
longMessageBox for longer messages that need a scrolling content area.
"""

from PyQt4 import QtCore, QtGui
from meggie.ui.general.longMessageBoxUi import Ui_LongMessageBoxDialog
from meggie.ui.general.shortMessageBoxUi import Ui_shortMessageBox
from meggie.ui.general.shortMessageBoxQuestionYesNoUi import Ui_shortMessageBoxQuestionYesNo


class shortMessageBox(QtGui.QDialog):
    """
    Class for creating simple messageboxes displaying error messages.
    """
    
    def __init__(self, message, parent=None, title='Error'):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_shortMessageBox()
        self.ui.setupUi(self)
    
        self.setWindowTitle(title)

        try:
            message = unicode(message, 'utf-8')
        except TypeError:
            message = unicode(message)

        self.ui.labelMessage.setText(message.encode('utf-8'))


class shortMessageBoxQuestionYesNo(QtGui.QDialog):
    """
    A class for simple non-modal question messageBox in the
    style of QMessageBox.question. 
    """
    def __init__(self, message, parent=None, title='title'):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_shortMessageBoxQuestionYesNo()
        self.ui.setupUi(self)
        self.setWindowTitle(title)
        self.ui.labelMessage.setText(message)
        self.returnValue = 'no'
        
    def get_return_value(self):
        return self.returnValue
        
    def accept(self):
        self.returnValue = 'yes'
        self.close()
        
    def reject(self):
        self.close()


class longMessageBox(QtGui.QDialog):
    """
    Class for larger, scrollable messageboxes, needed for longer errors and
    output.
    """
    
    def __init__(self, title, message, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_LongMessageBoxDialog()
        self.ui.setupUi(self)
    
        self.setWindowTitle(title)
        self.ui.textEdit.setText(message)
            
            
    def updateOutputField(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll()))
        self.output.ensureCursorVisible()
    
    
    def accept(self):
        self.close()


