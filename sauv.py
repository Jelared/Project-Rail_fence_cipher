def dechiffrage():
    Sentence = "Jsiueolruseusnpueoses"
    # Calcul de la longueur et séparation en deux phrases
    longueur_phrase = len(Sentence)
    split_sentence = longueur_phrase//2
    Sentence_A = Sentence[:split_sentence]
    Sentence_B = Sentence[split_sentence:]
    
    # Boucle pour sélectionner alternativement une lettre de chaque phrase
    Resultat = ""
    for lettreA, lettreB in zip(Sentence_A, Sentence_B):
        Resultat += lettreA + lettreB
        
    # Ajout d'une lettre si impaire
    if longueur_phrase % 2 != 0:
        Resultat += Sentence[-1]
    
    print(Sentence_A)
    print(Sentence_B)
    print(Resultat)

dechiffrage()
