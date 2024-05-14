def chiffrage(Sentence_C):

    resultat_CC = ""

    # Remplacement des espaces
    Sentence_without_space = Sentence_C.replace(" ", "") 

    # Phrase une lettre sur deux
    Sentence_A = Sentence_without_space[::2] # en commençant à la première lettre
    Sentence_B = Sentence_without_space[1::2] # en commençant à la deuxième lettre

    resultat_CC = Sentence_A + Sentence_B
    
    return resultat_CC


