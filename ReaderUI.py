import PySimpleGUI as sg
import os.path

class ReaderUI:

    def __init__(self):
        self.title = "Kamata"
        self.term_list_column = [
            [sg.Text("List of Terms Searched", key="TitleTerms")],
            [sg.FileBrowse(), sg.Text("", key="FileName")],
            [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")]
        ]

        # For now will only show the name of the file that was chosen
        self.image_viewer_column = [
            [sg.Text("Select Folder to Process")],
            [sg.Text("Folder                     "), sg.FolderBrowse()],
            [sg.Text("",key="ProcessFolder")],
            [sg.Submit()],
            [sg.Text("",key="ProcessStatus")]
        ]

        # ----- Full layout -----
        self.layout = [
            [
                sg.Column(self.term_list_column),
                sg.VSeperator(),
                sg.Column(self.image_viewer_column),
            ]
        ]


    def setUI(self):
        if 1:
            window = sg.Window("Term Viewer", self.layout)

            # Create an event loop
            while True:
                event, values = window.read()
                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                # Folder name was filled in, make a list of files in the folder
                if event == "FileName":
                    folder = values["-FOLDER-"]
                    try:
                        # Get list of files in folder
                        file_list = os.listdir(folder)
                    except:
                        file_list = []


                    fnames = [
                        f
                        for f in file_list
                        if os.path.isfile(os.path.join(folder, f))
                           and f.lower().endswith((".png", ".txt"))
                    ]
                    window["-FILE LIST-"].update(fnames)
                elif event == "-FILE LIST-":  # A file was chosen from the listbox
                    try:
                        filename = os.path.join(
                            values["-FOLDER-"], values["-FILE LIST-"][0]
                        )
                        window["-TOUT-"].update(filename)
                        window["-IMAGE-"].update(filename=filename)

                    except:
                        pass

            window.close()
