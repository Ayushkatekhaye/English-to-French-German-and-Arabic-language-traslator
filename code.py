import tkinter as tk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES

def find_translation():
    input_sentence = input_sentence_entry.get().strip()

    # Check if the user input is an empty string.
    if not input_sentence:
        messagebox.showerror("Error", "Please enter a sentence in French, German, Arabic, or another language.")
        return

    try:
        if input_language.get() == "Other":
            open_googletrans_window(input_sentence)
        else:
            with open(f'{input_language.get().lower()}.txt', 'r', encoding='utf-8') as input_file:
                input_sentences = input_file.read().splitlines()
            if input_sentence in input_sentences:
                index = input_sentences.index(input_sentence)

                # Display the corresponding sentence from the English file.
                with open('english.txt', 'r', encoding='utf-8') as english_file:
                    english_sentences = english_file.read().splitlines()
                    english_translation = english_sentences[index]
                    results_label.config(text=f"English: {english_translation}", fg="black")
            else:
                messagebox.showinfo("Not Found", "The sentence is not found in the selected language files.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_googletrans_window(input_text):
    googletrans_window = tk.Toplevel(root)
    googletrans_window.title("Googletrans Translation")

    lang_label = tk.Label(googletrans_window, text="Enter the input language (e.g., 'fr' for French):", fg="blue")
    lang_label.pack()
    lang_entry = tk.Entry(googletrans_window)
    lang_entry.pack()

    def translate_with_googletrans():
        input_language_code = lang_entry.get().strip().lower()

        if input_language_code in LANGUAGES:
            translator = Translator()
            translation = translator.translate(input_text, dest="en", src=input_language_code)
            translation_text = translation.text
            results_label.config(text=f"English: {translation_text}", fg="black")
            googletrans_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid language code. Please enter a valid language code.")

    translate_button = tk.Button(googletrans_window, text="Translate", command=translate_with_googletrans, bg="blue", fg="white")
    translate_button.pack()

# Create the main window
root = tk.Tk()
root.title("Translation Reverser")

# Set the window size
root.geometry("800x500")

# Language selection
input_language_label = tk.Label(root, text="Choose the input language:", fg="blue",width=20)
input_language_label.pack()
input_language = tk.StringVar()
input_language.set("French")  # Default language
input_language_option_menu = tk.OptionMenu(root, input_language, "French", "German", "Arabic", "Other")
input_language_option_menu.pack()

# Input sentence entry
input_sentence_label = tk.Label(root, text="Enter a sentence in the selected language:", fg="blue")
input_sentence_label.pack()
input_sentence_entry = tk.Entry(root)
input_sentence_entry.pack()

# Find button
find_button = tk.Button(root, text="Find English Translation", command=find_translation, bg="blue", fg="white")
find_button.pack()

# Result label
results_label = tk.Label(root, text="", font=("Arial", 12))
results_label.pack()

# Start the main loop
root.mainloop()

