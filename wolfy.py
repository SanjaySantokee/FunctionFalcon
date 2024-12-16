import wolframalpha
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pyperclip
from PIL import Image, ImageTk
import os
import configparser


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ADDITION_ICON = os.path.join(BASE_DIR, 'data', 'addition.png')
COPY_ICON = os.path.join(BASE_DIR, 'data', 'copy.png')
CONFIG_FILE = os.path.join(BASE_DIR, 'data', 'config.ini')

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

api_key = config.get('API', 'API_KEY')
client = wolframalpha.Client(api_key)


def calculate():
    input_str = input_box.get('1.0', tk.END)
    res = client.query(input_str)
    answer = next(res.results).text
    output_label.config(text='Answer: ' + answer)
    history_list.insert(0, input_str.strip() + ' = ' + answer)


def copy_answer():
    answer = output_label['text'][8:]
    pyperclip.copy(answer)
    tkinter.messagebox.showinfo('Copied', 'Answer copied to clipboard!')

def copy_from_history(event):
    selection = history_list.get(history_list.curselection())
    pyperclip.copy(selection.split(' = ')[1])
    tkinter.messagebox.showinfo("Copied", "Answer copied to clipboard!")


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Wolfy')

    addition_icon = tk.PhotoImage(file=ADDITION_ICON)
    window.iconphoto(True, addition_icon)

    input_label = ttk.Label(window, text='Enter a math question or expression:')
    input_label.pack()
    input_box = tk.Text(window, height=10)
    input_box.pack()

    calculate_button = ttk.Button(window, text='Calculate', command=calculate)
    calculate_button.pack()

    output_frame = ttk.Frame(window)
    output_frame.pack()

    output_label = ttk.Label(output_frame, text='Answer:')
    output_label.pack(side='left')

    copy_image = Image.open(COPY_ICON).resize((16, 16))
    copy_icon = ImageTk.PhotoImage(copy_image)
    copy_button = ttk.Button(output_frame, image=copy_icon, command=copy_answer)
    copy_button.pack(side='left')

    history_frame = ttk.Frame(window)
    history_frame.pack(side='bottom', fill='x')

    history_label = ttk.Label(history_frame, text='History:')
    history_label.pack()

    history_list = tk.Listbox(history_frame)
    scroll_bar = ttk.Scrollbar(history_frame, orient='vertical', command=history_list.yview)
    history_list.configure(yscrollcommand=scroll_bar.set)
    scroll_bar.pack(side='right', fill='y')
    history_list.pack(fill='both', expand=True)

    history_list.bind('<Double-Button-1>', copy_from_history)

    window.mainloop()
