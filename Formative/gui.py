from fileinput import filename
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import ttk
from cgitb import reset
from matplotlib.pyplot import table
import pandas as pd
import os
import formative
import numpy as np
from statistics import mode

class Application:
    def __init__(self):
        self.window = Tk()
        self.window.title("Main Frame")
        self.window.geometry("1000x500")

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
            df = formative.load(filename)
            self.on_data_loaded(df)


    def on_data_loaded(self, df):
        self.df = df
        export_json_button = Button(self.window, text="Export Json file", command=self.export_json)
        messagebox.showinfo("Message", "Json file is loaded")
        export_json_button.pack()
        show_table(self.window, self.df)
            
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

def show_table(window, df):
    table = ttk.Treeview(window, height=2)
    table['columns'] = ('group', 'mean', 'mode', 'median')

    table.column("#0", width=0,  stretch=NO)
    table.column('group', anchor=CENTER, width=150)
    table.column('mean', anchor=CENTER, width=150)
    table.column('mode', anchor=CENTER, width=100)
    table.column('median', anchor=CENTER, width=100)

    table.heading("#0",text="",anchor=CENTER)
    table.heading("group",text="Group",anchor=CENTER)
    table.heading("mean",text="Mean",anchor=CENTER)
    table.heading("mode",text="Mode",anchor=CENTER)
    table.heading("median",text="Median",anchor=CENTER)


    large_airport = df[df['type'] == 'large_airport']
    more_than_100mhz = df[df['freq'] > 100]

    table.insert(parent='',index='end',iid=0,text='',
    values=('large_airport', large_airport['freq'].mean(), large_airport['freq'].mode().values[0], large_airport["freq"].median()))
    table.insert(parent='',index='end',iid=1,text='',
    values=('more_than_100mhz', more_than_100mhz['freq'].mean(), more_than_100mhz['freq'].mode().values[0], more_than_100mhz["freq"].median()))
    
    table.pack()
def main():
    Application()


if __name__ == "__main__":
    main()
