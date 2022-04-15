import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

df = DataFrame('Formative/out.json', columns= ['airport_id', 'freq', 'type'])
root= tk.Tk()

figure = plt.Figure(figsize=(10, 10), dpi = 100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack()
df = df[['airport_id', 'freq', 'type']]
df.plot(kind='bar', legend=True, ax=ax)
ax.set_title = ('Airport data')

root.maiinloop()
