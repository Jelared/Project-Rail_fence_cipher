# Boucle pour sélectionner alternativement une lettre de chaque phrase
longueur_phrase = min(len(Sentence_A), len(Sentence_B))
for i in range(longueur_phrase):
    resultat += Sentence_A[i] + Sentence_B[i]

# Ajouter le reste de la phrase plus longue, si elle existe
if len(Sentence_A) > len(Sentence_B):
    resultat += Sentence_A[longueur_phrase:]
elif len(Sentence_B) > len(Sentence_A):
    resultat += Sentence_B[longueur_phrase:]