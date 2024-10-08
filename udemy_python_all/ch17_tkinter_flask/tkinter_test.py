import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()


def hello():
    label = tk.Label(root, text='Hello World!', fg='green')
    canvas.create_window(250, 300, window=label)


button = tk.Button(text='Click Me!!', fg='black', command=hello, font=('helvetica', 12, 'bold'))
canvas.create_window(250, 250, window=button)
root.mainloop()
