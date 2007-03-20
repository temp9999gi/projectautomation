#!/usr/bin/env python
###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2002 by:                                                 #
#    * California Institute of Technology                                 #
#                                                                         #
#    All Rights Reserved.                                                 #
#                                                                         #
# Permission is hereby granted, free of charge, to any person             #
# obtaining a copy of this software and associated documentation files    #
# (the "Software"), to deal in the Software without restriction,          #
# including without limitation the rights to use, copy, modify, merge,    #
# publish, distribute, sublicense, and/or sell copies of the Software,    #
# and to permit persons to whom the Software is furnished to do so,       #
# subject to the following conditions:                                    #
#                                                                         #
# The above copyright notice and this permission notice shall be          #
# included in all copies or substantial portions of the Software.         #
#                                                                         #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,         #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF      #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                   #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS     #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN      #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN       #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE        #
# SOFTWARE.                                                               #
###########################################################################
#
#       Authors: Brandon King
# Last Modified: $Date: 2006/12/18 15:54:02 $
#
rev = '$Revision: 1.1 $'
rev = rev.replace('$Revision: ', '')
rev = rev.replace(' $', '')
VERSION = 'v0.%s' % (rev)

from Tkinter import *
import tkFileDialog
import tkMessageBox
import pymerase
#import Pmw

PymVERSION = pymerase.VERSION

import os
import pickle

