import unicodedata

# Texte à analyser
text = "Ｃhｏose  a  jοｂ  yоu lονｅ,  and  you  ｗіｌl  ｎeｖｅｒ  have tο ｗｏrk  a  day  in  yοur lіfｅ．"

# Fonction pour détecter les caractères invisibles ou homoglyphes
def detect_special_characters(input_text):
    special_chars = []
    for char in input_text:
        # Vérifie si le caractère n'est pas standard ASCII
        if char not in map(chr, range(32, 127)):
            special_chars.append(f"{char} (Unicode: {ord(char)}) - {unicodedata.name(char, 'UNKNOWN')}")
    return special_chars

# Analyse des caractères spéciaux
special_characters = detect_special_characters(text)

# Affichage des résultats
print("Caractères spéciaux détectés :")
for char_info in special_characters:
    print(char_info)
