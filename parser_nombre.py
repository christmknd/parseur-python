#!/usr/bin/python
# -*- coding: utf-8 -*-
   
import re
import sys

txt = ''
output = ''

#terminaison du fichier à lire 
filename_end = re.compile('(?<=\\w\.)txt$')

###Le lexique pour la quantification
###Par simplification , les nombres composées comme "vingt-et-un" ne seront pas parsées ici 
 
#chiffre et nombre 
quantification1 =  ["zero","un","une","uns","deux","trois","quatres","cinq","six","sept","huit","neuf","dix",
					"onze","douze","treize","quatorze","quinze","seize",
					"vingt","trente","quanrante","cinquante","soixante","soixante-dix","quatres-vingt","quatres-vingt-dix"
					"cent","cents","mille","milles","million","millions","milliard","milliards"]
#adjectif numéral
quantification2 = ['zéroième', 'zéroièmes', 'zérotième', 'zérotièmes',"premier","premiers",'unième', 'unièmes',"deuxième","deuxièmes","troisième","troisièmes","quatrième","quatrièmes","cinquième","cinquièmes",
				   "sixiéme","sixiémes","septième","septièmes","huitième","huitièmes","neuvième","neuvièmes","dixième","dizaine","dizaines",
				   "onzième","douzième","treizième","quatorzième","quinzième","seizième",
				   "vingtième","trentièmes","quanrantième","cinquantième","soixantième","soixante-dixième","quatres-vingtième","quatres-vingt-dix"
					"centaine","centaines","centième","centièmes","millième","millièmes","millionième","millionièmes","milliardième","milliardièmes"]

#position
quantification3 = ["second","second","seconde","antépénultième","antépénultième","avant-dernier","avant-derniers","pénultième","pénultièmes",
				   "dernier","derniers","dernière","dernières"]

#adverbe et expression exprimant l'ordre ou l'ordonnancement 
quantification4 = [ "avant","antérieur","antérieurement", "au préalable","auparavant","derrière","déjà","en amont","plus tôt","préalablement", "précédemment",
					"premièrement","dans un premier temps","primo","d'abord","tout d'abord",
					"deuxièmement","ensuite","par la suite","à la suite","a posteriori","plus tard","après coup","puis"
					"à la fin", "après tout", "bref","dernièrement","du moins", "en un mot", "finalement", "pour finir", "somme toute", "tout compte fait", "ultimo"]

#unités
quantification5 = ["mètre","mètres","miles","yard","pied","pieds","pouce","pouces","coudés","mile marin","année lumière","années lumières",
					"aire","hectares","nanomètre","millimètre","millimètres","centimètre","centimètres","décimètre","décamètre","hectomètre","kilomètre","kilomètres"]

#temps , espace temporel
quantification6 = ["minute","minutes","heure","heures","jour","jours","année","années","décennies","décennies","siècle","siècles","millénaire","millénaires"]



quantification = []
quantification.append(quantification1)
quantification.append(quantification2)
quantification.append(quantification3)
quantification.append(quantification4)
quantification.append(quantification5)
quantification.append(quantification6)




def addBalisequantification(txt, output):
	sentence2 = ''
	for sentence in txt.readlines():
		for i in range(0,len(quantification)):
			for j in range(0,len(quantification[i])):
				if sentence.find(quantification[i][j]) != -1:
					sentence2 = '<quantification int=' + str(i+1) +'>' + sentence + '</quantification>'
		if sentence2 != '':
			output += sentence2
			sentence2 = ''
		else:
			output += sentence
	return output

if len(sys.argv) < 2 or filename_end.findall(sys.argv[1]) == []:
    exit("Usage: parser *.txt")

with open(sys.argv[1], 'r',encoding="utf8") as txt_file:
		output = addBalisequantification(txt_file, output)

with open('fichier.txt', 'w',encoding="utf8") as final_file:
    final_file.write(output)

exit(0)
