import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

class Kviz:
    def __init__(self, master):
        self.master = master
        self.master.title("Kviz Moja kuhinja")
        self.master.geometry("620x700")
        self.master.configure(bg='black')

        # Postavite željeni font
        veliki_font = ("Gagalin", 28, "bold italic")

        # Primjer korištenja fonta
        label_text = "Dobrodošao u kviz Moja kuhinja"
        label = tk.Label(self.master, text=label_text, font=veliki_font)
        label.pack(pady=20)

        # Učitavanje bijele slike
        putanja_do_slike = "/home/ivan/Preuzimanja/image.png"  # Prilagodite putanju prema stvarnoj lokaciji slike
        bijela_slika = Image.open(putanja_do_slike)
        bijela_slika = ImageTk.PhotoImage(bijela_slika)

        # Postavljanje bijele slike na prozor
        self.labela_slika = tk.Label(self.master, image=bijela_slika, bg='black')
        self.labela_slika.image = bijela_slika
        self.labela_slika.pack(fill='both', expand=True)

        self.pitanja = [
            {
                "pitanje": "Voliš li kuhati?",
                "odgovori": ["Da", "Ne", "Ponekada"],
                "tocan_odgovor": "Da"
            },
            {
                "pitanje": "Kako se zove simbioza mesožderstva i veganstva od kiselog kupusa?",
                "odgovori": ["Sekeli gulaš", "Sarma", "Ćufte"],
                "tocan_odgovor": "Sarma"
            },
            {
                "pitanje": "Smije li se voda sipati u vruću mast?",
                "odgovori": ["Naravno", "Nikada", "Po potrebi"],
                "tocan_odgovor": "Nikada"
            },
            {   
                "pitanje": "Zaprška je?",
                "odgovori": ["Mješavina brašna i ulja", "Prženo brašno na ulju/masti", "Ukuhano brašno u pasiranu rajčicu"],
                "tocan_odgovor": "Prženo brašno na ulju/masti"
            },
            {   
                "pitanje": "Vegeta se ne smije stavljati u?",
                "odgovori": ["Juhu i umake", "Na meso i u salate", "U čobanac i fish paprikaš"],
                "tocan_odgovor": "U čobanac i fish paprikaš"
            },
            {   
                "pitanje": "Pohovani šaran se ne smije poslužiti uz?", 
                "odgovori": ["Francusku salatu", "Krumpir salatu", "Tartar umak"],
                "tocan_odgovor": "Francusku salatu"
            },

            # Dodajte više pitanja po potrebi
        ]
 
        self.trenutno_pitanje = 0
        self.tocni_odgovori = 0

        self.prikazi_pitanje()

    def prikazi_pitanje(self):
        pitanje_label = tk.Label(self.master, text=self.pitanja[self.trenutno_pitanje]["pitanje"], bg='black', fg='white')
        pitanje_label.pack(pady=20)

        if "slika" in self.pitanja[self.trenutno_pitanje]:
            slika = Image.open(self.pitanja[self.trenutno_pitanje]["slika"])
            slika = ImageTk.PhotoImage(slika)
            slika_label = tk.Label(self.master, image=slika, bg='black')
            slika_label.image = slika
            slika_label.pack(pady=20)

        for odgovor in self.pitanja[self.trenutno_pitanje]["odgovori"]:
            odgovor_button = tk.Button(self.master, text=odgovor, command=lambda o=odgovor: self.provjeri_odgovor(o))
            odgovor_button.pack(pady=5)

    def provjeri_odgovor(self, odgovor):
        tocan_odgovor = self.pitanja[self.trenutno_pitanje]["tocan_odgovor"]
        if odgovor == tocan_odgovor:
            self.tocni_odgovori += 1

        self.trenutno_pitanje += 1

        if self.trenutno_pitanje < len(self.pitanja):
            self.ponovno_prikazi_pitanje()
        else:
            self.prikazi_cestitku()

    def ponovno_prikazi_pitanje(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.prikazi_pitanje()

    def prikazi_cestitku(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        cestitka_label = tk.Label(self.master, text=f"Čestitamo! Točnih odgovora: {self.tocni_odgovori}", bg='black', fg='white')
        cestitka_label.pack(pady=10)

        # Ovdje možete dodati kod za prikaz slike ili drugih elementa čestitke
    def prikazi_cestitku(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        novi_prozor = tk.Toplevel(root)
        novi_prozor.title("Čestitamo!")
     
        # Učitaj sliku za čestitanje
        putanja_do_cestitke = "/home/ivan/Radna površina/moja kuhinja diploma.png"  # Prilagodite putanju prema stvarnoj lokaciji slike
        slika_cestitke = Image.open(putanja_do_cestitke)
        slika_cestitke = ImageTk.PhotoImage(slika_cestitke)

        

        # Prikaz čestitke samo ako su sva pitanja točno odgovorena
        if self.tocni_odgovori == len(self.pitanja):
            cestitka_label = tk.Label(self.master, text=f"Čestitamo! Točnih odgovora: {self.tocni_odgovori}", bg='black', fg='white')
            cestitka_label.pack(pady=10)

            # Postavi sliku na novi prozor
            self.labela_cestitke = tk.Label(novi_prozor, image=slika_cestitke)
            self.labela_cestitke.image = slika_cestitke
            self.labela_cestitke.pack()

            # Dodajte gumb za printanje čestitke
            print_button = tk.Button(self.master, text="Printaj čestitku", command=self.printaj_cestitku)
            print_button.pack(pady=5)

        zatvori_button = tk.Button(self.master, text="Zatvori", command=self.master.destroy)
        zatvori_button.pack(pady=5)

    def printaj_cestitku(self):
        # Dodajte kod za printanje čestitke
        print("Čestitamo! Točnih odgovora:", self.tocni_odgovori)
        # Dodajte ostatak koda za printanje čestitke


        zatvori_button = tk.Button(self.master, text="Zatvori", command=self.master.destroy)
        zatvori_button.pack(pady=5)

        

if __name__ == "__main__":
    root = tk.Tk()
    kviz = Kviz(root)
    root.mainloop()

