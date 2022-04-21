from fileinput import filename
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import ttk
from cgitb import reset
import pandas as pd
import os
import formative

class Application:
    def __init__(self):
        self.window = Tk()
        self.window.title("Main Frame")
        self.window.geometry("4000x1000")

        button_upload_csv = Button(self.window, text="Upload csv", command=self.load_csv)
        button_upload_csv.pack()

        button_import_json = Button(self.window, text="Upload json", command=self.load_json)
        button_import_json.pack()

        self.window.mainloop()

    def load_csv(self):
        filetypes = (
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )

        airport_file = fd.askopenfilename(
            title='Select the file with airport data',
            initialdir='/',
            filetypes=filetypes)

        if airport_file:
            freq_file = fd.askopenfilename(
                title='Select the file with airport frequence',
                initialdir= os.path.dirname(airport_file),
                filetypes=filetypes)

            if freq_file:
                df = formative.parse(freq_file, airport_file)
                self.on_data_loaded(df)

    def load_json(self):
        filetypes = (
            ('json files', '*.json'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Select exported json file',
            initialdir='/',
            filetypes=filetypes)

        if filename:
            df = pd.read_json(filename)
            self.on_data_loaded(df)

    def on_data_loaded(self, df):
        self.df = df
        export_json_button = Button(self.window, text="Export Json file", command=self.export_json)
        messagebox.showinfo("Message", "Json file is loaded")
        export_json_button.pack()

    def export_json(self):
        filetypes = (
            ('json files', '*.json'),
            ('All files', '*.*')
        )
        filename = fd.asksaveasfilename(
            filetypes= filetypes,
            title="Where to save the file?"
        )
        if filename:
            formative.save(self.df, filename)
            messagebox.showinfo("Message", f"Json file is exported to {filename}")

def main():
    Application()

def select():
    result = []
    while(True):
        type = str(input("Enter airport type: "))
        if type == "small":
            result = df[df["type"] == "small_airport"]
        elif type == "medium":
            result = df[df["type"] == "medium_airport"]
        elif type == "large":
            result = df[df["type"] == "large_airport"]
        else: print("wrong input")
        print(result)

if __name__ == "__main__":
    main()
