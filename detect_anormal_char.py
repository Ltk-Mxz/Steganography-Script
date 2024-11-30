import unicodedata

# Texte à analyser
text = "Ｃhｏose  a  jοｂ  yоu lονｅ,  and  you  ｗіｌl  ｎeｖｅｒ  have tο ｗｏrk  a  day  in  yοur lіfｅ．   ."

# Fonction pour détecter les caractères anormaux
def detect_anomalous_characters(input_text):
    anomalous_chars = []
    for char in input_text:
        # Vérifie si le caractère est ASCII standard
        if char not in map(chr, range(32, 127)):
            # Ajoute les caractères non-standards à la liste
            anomalous_chars.append(char)
    return anomalous_chars

# Récupération des caractères anormaux
anomalous_chars = detect_anomalous_characters(text)

# Affichage des caractères détectés
print("Caractères anormaux détectés :", "".join(anomalous_chars))
