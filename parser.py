#!/usr/bin/python
# -*- coding: utf-8 -*-
   
import re
import sys

txt = ''
output = ''

#terminaison du fichier à lire 
filename_end = re.compile('(?<=\\w\\.)txt$')

###Le lexique pour dissatisfaction
dissatisfaction1 = ["moins de besoins", "peu de besoins"]
dissatisfaction2 = ["ni plus intéressant", "plus ultra de la belle", "rien de plus simple", "pas moins intéressants", "point du tout agréables",
	"pas moins de bonnes", "assez coûteux", "Rien de plus beau", "plus aussi bon", "pas fort contente", "ne me satisfait plus entièrement"]
dissatisfaction3 = ["Ne me contentant pas", "pas un simple", "pas simples", "ne se contente pas de", "seulement insuffisante", 
	"ne se contentât pas de", "assez mécontent", "pas satisfait", "pas un bon", "si fade", "pas les bonnes", "pas de belles", "pas bon",
	 "pas de bon", "le moins mauvais"]
dissatisfaction4 = ["pas abouti", "nul pour ainsi dire", "pas moins bien", "loin d'être aussi bien", "guère réussi", "besoin particulier",
	"pas tout le bien", "grossièrement imaginée", "passablement ennuyeux", "grand besoin", "assez bizarres", "point du tout remarquable", 
	"pas tant de bien", "privé de tout"]
dissatisfaction5 = ["sans aucune satisfaction", "si grand besoin", "mal fait", "très incertaine", "pas réussi", "for incertaines", 
	"pas moins le grand", "tellement grossiers", "mal faites", "pas de bien", "pas assez grand", "besoins absolument nécessaires", "pas bien"
	"beaucoup de besoins", "besoin insatiable", "point contents", "immense besoin", "rien de plus saisissant", "pur besoin", "pas plus grande",
	"plus de besoin", "pas aussi grands", "pas si grand", "pas un bien"]
dissatisfaction6 = ["profonde injustice", "pas grand", "si mauvaise", "fort laid", "très insuffisant", "sans grandeur", "très pénible", 
	"pas étonnant", "bien insuffisantes", "complètement incertaines", "très mauvaises", "très mauvais", "plus grossières", "essentiellement nulles",
	"pas une grande", "mauvaises sans doute", "si stupides", "pas les grands", "pas d'énormes", "presque effrayantes", "pas proprement brillante",
	"fort pénible", "plus grossiers", "sans grand", "pas si fantastique", "bien mauvais", "aussi stupide", "bien médiocres", "plus incertaine",
	"pas un grand", "sans grande", "sans grandement", "si nul", "bien nulle", "passablement lamentable", "pas de grands"]
dissatisfaction7 = ["parfaitement ennuyeuses", "souveraine injustice", "plus mauvaises", "ni classe", "tout à fait insuffisant",
	"beaucoup insuffisante", "les plus mauvais", "absolument insuffisants", "plus stupides", "plus laids", "nul plus", "infiniment pénible",
	"ni bien", "la plus pénible", "farouche stupidité", "pas parfaitement", "plus laid", "absolument nulles", "la plus mauvaise", "vraiment insuffisante"]
dissatisfaction8 = ["ni grand", "point de perfection", "si affreux", "si atroce", "plus rebutant", "Rien de grand", "laid foncièrement",
	"point original", "plus pitoyable", "point d'une grande", "ni la perfection", "ni grandeur"]
dissatisfaction9 = ["point le plus important", "les plus affreux", "rien d'extraordinaire"]
dissatisfaction10 = ["ni la plus grande"]

dissatisfaction = []
dissatisfaction.append(dissatisfaction1)
dissatisfaction.append(dissatisfaction2)
dissatisfaction.append(dissatisfaction3)
dissatisfaction.append(dissatisfaction4)
dissatisfaction.append(dissatisfaction5)
dissatisfaction.append(dissatisfaction6)
dissatisfaction.append(dissatisfaction7)
dissatisfaction.append(dissatisfaction8)
dissatisfaction.append(dissatisfaction9)
dissatisfaction.append(dissatisfaction10)



def addBaliseDissatisfaction(txt, output):
	sentence2 = ''
	for sentence in txt.readlines():
		for i in range(0,len(dissatisfaction)):
			for j in range(0,len(dissatisfaction[i])):
				if sentence.find(dissatisfaction[i][j]) != -1:
					sentence2 = '<dissatisfaction int=' + str(i+1) +'>' + sentence + '</dissatisfaction>'
		if sentence2 != '':
			output += sentence2
			sentence2 = ''
		else:
			output += sentence
	return output

if len(sys.argv) < 2 or filename_end.findall(sys.argv[1]) == []:
    exit("Usage: parser *.txt")

with open(sys.argv[1], 'r', encoding="utf8") as txt_file:
		output = addBaliseDissatisfaction(txt_file, output)

with open('fichier.txt', 'w',encoding="utf8") as final_file:
    final_file.write(output)

exit(0)
