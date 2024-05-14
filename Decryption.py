def dechiffrage(Sentence_D):

    # Calcul de la longueur et séparation en deux phrases
    longueur_phrase = len(Sentence_D)
    split_sentence = longueur_phrase//2
    Sentence_A = Sentence[:split_sentence]
    Sentence_B = Sentence[split_sentence:]
    
    # Boucle pour sélectionner alternativement une lettre de chaque phrase
    resultat_D = ""
    for lettreA, lettreB in zip(Sentence_A, Sentence_B):
        resultat_D += lettreA + lettreB
        
    # Ajout d'une lettre si impaire
    if longueur_phrase % 2 != 0:
        resultat_D += Sentence_D[-1]
    
    return resultat_D
