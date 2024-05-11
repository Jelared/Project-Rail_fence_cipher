resultat = ""

# Input
Sentence = input("Phrase à chiffrer: ")

# Remplacement des espaces
Sentence_without_space = Sentence.replace(" ", "") 

# Phrase une lettre sur deux
Sentence_A = Sentence_without_space[::2] # en commençant à la première lettre
Sentence_B = Sentence_without_space[1::2] # en commençant à la deuxième lettre

resultat = Sentence_A + Sentence_A
    
print(resultat)