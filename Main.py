from Encryption import chiffrage
from Decryption import dechiffrage  

import customtkinter as ctk
root = ctk.CTk()

# titre de la fenetre
root.title("Rail Fence")

# taille de la fenetre
root.geometry("800x400")

########################################################################

def sequence_chiffrage():
    # récuperation de la phrase à chiffrer
    Sentence_C = entry.get()
    # Utilisation de la fonction et résultat
    resultat = chiffrage(Sentence_C)
    # Insertion du résultat
    entry_resultat_C.insert(0,resultat_C)

# Texte
label = ctk.CTkLabel(root, text="Ajouter la phrase à chiffrer", anchor="w")
label.pack(pady=20, padx=20, fill="x")

# Pour la saisie de texte
entry = ctk.CTkEntry(root, width=100)
entry.pack(padx=20, fill="x", anchor="w")

# Bouton pour enregistrer le texte et afficher le résultat
button = ctk.CTkButton(root, text="Chiffrage",command=sequence_chiffrage)
button.pack(pady=20,padx=20, anchor="w")

# Pour l'inscription du texte chiffrer
entry_resultat_C = ctk.CTkEntry(root, width=100)
entry_resultat_C.pack(padx=20, fill="x", anchor="w")

###########################################################################

def sequence_dechiffrage():
    # récuperation de la phrase à chiffrer
    Sentence_D = entry2.get()
    # Utilisation de la fonction et résultat
    resultat_D = dechiffrage(Sentence_D)
    # Insertion du résultat
    entry_resultat_D.insert(0,resultat_D)

# Texte
label2 = ctk.CTkLabel(root, text="Ajouter la phrase à dechiffrer", anchor="w")
label2.pack(pady=20, padx=20, fill="x")

# Pour la saisie de texte
entry2 = ctk.CTkEntry(root, width=100)
entry2.pack(padx=20, fill="x", anchor="w")

# Bouton pour enregistrer le texte et afficher le résultat
button2 = ctk.CTkButton(root, text="dechiffrage",command=sequence_dechiffrage)
button2.pack(pady=20,padx=20, anchor="w")

# Pour l'inscriptiuon du texte chiffrer
entry_resultat_D = ctk.CTkEntry(root, width=100)
entry_resultat_D.pack(padx=20, fill="x", anchor="w")

root.mainloop()
