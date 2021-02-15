# Import the module
from docx import Document
from AIDoc import AIDoc
import sys
import ntpath
from Keyword import *
from ReaderUI import *

import PySimpleGUI as sg
import os
import os.path

filename = "testterms2.txt"
display_keywords = []
keyword_list = []
keyword_flag = 0
folder_flag = 0
#Setting up the UI components
title = "Kamata"
term_list_column = [
    [sg.Text("List of Terms Searched", key="TitleTerms")],
    [sg.InputText("", key="ProcessFile")],
    [sg.Button('Keyword File')],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")]
]
image_viewer_column = [
    [sg.Text("Select Folder to Process")],
    [sg.Button('FolderBrowse')],
    [sg.InputText("", key="ProcessFolder")],
    [sg.Submit()],
    [sg.InputText("",key="--STATUS--")]
]
# ----- Full layout -----
layout = [
    [
        sg.Column(term_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]


if 1:
    window = sg.Window("Term Viewer", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == 'Keyword File':
            print("file browse")
            filename = "testterms2.txt"
            keyword_flag = 0
            try:
                filename = sg.PopupGetFile('Select file', no_window=True)
                if filename: # Get list of files in folder
                    window.Element('ProcessFile').Update(filename)
                    print(filename)
                    test_list = open(filename).read().splitlines()
                    keyword_list = []
                    display_keywords = []
                    for term in test_list:
                        if term != '':
                            x = term.split(", ")
                            name = x[0]
                            weight = 0
                            if len(x) > 1:
                                print(x)
                                weight = x[1]
                            display_keywords.append(name)
                            keyword = Keyword(name, weight)
                            keyword_list.append(keyword)

                    print(test_list)
                    for x in keyword_list:
                        l = x.getWeight()
                        print(l)
                        print(x.getName())
                    window["-FILE LIST-"].update(display_keywords)
                    keyword_flag = 1
            except:
                file_list = []

        elif event == 'FolderBrowse':  # A file was chosen from the listbox
            print("folder browse")
            folder_flag = 0
            try:
                foldername = sg.PopupGetFolder('Select folder', no_window=True)
                if foldername:  # `None` when clicked `Cancel` - so I skip it
                    filenames = sorted(os.listdir(foldername))
                    # it use `key='files'` to `Multiline` widget
                    print(filenames)
                    folder_flag = 1
                    window.Element('ProcessFolder').Update(foldername)

            except:
                pass
        elif event == "Submit":
            print("submit")
            window.Element('--STATUS--').Update("submit button pushed")
            if (keyword_flag and folder_flag):
                for fname in os.listdir(foldername):
                    try:
                        #initialize instances
                        kw_instance = [0 for i in range(len(display_keywords))]
                        #TO BE CHANGED TO Keywords with weights
                        changeflag = 0

                        # Open the .docx file
                        if 0:
                            document = Document(os.path.join(docpath, filename))
                            paragraphs = document.paragraphs

                        if 1:
                            document = open(os.path.join(foldername, fname))
                            for line in document.readlines():  # to extract the whole text
                                i = 0
                                for word in display_keywords:
                                    if word.lower() in line.strip().lower():
                                        kw_instance[i] = kw_instance[i] + 1
                                        if changeflag == 0:
                                            changeflag = 1
                                    i = i + 1


                        # Search returns true if found
                        if 0:
                            for par in paragraphs:  # to extract the whole text
                                i = 0
                                for word in display_keywords:
                                    if word.lower() in par.text.lower():
                                        kw_instance[i] = kw_instance[i] + 1
                                    i = i + 1
                                    if changeflag == 0:
                                        changeflag = 1

                        if changeflag:
                            results_name = "results4.txt"
                            results_file = open(results_name,"a")
                            results_file.write(filename + "; ")

                            for strindex in range(len(display_keywords)):
                                kwval = kw_instance[strindex]
                                if kwval > 0:
                                    term = display_keywords[strindex]
                                    occurances = str(kwval)
                                    results_file.write(term + " appears " + occurances + " times," + " ")

                            results_file.write("\n\n")
                            results_file.close()
                            window.Element('--STATUS--').Update("written to " + results_name)


                    except:
                        print('fix an error')
                        window.Element('--STATUS--').Update("fix an error")
                        exit()
    window.close()