class tkPymerase:

  def __init__(self, master):
    print "Loading... Please Wait."

    #Master Tk object
    self.master = master
    
    #####################
    # About Dialog Box
    #Pmw.aboutversion(VERSION)
    #Pmw.aboutcopyright('Copyright (c) 2002 by:\n'\
    #                   'California Institute of Technology\n'\
    #                   'All rights reserved')
    #Pmw.aboutcontact(
    #  'Pymerase %s\n' %(PymVERSION) +
    #  '  Author: Diane Trout\n' +
    #  '  E-mail: diane@caltech.edu\n' +
    #  '\n' +
    #  'tkPymerase %s\n' % (VERSION) +
    #  '  Author: Brandon King\n' +
    #  '  E-mail: kingb@caltech.edu'
    #  )
    #self.aboutDialog = Pmw.AboutDialog(master, applicationname = 'tkPymerase')
    #self.aboutDialog.withdraw()
    
    #####################
    # Menu Bar
    self.menuBar = Menu(master)

    #File Menu
    self.fileMenu = Menu(self.menuBar, tearoff=0)
    self.fileMenu.add_command(label="Load Settings...",
                              command=self.loadSettings)
    self.fileMenu.add_command(label="Save Settings...",
                              command=self.saveSettings)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label="Quit", command=master.quit)
    self.menuBar.add_cascade(label="File", menu=self.fileMenu)

    #Help Menu
    self.helpMenu = Menu(self.menuBar, tearoff=0)
    self.helpMenu.add_command(label="Help...", command=self.help)
    self.helpMenu.add_separator()
    #self.helpMenu.add_command(label="About...", command=self.aboutDialog.show)
    self.helpMenu.add_command(label="About...", command=self.about)
    self.menuBar.add_cascade(label='Help', menu=self.helpMenu)

    #Display Menu
    master.config(menu=self.menuBar)
    
    #####################
    # Frames
    titleFrame = Frame(master)
    titleFrame.grid(row=0)
    
    frame = Frame(master)
    frame.grid(row=1)

    bottomFrame = Frame(master)
    bottomFrame.grid(row=2)

    #####################
    # TITLE
    self.title = Label(titleFrame,
                       text="Pymerase %s" % (PymVERSION),
                       fg="blue",
                       font=("Times", 30))
    self.title.grid(row=0)

    self.launchButton = Button(bottomFrame,
                               text="Launch Pymerase",
                               fg="white",
                               bg="blue",
                               command=self.launch)
    self.launchButton.grid(row=2)
    
    #####################
    #Source Path

    self.sourcePathLabel = Label(frame, text="Input Source:", fg='blue')
    self.sourcePathLabel.grid(row=0)
    self.sourcePathEntry = Entry(frame)
    self.sourcePathEntry.grid(row=1, column=0)
    
    self.outputPathLabel = Label(frame, text="Output Path:", justify=LEFT, fg='blue')
    self.outputPathLabel.grid(row=0, column=3)

        
    #####################
    #Input Mod
    self.inputModLabel = Label(frame,
                               text="Input Module:",
                               justify=LEFT,
                               fg='blue')
    self.inputModLabel.grid(row=0, column=1)

    self.inputModule = StringVar()

    self.radioXml = Radiobutton(frame,
                                text="parseGenexSchemaXML",
                                variable=self.inputModule,
                                value="parseGenexSchemaXML").grid(row=1,
                                                                  column=1)
        
    self.radioXmi = Radiobutton(frame,
                                text="parseXMI",
                                variable=self.inputModule,
                                value="parseXMI").grid(row=2,
                                                       column=1)
    
    #####################
    #Output Mod Check Box

    #LABEL
    self.outputModLabel = Label(frame, text="Output Module:", justify=LEFT, fg='blue')
    self.outputModLabel.grid(row=0, column=2)

    #CreateCppAPI
    self.intCreateCppAPI = IntVar()
    self.CreateCppAPI = Checkbutton(frame,
                                   text="CreateCppAPI",
                                   variable=self.intCreateCppAPI,
                                   command=self.outputModCheck1)
    self.CreateCppAPI.grid(row=1, column=2, sticky=W)
    self.outputCppAPIEntry = Entry(frame)
    self.outputCppAPIEntry.grid(row=1, column=3)

    #CreateDBAPI
    self.intCreateDBAPI = IntVar()
    self.CreateDBAPI = Checkbutton(frame,
                                   text="CreateDBAPI",
                                   variable=self.intCreateDBAPI,
                                   command=self.outputModCheck1)
    self.CreateDBAPI.grid(row=2, column=2, sticky=W)
    self.outputDBAPIEntry = Entry(frame)
    self.outputDBAPIEntry.grid(row=2, column=3)

    #CreateDbTableBrowser
    self.intCreateDbTableBrowser = IntVar()
    self.CreateDbTableBrowser = Checkbutton(frame,
                                   text="CreateDbTableBrowser",
                                   variable=self.intCreateDbTableBrowser,
                                   command=self.outputModCheck1)
    self.CreateDbTableBrowser.grid(row=3, column=2, sticky=W)
    self.outputDbTableBrowserEntry = Entry(frame)
    self.outputDbTableBrowserEntry.grid(row=3, column=3)

    #CreateDBEditor
    #self.intCreateDBEditor = IntVar()
    #self.CreateDBEditor = Checkbutton(frame,
    #                                  text="CreateDBEditor",
    #                                  variable=self.intCreateDBEditor,
    #                                  command=self.outputModCheck1)
    #self.CreateDBEditor.grid(row=2, column=2, sticky=W)
    #self.outputDBEditorEntry = Entry(frame)
    #self.outputDBEditorEntry.grid(row=2, column=3)

    #CreateHtmlForms
    #self.intCreateHtmlForms = IntVar()
    #self.CreateHtmlForms = Checkbutton(frame,
    #                                   text="CreateHtmlForms",
    #                                   variable=self.intCreateHtmlForms,
    #                                   command=self.outputModCheck1)
    #self.CreateHtmlForms.grid(row=3, column=2, sticky=W)
    #self.outputHtmlFormsEntry = Entry(frame)
    #self.outputHtmlFormsEntry.grid(row=3, column=3)

    #CreatePythonAPI
    self.intCreatePythonAPI = IntVar()
    self.CreatePythonAPI = Checkbutton(frame,
                                 text="CreatePythonAPI",
                                 variable=self.intCreatePythonAPI,
                                 command=self.outputModCheck1)
    self.CreatePythonAPI.grid(row=4, column=2, sticky=W)
    self.outputPythonAPIEntry = Entry(frame)
    self.outputPythonAPIEntry.grid(row=4, column=3)

    #CreateSQL
    self.intCreateSQL = IntVar()
    self.CreateSQL = Checkbutton(frame,
                                 text="CreateSQL",
                                 variable=self.intCreateSQL,
                                 command=self.outputModCheck1)
    self.CreateSQL.grid(row=5, column=2, sticky=W)
    self.outputSQLEntry = Entry(frame)
    self.outputSQLEntry.grid(row=5, column=3)

    #CreateGraphvizUML
    self.intCreateGraphvizUML = IntVar()
    self.CreateGraphvizUML = Checkbutton(frame,
                                 text="CreateGraphvizUML",
                                 variable=self.intCreateGraphvizUML,
                                 command=self.outputModCheck1)
    self.CreateGraphvizUML.grid(row=6, column=2, sticky=W)
    self.outputGraphvizUMLEntry = Entry(frame)
    self.outputGraphvizUMLEntry.grid(row=6, column=3)

    #CreatePyTkWidgets
    self.intCreatePyTkWidgets = IntVar()
    self.CreatePyTkWidgets = Checkbutton(frame,
                                 text="CreatePyTkWidgets",
                                 variable=self.intCreatePyTkWidgets,
                                 command=self.outputModCheck1)
    self.CreatePyTkWidgets.grid(row=7, column=2, sticky=W)
    self.outputPyTkWidgetsEntry = Entry(frame)
    self.outputPyTkWidgetsEntry.grid(row=7, column=3)

    #CreatePyTkDBWidgets
    self.intCreatePyTkDBWidgets = IntVar()
    self.CreatePyTkDBWidgets = Checkbutton(frame,
                                 text="CreatePyTkDBWidgets",
                                 variable=self.intCreatePyTkDBWidgets,
                                 command=self.outputModCheck1)
    self.CreatePyTkDBWidgets.grid(row=8, column=2, sticky=W)
    self.outputPyTkDBWidgetsEntry = Entry(frame)
    self.outputPyTkDBWidgetsEntry.grid(row=8, column=3)

    #CreateReport
    self.intCreateReport = IntVar()
    self.CreateReport = Checkbutton(frame,
                                 text="CreateReport",
                                 variable=self.intCreateReport,
                                 command=self.outputModCheck1)
    self.CreateReport.grid(row=9, column=2, sticky=W)
    self.outputReportEntry = Entry(frame)
    self.outputReportEntry.grid(row=9, column=3)

    #CreateTabDelimitedParser
    self.intCreateTabDelimitedParser = IntVar()
    self.CreateTabDelimitedParser = Checkbutton(frame,
                                 text="CreateTabDelimitedParser",
                                 variable=self.intCreateTabDelimitedParser,
                                 command=self.outputModCheck1)
    self.CreateTabDelimitedParser.grid(row=10, column=2, sticky=W)
    self.outputTabDelimitedParserEntry = Entry(frame)
    self.outputTabDelimitedParserEntry.grid(row=10, column=3)

    #CreateTableXML
    self.intCreateTableXML = IntVar()
    self.CreateTableXML = Checkbutton(frame,
                                 text="CreateTableXML",
                                 variable=self.intCreateTableXML,
                                 command=self.outputModCheck1)
    self.CreateTableXML.grid(row=11, column=2, sticky=W)
    self.outputTableXMLEntry = Entry(frame)
    self.outputTableXMLEntry.grid(row=11, column=3)

    #iPymerase
    self.intiPymerase = IntVar()
    self.iPymerase = Checkbutton(frame,
                                 text="iPymerase",
                                 variable=self.intiPymerase,
                                 justify=LEFT,
                                 command=self.outputModCheck2)
    self.iPymerase.grid(row=12, column=2, sticky=W)
    self.outputiPymeraseEntry = Entry(frame)
    self.outputiPymeraseEntry.grid(row=12, column=3)

    #Run load settings in initialize mode
    self.loadSettings(init=1)

  def __del__(self):
    print "Exiting now."

  def outputModCheck1(self):
    
    if self.intCreateDBAPI.get() == 1 or \
           self.intCreateDbTableBrowser.get() == 1 or \
           self.intCreateCppAPI.get() == 1 or \
           self.intCreateSQL.get() == 1 or \
           self.intCreateGraphvizUML.get() == 1 or \
           self.intCreateReport.get() == 1 or \
           self.intCreateTabDelimitedParser.get() == 1 or \
           self.intCreateTableXML.get() == 1 or \
           self.intCreatePyTkWidgets.get() == 1 or \
           self.intCreatePyTkDBWidgets.get() == 1 or \
           self.intCreatePythonAPI.get() == 1:
      self.intiPymerase.set(0)

  def outputModCheck2(self):
    
    if self.intiPymerase.get() == 1:
      #reset other buttons
      self.intCreateDBAPI.set(0)
      self.intCreateDbTableBrowser.set(0)
      self.intCreateCppAPI.set(0)
      #self.intCreateDBEditor.set(0)
      #self.intCreateHtmlForms.set(0)
      self.intCreateSQL.set(0)
      self.intCreateGraphvizUML.set(0)
      self.intCreatePyTkWidgets.set(0)
      self.intCreatePyTkDBWidgets.set(0)
      self.intCreateReport.set(0)
      self.intCreateTabDelimitedParser.set(0)
      self.intCreateTableXML.set(0)
      self.intCreatePythonAPI.set(0)

  def notImplemented(self):
    print 'Not Implemented feature'

  def help(self):
    msg = "For help using pymerase goto http://pymerase.sf.net/"
    tkMessageBox.showinfo("Pymerase: Help", msg)

  def about(self):
    msg = "Pymerase %s\n" \
          "Pymerase GUI %s\n\n" \
          "Copyright (c) 2002 by:\n" \
          "California Institute of Technology\n\n" \
          "License: MIT\n\n" \
          "Lead Developer:\n" \
          "Diane Trout\n\n" \
          "Co-Developer:\n"\
          "Brandon King\n\n" \
          "Mailing List:\n" \
          "pymerase-devel@lists.sf.net" % (PymVERSION, VERSION)
    tkMessageBox.showinfo("Pymerase: About", msg)

  def launch(self):
    print 'Preparing for launch of Pymerase...\n'
    ABORT = 0
    if self.sourcePathEntry.get() == '':
      print 'Invalid Source Path'
      ABORT = 1

    if self.inputModule.get() == '':
      print 'Invalid Input Module'
      ABORT = 1

    if self.intiPymerase.get() == 0 and \
       self.intCreateDBAPI.get() == 0 and \
       self.intCreateDbTableBrowser.get() == 0 and \
       self.intCreateCppAPI.get() == 0 and \
       self.intCreatePythonAPI.get() == 0 and \
       self.intCreateReport.get() == 0 and \
       self.intCreateTabDelimitedParser.get() == 0 and \
       self.intCreateTableXML.get() == 0 and \
       self.intCreateGraphvizUML.get() == 0 and \
       self.intCreatePyTkWidgets.get() == 0 and \
       self.intCreatePyTkDBWidgets.get() == 0 and \
       self.intCreateSQL.get() == 0:
      print 'Must select one or more Output Modules'
      ABORT = 1

    if self.intiPymerase.get() == 1 and \
           len(self.outputiPymeraseEntry.get()) == 0:
      print 'Must enter an output path for iPymerase.'
      ABORT = 1

    if self.intCreateDBAPI.get() == 1 and \
           len(self.outputDBAPIEntry.get()) == 0:
      print 'Must enter an output path for CreateDBAPI.'
      ABORT = 1

    if self.intCreateDbTableBrowser.get() == 1 and \
           len(self.outputDbTableBrowserEntry.get()) == 0:
      print 'Must enter an output path for CreateDbTableBrowser.'
      ABORT = 1

    if self.intCreateCppAPI.get() == 1 and \
           len(self.outputCppAPIEntry.get()) == 0:
      print 'Must enter an output path for CreateCppAPI.'
      ABORT = 1

    #if self.intCreateDBEditor.get() == 1 and \
    #       len(self.outputDBEditorEntry.get()) == 0:
    #  print 'Must enter an output path for CreateDBEditor.'
    #  ABORT = 1
    #
    #if self.intCreateHtmlForms.get() == 1 and \
    #       len(self.outputHtmlFormsEntry.get()) == 0:
    #  print 'Must enter an output path for CreateHtmlForms.'
    #  ABORT = 1

    if self.intCreatePythonAPI.get() == 1 and \
           len(self.outputPythonAPIEntry.get()) == 0:
      print 'Must enter an output path for CreatePythonAPI.'
      ABORT = 1

    if self.intCreateSQL.get() == 1 and \
           len(self.outputSQLEntry.get()) == 0:
      print 'Must enter an output path for CreateSQL.'
      ABORT = 1

    if self.intCreateGraphvizUML.get() == 1 and \
           len(self.outputGraphvizUMLEntry.get()) == 0:
      print 'Must enter an output path for CreateGraphvizUML.'
      ABORT = 1

    if self.intCreatePyTkWidgets.get() == 1 and \
           len(self.outputPyTkWidgetsEntry.get()) == 0:
      print 'Must enter an output path for CreatePyTkWidgets.'
      ABORT = 1

    if self.intCreatePyTkDBWidgets.get() == 1 and \
           len(self.outputPyTkDBWidgetsEntry.get()) == 0:
      print 'Must enter an output path for CreatePyTkDBWidgets.'
      ABORT = 1

    if self.intCreateReport.get() == 1 and \
       len(self.outputReportEntry.get()) == 0:
      print 'Must enter an output path for CreateReport.'
      ABORT = 1

    if self.intCreateTabDelimitedParser.get() == 1 and \
       len(self.outputTabDelimitedParserEntry.get()) == 0:
      print 'Must enter an output path for CreateTabDelimitedParser.'
      ABORT = 1

    if self.intCreateTableXML.get() == 1 and \
       len(self.outputTableXMLEntry.get()) == 0:
      print 'Must enter an output path for CreateTableXML.'
      ABORT = 1

    if ABORT == 1:
      print '\nAborting Launch.'
    else:
      print 'All systems go... Launching Pymerase now!\n'
      self.runPymerase()

  def runPymerase(self):
    schema = os.path.abspath(self.sourcePathEntry.get())
    translatorName = self.inputModule.get()
    outputPairList = []

    if self.intiPymerase.get() == 1 and \
           len(self.outputiPymeraseEntry.get()) > 0:
      outputPairList.append( ('iPymerase',
                              self.outputiPymeraseEntry.get()) )

    if self.intCreateDBAPI.get() == 1 and \
           len(self.outputDBAPIEntry.get()) > 0:
      outputPairList.append( ('CreateDBAPI',
                              self.outputDBAPIEntry.get()) )

    if self.intCreateDbTableBrowser.get() == 1 and \
           len(self.outputDbTableBrowserEntry.get()) > 0:
      outputPairList.append( ('CreateDbTableBrowser',
                              self.outputDbTableBrowserEntry.get()) )

    if self.intCreateCppAPI.get() == 1 and \
           len(self.outputCppAPIEntry.get()) > 0:
      outputPairList.append( ('CreateCppAPI',
                              self.outputCppAPIEntry.get()) )

    #if self.intCreateDBEditor.get() == 1 and \
    #       len(self.outputDBEditorEntry.get()) > 0:
    #  outputPairList.append( ('CreateDBEditor',
    #                          self.outputDBEditorEntry.get()) )
    #  
    #if self.intCreateHtmlForms.get() == 1 and \
    #       len(self.outputHtmlFormsEntry.get()) > 0:
    #  outputPairList.append( ('CreateHtmlForms',
    #                          self.outputHtmlFormsEntry.get()) )

    if self.intCreatePythonAPI.get() == 1 and \
           len(self.outputPythonAPIEntry.get()) > 0:
      outputPairList.append( ('CreatePythonAPI',
                              self.outputPythonAPIEntry.get()) )      
      
    if self.intCreateSQL.get() == 1 and \
           len(self.outputSQLEntry.get()) > 0:
      outputPairList.append( ('CreateSQL',
                              self.outputSQLEntry.get()) )

    if self.intCreateGraphvizUML.get() == 1 and \
       len(self.outputGraphvizUMLEntry.get()) > 0:
      outputPairList.append( ('CreateGraphvizUML',
                              self.outputGraphvizUMLEntry.get()) )

    if self.intCreatePyTkWidgets.get() == 1 and \
           len(self.outputPyTkWidgetsEntry.get()) > 0:
      outputPairList.append( ('CreatePyTkWidgets',
                              self.outputPyTkWidgetsEntry.get()) )

    if self.intCreatePyTkDBWidgets.get() == 1 and \
           len(self.outputPyTkDBWidgetsEntry.get()) > 0:
      outputPairList.append( ('CreatePyTkDBWidgets',
                              self.outputPyTkDBWidgetsEntry.get()) )

    if self.intCreateReport.get() == 1 and \
       len(self.outputReportEntry.get()) > 0:
      outputPairList.append( ('CreateReport',
                              self.outputReportEntry.get()) )

    if self.intCreateTabDelimitedParser.get() == 1 and \
       len(self.outputTabDelimitedParserEntry.get()) > 0:
      outputPairList.append( ('CreateTabDelimitedParser',
                              self.outputTabDelimitedParserEntry.get()) )

    if self.intCreateTableXML.get() == 1 and \
       len(self.outputTableXMLEntry.get()) > 0:
      outputPairList.append( ('CreateTableXML',
                              self.outputTableXMLEntry.get()) )

    if len(outputPairList) == 0:
      raise ValueError, 'Output Module/Destinations missing.'

    translator = pymerase.Pymerase(translatorName)
    parsed_input = translator.read(schema, None, {})

    for outputMod, destination in outputPairList:
      print 'LAUNCHING %s NOW' % (outputMod)
      translator.write(parsed_input, destination, outputMod)

    print "STATUS: Done"
    #Save default file to home directory
    self.saveSettings(homeDir=1)


  def saveSettings(self, homeDir=0):
    """
    Saves tkPymerase settings.
    if homeDir = 0; opens SaveAs Dialog Box
    if homeDir = 1; save to /home/{USER}/.tkPymerase
    """
    settings = {}

    #Source
    settings['sourchPath'] = self.sourcePathEntry.get()

    #Input Module
    settings['inputModule'] = self.inputModule.get()

    #Output Modules
    settings['CreateDBAPI'] = self.intCreateDBAPI.get()
    settings['CreateDbTableBrowser'] = self.intCreateDbTableBrowser.get()
    settings['CreateCppAPI'] = self.intCreateCppAPI.get()
    #settings['CreateDBEditor'] = self.intCreateDBEditor.get()
    #settings['CreateHtmlForms'] = self.intCreateHtmlForms.get()
    settings['CreatePythonAPI'] = self.intCreatePythonAPI.get()
    settings['CreateSQL'] = self.intCreateSQL.get()
    settings['CreateGraphvizUML'] = self.intCreateGraphvizUML.get()
    settings['CreatePyTkWidgets'] = self.intCreatePyTkWidgets.get()
    settings['CreatePyTkDBWidgets'] = self.intCreatePyTkDBWidgets.get()
    settings['CreateReport'] = self.intCreateReport.get()
    settings['CreateTabDelimitedParser'] = self.intCreateTabDelimitedParser.get()
    settings['CreateTableXML'] = self.intCreateTableXML.get()
    settings['iPymerase'] = self.intiPymerase.get()
    
    #Output Destinations
    settings['outputDBAPI'] = self.outputDBAPIEntry.get()
    settings['outputDbTableBrowser'] = self.outputDbTableBrowserEntry.get()
    settings['outputCppAPI'] = self.outputCppAPIEntry.get()
    #settings['outputDBEditor'] = self.outputDBEditorEntry.get()
    #settings['outputHtmlForms'] = self.outputHtmlFormsEntry.get()
    settings['outputPythonAPI'] = self.outputPythonAPIEntry.get()
    settings['outputSQL'] = self.outputSQLEntry.get()
    settings['outputGraphvizUML'] = self.outputGraphvizUMLEntry.get()
    settings['outputPyTkWidgets'] = self.outputPyTkWidgetsEntry.get()
    settings['outputPyTkDBWidgets'] = self.outputPyTkDBWidgetsEntry.get()
    settings['outputReport'] = self.outputReportEntry.get()
    settings['outputTabDelimitedParser'] = self.outputTabDelimitedParserEntry.get()
    settings['outputTableXML'] = self.outputTableXMLEntry.get()
    settings['outputiPymerase'] = self.outputiPymeraseEntry.get()

    if homeDir == 1:
      filePath = '/home/' + os.environ.get('USER') + '/.tkPymerase'
      f = open(filePath, 'w')
    else:
      f = tkFileDialog.asksaveasfile(parent=self.master,
                                     filetypes=[('tkPymerase Settings',
                                                 '*.pymer')],
                                     defaultextension='.pymer',
                                     title='Save tkPymerase Settings')
      if f is None:
        print "Aborting Save Settings"
        return
        
    try:
      pickle.dump(settings, f)
      print 'Save Settings Complete.'
    except:
      print 'ERROR: Save Settings Failed.'
      if f == types.FileType:
        print '  %s is causing problems' % (f.name)
      return
    

  def loadSettings(self, init=0):
    """
    Loads pickle file of tkPymerase settings.
    if init = 1, loads from /home/{user}/.tkPymerase if exists
    if init = 0, loads from tkFileDialog box.
    """
    # init == 1; load from /home/{USER}/.tkPymerase
    if init == 1:

      #Contstruct home user path
      if sys.platform == 'win32':
        filePath = 'C:\\Program Files\\Pymerase\\.tkPymerase'
      else:
        filePath = '/home/' + os.environ.get('USER') + '/.tkPymerase'
      
      #check to see if file exists; yes = open file, no = abort
      if os.path.exists(filePath):
        f = open(filePath, 'r')
      else:
        print 'No .tkPymerase file, no default settings loaded.'
        return
    # init == 0; open dialog box to get file from user
    else:
      
      #Open FileOpen DialogBox
      f = tkFileDialog.askopenfile(filetypes=[('tkPymerase Settings',
                                               '.pymer')],
                                   parent=self.master,
                                   title='Open tkPymerase Settings')
      
      #if dialog box returned none, user cancled, so abort
      if f is None:
        print 'Aborting File Open'
        return

    #Attempt to load pickle file
    try:
      settings = pickle.load(f)

    #Load pickle fail... display info and abort
    except:
      if type(f) == types.FileType:
        print 'Unable to load file %s' % (f.name)
        return
      else:
        raise ValueError, 'ERROR: Not object of type File'

    #Try loading tkPymerase settings
    try:
      #Source
      self.sourcePathEntry.delete(0, END)
      self.sourcePathEntry.insert(0, settings['sourchPath'])
      
      #Input Module
      self.inputModule.set(settings['inputModule'])
      
      #Output Modules
      self.intCreateDBAPI.set(settings['CreateDBAPI'])
      self.intCreateDbTableBrowser.set(settings['CreateDbTableBrowser'])
      self.intCreateCppAPI.set(settings['CreateCppAPI'])
      #self.intCreateDBEditor.set(settings['CreateDBEditor'])
      #self.intCreateHtmlForms.set(settings['CreateHtmlForms'])
      self.intCreatePythonAPI.set(settings['CreatePythonAPI'])
      self.intCreateSQL.set(settings['CreateSQL'])
      self.intCreateGraphvizUML.set(settings['CreateGraphvizUML'])
      self.intCreatePyTkWidgets.set(settings['CreatePyTkWidgets'])
      self.intCreatePyTkDBWidgets.set(settings['CreatePyTkDBWidgets'])
      self.intCreateReport.set(settings['CreateReport'])
      self.intCreateTabDelimitedParser.set(settings['CreateTabDelimitedParser'])
      self.intCreateTableXML.set(settings['CreateTableXML'])
      self.intiPymerase.set(settings['iPymerase'])
      
      #Output Destinations
      self.outputDBAPIEntry.delete(0, END)
      self.outputDBAPIEntry.insert(0, settings['outputDBAPI'])
      self.outputDbTableBrowserEntry.delete(0, END)
      self.outputDbTableBrowserEntry.insert(0, settings['outputDbTableBrowser'])
      self.outputCppAPIEntry.delete(0, END)
      self.outputCppAPIEntry.insert(0, settings['outputCppAPI'])
      #self.outputDBEditorEntry.delete(0, END)
      #self.outputDBEditorEntry.insert(0, settings['outputDBEditor'])
      #self.outputHtmlFormsEntry.delete(0, END)
      #self.outputHtmlFormsEntry.insert(0, settings['outputHtmlForms'])
      self.outputPythonAPIEntry.delete(0, END)
      self.outputPythonAPIEntry.insert(0, settings['outputPythonAPI'])
      self.outputSQLEntry.delete(0, END)
      self.outputSQLEntry.insert(0, settings['outputSQL'])
      self.outputGraphvizUMLEntry.delete(0, END)
      self.outputGraphvizUMLEntry.insert(0, settings['outputGraphvizUML'])
      self.outputPyTkWidgetsEntry.delete(0, END)
      self.outputPyTkWidgetsEntry.insert(0, settings['outputPyTkWidgets'])
      self.outputPyTkDBWidgetsEntry.delete(0, END)
      self.outputPyTkDBWidgetsEntry.insert(0, settings['outputPyTkDBWidgets'])
      self.outputReportEntry.delete(0, END)
      self.outputReportEntry.insert(0, settings['outputReport'])
      self.outputTabDelimitedParserEntry.delete(0, END)
      self.outputTabDelimitedParserEntry.insert(0, settings['outputTabDelimitedParser'])
      self.outputTableXMLEntry.delete(0, END)
      self.outputTableXMLEntry.insert(0, settings['outputTableXML'])
      self.outputiPymeraseEntry.delete(0, END)
      self.outputiPymeraseEntry.insert(0, settings['outputiPymerase'])
      
      print 'Load Settings Complete'
    #Fail; Abort 
    except:
      print 'ERROR: Load Settings Failed'
      return

def loadGUI():
  root = Tk()
  root.title('Pymerase GUI %s' % VERSION)
  pymApp = tkPymerase(root)
  root.mainloop()

if __name__ == '__main__':
  loadGUI()
