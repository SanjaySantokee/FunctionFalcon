import wolframalpha
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pyperclip
from PIL import Image, ImageTk

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config.get('API', 'API_KEY')
client = wolframalpha.Client(api_key)


# Define a function to process the input and update the output label and history
def calculate():
    # Get the input from the user
    input_str = input_box.get('1.0', tk.END)

    # Call the Wolfram Alpha API to process the input and get the result
    res = client.query(input_str)

    # Extract the result from the API response
    answer = next(res.results).text

    # Update the output label with the result
    output_label.config(text='Answer: ' + answer)

    # Add the input and output to the history list
    history_list.insert(0, input_str.strip() + ' = ' + answer)


# Define a function to copy the answer to the clipboard
def copy_answer():
    answer = output_label['text'][8:]
    pyperclip.copy(answer)
    tkinter.messagebox.showinfo('Copied', 'Answer copied to clipboard!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a new tkinter window
    window = tk.Tk()
    window.title('Math Solver')

    # Set the window icon to an "addition" and a "multiplication" icon
    addition_icon = tk.PhotoImage(file='addition.png')
    window.iconphoto(True, addition_icon)

    # Create a label and a text area for the user to enter a math question or expression
    input_label = ttk.Label(window, text='Enter a math question or expression:')
    input_label.pack()
    input_box = tk.Text(window, height=10)
    input_box.pack()

    # Create a button to submit the input and calculate the result
    calculate_button = ttk.Button(window, text='Calculate', command=calculate)
    calculate_button.pack()

    # Create a frame for the output and copy button
    output_frame = ttk.Frame(window)
    output_frame.pack()

    # Create a label to display the result
    output_label = ttk.Label(output_frame, text='Answer:')
    output_label.pack(side='left')

    # Create a button to copy the answer to the clipboard
    copy_image = Image.open('copy.png').resize((16, 16))
    copy_icon = ImageTk.PhotoImage(copy_image)
    copy_button = ttk.Button(output_frame, image=copy_icon, command=copy_answer)
    copy_button.pack(side='left')

    # Create a frame for the history pane
    history_frame = ttk.Frame(window)
    history_frame.pack(side='bottom', fill='x')

    # Create a label for the history pane
    history_label = ttk.Label(history_frame, text='History:')
    history_label.pack()

    # Create a listbox to display the history
    history_list = tk.Listbox(history_frame)
    history_list.pack(fill='both', expand=True)

    # Start the tkinter event loop
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
