from tkinter import *
from tkinter import filedialog
from folder_content import folder_content
import webbrowser


class InterfaceTk:
    def __init__(self):
        self.folder_name = ""
        self.folder_output_name = ""

        self.window = Tk()
        self.window.title("Folder content")
        self.window.geometry("445x450")
        self.window.config(bg="gray")

        self.label = Label(text="Select a folder to crate an exel file with all file names", bg="gray", pady=20)
        self.label.grid(row=0, column=0, padx=48)

        self.label_browse = Label(text="Select a folder", bg="gray", justify=LEFT, anchor="w")
        self.label_browse.grid(row=2, column=0, sticky=W, padx=50, pady=5)

        self.button_browse = Button(text="Browse...", fg="red", justify=LEFT, anchor="w", borderwidth=0,
                                    command=self.browse_files)
        self.button_browse.grid(row=3, column=0, sticky=W, padx=50, pady=10)

        self.selected_folder = Label(text="Selected folder", bg="gray", justify=LEFT, anchor="w")
        self.selected_folder.grid(row=4, column=0)

        self.output_folder_select = Button(text="Select where to save the Excel list", fg="red", justify=LEFT,
                                           anchor="w", borderwidth=0,
                                           command=self.browse_output)
        self.output_folder_select.grid(row=5, column=0, sticky=W, padx=50, pady=5)

        self.selected_output_folder = Label(text="Selected output folder", bg="gray", justify=LEFT, anchor="w")
        self.selected_output_folder.grid(row=6, column=0)

        self.button_go = Button(text="GO", background="red", padx=50, pady=50, borderwidth=0, command=self.read_folder)
        self.button_go.grid(row=7, column=0, columnspan=2, padx=40, pady=20)

        self.button_output = Button(text="Go to output folder", justify=LEFT, anchor="w", borderwidth=0,
                                    command=self.open_output_folder)
        self.button_output.grid(row=8, column=0, padx=50, pady=20, sticky=W)

        self.window.mainloop()

    def browse_files(self):
        self.folder_name = filedialog.askdirectory(initialdir="/")
        self.selected_folder.configure(text="Folder Selected: "+self.folder_name)

    def browse_output(self):
        self.folder_output_name = filedialog.askdirectory(initialdir="/")
        self.selected_output_folder.configure(text="Output folder: "+self.folder_output_name)

    def read_folder(self):
        folder_content(self.folder_name, self.folder_output_name)

    def open_output_folder(self):
        webbrowser.open(f"file:///{self.folder_output_name}")
