from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os
import parsing


class Application:
    def __init__(self):
        self.window = Tk()
        self.window.title("Summative")
        self.window.geometry("1920x1080")

        button_upload_csv = Button(self.window, text="Upload CSV", command=self.load_csv)
        button_upload_csv.pack()

        button_import_json = Button(self.window, text="Upload JSON", command=self.load_json)
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
                df = parsing.parse(freq_file, airport_file)
                self.on_data_loaded(df)

    def load_json(self):
        filetypes = (
            ('json files', '*.json'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Select exported JSON file',
            initialdir='/',
            filetypes=filetypes)

        if filename:
            df = parsing.load(filename)
            self.on_data_loaded(df)


    def on_data_loaded(self, df):
        self.df = df
        export_json_button = Button(self.window, text="Export JSON file", command=self.export_json)
        messagebox.showinfo("Message", "JSON file is loaded")
        export_json_button.pack()
        show_table(self.window, self.df)
        show_small_airport_chart(self.window, self.df)
        show_all_chart(self.window, self.df)
            
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
            parsing.save(self.df, filename)
            messagebox.showinfo("Message", f"JSON file is exported to {filename}")

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

def show_small_airport_chart(window, df):
    f = Figure(figsize=(12, 4), dpi=80)
    canvas = FigureCanvasTkAgg(f, master=window)
    small_airport = df[df['type'] == 'small_airport']
    sp = f.add_subplot()
    sp.hist(small_airport['freq'], bins=50, log=True)
    sp.set_title('Small airport Frequency')
    sp.set_xlabel('Frequency')
    sp.set_ylabel('Amount of airport')
    
    canvas.draw()
    canvas.get_tk_widget().pack()

def show_all_chart(window, df):
    f2 = Figure(figsize=(12, 4), dpi=80)
    canvas2 = FigureCanvasTkAgg(f2, master=window)
    small_airport = df[df['type'] == 'small_airport']
    medium_airport = df[df['type'] == 'medium_airport']
    large_airport = df[df['type'] == 'large_airport']
    colors = ['red', 'tan', 'lime']
    labels = ['small', 'medium', 'large']
    all_airport = [small_airport['freq'], medium_airport['freq'], large_airport['freq']]
    sp2 = f2.add_subplot()
    sp2.hist(all_airport, bins=50, log= True, histtype='bar', color=colors, label=labels)
    sp2.legend(prop={'size': 10})
    sp2.set_ylabel('Amount of airport')
    sp2.set_xlabel('Frequencies')
    sp2.set_title('All airport frequencies correlation')

    canvas2.draw()
    canvas2.get_tk_widget().pack()

def main():
    Application()


if __name__ == "__main__":
    main()
