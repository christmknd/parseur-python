#GHLAMALLAH Aïmane 14503215


import os
import re
import sys

lcount = 0

def syllable_count(word):
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
            if word.endswith("e"):
                count -= 1
    if count == 0:
        count += 1
    return count
def parse(in_f,out_f):

	out_f.write('<?xml version = "1.0" encoding="UTF-8" standalone="yes" ?>\n')

	out_f.write('<text>\n')
	
	for line in in_f:
		if syllable_count(line)==17:
			out_f.write("<haiku>"+line+"</haiku>")
			
		for word in re.findall(r'[\w.,;:?!"\'\n\b@-_]+', line):

			if re.search(r'\bi\b|\bme\b|\byou\b|\bhe\b|\bshe\b|\bher\b|\bhim\b|\bit\b|\bwe\b|\bus\b|\bthey\b|\bthem\b', word, re.I):
				out_f.write("<pronoun>"+word+"</pronoun>")

			elif re.search(r'\bmy\b|\byour\b|\bits\b|\bour\b|\byour\b|\btheir\b|\bhis\b', word, re.I):
				out_f.write("<poss_pronoun>"+word+"</poss_pronoun>")

			elif re.search(r'\babide\b|\barise\b|\bawake\b|\bbe\b|\bbeat\b|\bbecome\b|\bbeget\b', word, re.I):
				out_f.write("<verb_inf>"+word+"</verb_inf>")

			elif re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', word, re.I):
				out_f.write("<mail>"+word+"</mail>")

			elif re.search(r'www|http', word, re.I):
				out_f.write("<url>"+word+"</url>")

			elif re.search(r'\b[01]+B\b', word, re.I):
				out_f.write("<binary>"+word+"</binary>")

			elif re.search('/[.]',word,re.I):
				out_f.write("<command>"+word+"</command>")
			elif re.search(r'^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$', word, re.I):
				out_f.write("<phone>"+word+"</phone>")


			else:
				out_f.write(word+" ")

	out_f.write('\n')
	out_f.write('</text>')






def main():
	
	
	input_file = open(sys.argv[1],'r')
	output_file= open('output'+'.xml',"w+")
	#dic = pyphen.Pyphen(lang='en')
	#print(dic.wrap(text,len(text)))
	#print (dic.inserted(text))
	parse(input_file,output_file)
    


				

if __name__ == '__main__':
	main()