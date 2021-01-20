# Import the module
from docx import Document
from AIDoc import AIDoc
import sys
import ntpath
import PySimpleGUI as sg
import os

ai_list = open("implementationterms.txt").read().splitlines()
ai_instance = []


layout = [[sg.Text("PASCO")], [sg.Button("OK")]]

# Create the window
window = sg.Window("PASCO", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()


docpath = os.path.abspath(r'C:\Users\EMOORSA\PycharmProjects\AIMLReader\Txt')
for filename in os.listdir(docpath):
    try:

        #initialize instances
        ai_instance = [0 for i in range(len(ai_list))]
        changeflag = 0

        # Open the .docx file
        if 0:
            document = Document(os.path.join(docpath, filename))
            paragraphs = document.paragraphs

        if 1:
            document = open(os.path.join(docpath, filename))
            for line in document.readlines():  # to extract the whole text
                i = 0
                for word in ai_list:
                    if word.lower() in line.strip().lower():
                        ai_instance[i] = ai_instance[i] + 1
                        if changeflag == 0:
                            changeflag = 1
                    i = i + 1


        # Search returns true if found
        if 0:
            for par in paragraphs:  # to extract the whole text
                i = 0
                for word in ai_list:
                    if word.lower() in par.text.lower():
                        ai_instance[i] = ai_instance[i] + 1
                    i = i + 1
                    if changeflag == 0:
                        changeflag = 1

        if changeflag:
            results_file = open("results3.txt","a")
            results_file.write(filename + "; ")

            for strindex in range(len(ai_instance)):
                aival = ai_instance[strindex]
                if aival > 0:
                    term = ai_list[strindex]
                    occurances = str(aival)
                    results_file.write(term + " appears " + occurances + " times," + " ")

            results_file.write("\n\n")
            results_file.close()

    except:
        print('fix an error')
        exit()


