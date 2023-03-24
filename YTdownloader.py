import time

from tkinter import *
from pytube import YouTube
from tkinter import messagebox

root = Tk()
root.title("YouTube Downloader")

# Creo file per ricordare il percorso della cartella di download
def remember_file():
    import os

    # Controlla se il file "remember.txt" esiste già
    if os.path.isfile("remember.txt"):
        print("Il file 'remember.txt' esiste già.")
    else:
        # Crea il file "remember.txt"
        with open("remember.txt", "w") as f:
            f.write("Questo è il file di remember.")
        print("Il file 'remember' è stato creato con successo.")

# Funzione per il download del video
def download():
    remember_file()
    try:

        # Ottieni il link dallo spazio di input di testo
        link = YouTube(link_entry.get())

        # Ottieni la cartella di destinazione dallo spazio di input di testo
        destination_folder = destination_entry.get()

        # Scarica il video nella cartella di destinazione
        video = link.streams.first()
        video.download(destination_folder)

        # Mostra il messaggio di conferma del download
        messagebox.showinfo("Download completato", "Il video è stato scaricato con successo!")

    except:
        # Mostra un messaggio di errore se il download fallisce
        messagebox.showerror("Errore", "Si è verificato un errore durante il download del video.")



# Dimensioni generiche della finestra
root.geometry("800x600+100+100")


# Spazio di input di testo per il link del video
link_label = Label(root,height=2,text="Inserisci il link del video:", font=("Helvetica"))
link_label.pack()
link_entry = Entry(root, width=50)
link_entry.pack()

# Spazio di input di testo per la cartella di destinazione
destination_label = Label(root,height=2, text="Inserisci il percorso della cartella di destinazione:", font=("Helvetica"))
destination_label.pack()
destination_entry = Entry(root, width=50)
destination_entry.pack()

# Aggiungi uno spaziatore verticale
spacer = Label(root, height=1).pack()


# Bottone per avviare il download
download_button = Button(root,height=3, text="Download", font=("Helvetica"), background="Orange", command=download)
download_button.pack()

# language
lang= StringVar()
r1= Radiobutton(root, text="Italiano", value="ita", variable=lang, font="Arial")
r2= Radiobutton(root, text="English",value="eng", variable=lang, font="Arial")
r1.pack()
r1.select()
r2.deselect()
r2.pack()
root.mainloop()
