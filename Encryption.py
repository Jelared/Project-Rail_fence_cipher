def chiffrage(Sentence):

    resultat = ""

    # Remplacement des espaces
    Sentence_without_space = Sentence.replace(" ", "") 

    # Phrase une lettre sur deux
    Sentence_A = Sentence_without_space[::2] # en commençant à la première lettre
    Sentence_B = Sentence_without_space[1::2] # en commençant à la deuxième lettre

    resultat = Sentence_A + Sentence_B
    
    return resultat

def dechiffrage(Sentence):

    # Calcul de la longueur et séparation en deux phrases
    longueur_phrase = len(Sentence)
    split_sentence = longueur_phrase//2
    Sentence_A = Sentence[:split_sentence]
    Sentence_B = Sentence[split_sentence:]
    
    # Boucle pour sélectionner alternativement une lettre de chaque phrase
    resultat = ""
    for lettreA, lettreB in zip(Sentence_A, Sentence_B):
        resultat += lettreA + lettreB
        
    # Ajout d'une lettre si impaire
    if longueur_phrase % 2 != 0:
        resultat += Sentence[-1]
    
    return resultat
