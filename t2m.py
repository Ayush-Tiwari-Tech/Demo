import os
from tkinter import *
from gtts import gTTS
from tkinter import messagebox

def convert_text_to_speech():
    text = text_input.get("1.0", END).strip()
    if text == "":
        messagebox.showerror("Error", "Please enter some text.")
        return

    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("output.mp3")

    messagebox.showinfo("Success", "MP3 file created successfully as output.mp3!")

    # Auto-play (Windows)
    os.system("start output.mp3")
    # For macOS: os.system("afplay output.mp3")
    # For Linux: os.system("mpg123 output.mp3")

# Create GUI window
root = Tk()
root.title("Text to MP3 Converter")
root.geometry("400x300")
root.resizable(False, False)

# Heading
Label(root, text="Enter text to convert to MP3", font=("Arial", 14)).pack(pady=10)

# Text input
text_input = Text(root, wrap=WORD, font=("Arial", 12), height=8)
text_input.pack(padx=10, pady=5)

# Convert button
Button(root, text="Convert to MP3", command=convert_text_to_speech, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

# Run the GUI
root.mainloop()
