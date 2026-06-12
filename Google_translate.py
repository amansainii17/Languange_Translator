from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    # Convert source and destination language names to codes
    src_code = [key for key, value in LANGUAGES.items() if value.lower() == src.lower()]
    dest_code = [key for key, value in LANGUAGES.items() if value.lower() == dest.lower()]

    if not src_code or not dest_code:
        return "Invalid source or destination language."

    try:
        trans1 = trans.translate(text, src=src_code[0], dest=dest_code[0])
        return trans1.text
    except Exception as e:
       return "Translation error: {}".format(e)

def data():
    s = comb1_sor.get()
    d = comb1_dest.get()
    masg = Sor_txt.get(1.0, END).strip()
    if not masg:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, "Please enter text to translate.")
        return
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

# Initialize GUI
root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='Red')

# Title Label
lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg='red', fg='white')
lab_txt.place(x=100, y=40, height=50, width=300)

# Source Text Label
lab_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="red")
lab_txt.place(x=100, y=100, height=20, width=300)

# Source Text Box
Sor_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

# Language Comboboxes
list_text = list(LANGUAGES.values())

comb1_sor = ttk.Combobox(root, value=list_text, font=("Times New Roman", 12))
comb1_sor.place(x=10, y=300, height=40, width=150)
comb1_sor.set("English")

button_change = Button(root, text="Translate", relief=RAISED, command=data, bg="blue", fg="white", font=("Times New Roman", 12, "bold"))
button_change.place(x=170, y=300, height=40, width=150)

comb1_dest = ttk.Combobox(root, value=list_text, font=("Times New Roman", 12))
comb1_dest.place(x=330, y=300, height=40, width=150)
comb1_dest.set("Hindi")

# Destination Text Label
lab_txt = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="red")
lab_txt.place(x=100, y=360, height=20, width=300)

# Destination Text Box
dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

# Run GUI
root.mainloop()
