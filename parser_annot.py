
# coding: utf-8
#
#             1ER PARTIE :
# récupérer
#
# ===>Fusion_Animal_Hum_Corpus_v3_annotation_FR_utf8.txt
#
# changer le fichier si besoin, ou ajouter à la main d'autre mots dans les listes
#
#
#             2E PARTIE
#
#
# le fichier à parser, ===> Fusion_Animal_Hum_Corpus_v3_FR_utf8.txt ou les_misérable.txt
#
# ---le changer pour parser un autre texte.
#
# mise en place des balises: phrase, Satisfaction, Dissatisfaction, Agreement, Disagreement.
#
#
#             3E PARTIE
#
# générer 4 fichier .csv contenant les mots qui on été balisé
#
#
#
# Prévoir environ 1 minute au lancement des cellule les plus longues

#             1ER PARTIE

# In[65]:


import string
import re


# In[67]:


#ouvrir le fichier annotation pour recuperer les mots dans les balises sentiments

file = open("Corpus_v4_annotation_FR_utf8.txt",encoding="UTF-8")
chaine=file.read()



# In[68]:


#recuperation des mots Disssatisfaction dans la variable list Dissatisfaction

a = re.findall('<Dissatisfaction int=[0-9]>(.*?)</Dissatisfaction>', chaine)
Dissatisfaction=list(set(a))


# In[69]:


#recuperation des mots Satisfaction dans la variable list Satisfaction


b = re.findall('<Satisfaction int=[0-9]>(.*?)</Satisfaction>', chaine)
Satisfaction=list(set(b))


# In[70]:


#recuperation des mots Disagreement dans la variable list Disagreement

c = re.findall('<Disagreement int=[0-9]>(.*?)</Disagreement>', chaine)
Disagreement=list(set(c))


# In[71]:


#recuperation des mots Agreement dans la variable list Agreement

d = re.findall('<Agreement int=[0-9]>(.*?)</Agreement>', chaine)
Agreement=list(set(d))


#             2E PARTIE

# In[72]:


# ouvrir le fichier à parser

file = open("Corpus_normal.txt",encoding="UTF-8")

fichier=file.read()




# In[73]:


#traitement du fichier pour faciliter le parsing

fichier1 = re.sub(r'[A-Z](\.)', "", fichier)
fichier2=re.sub('\n',' ',fichier1)
#b=re.sub(r'\.',r'.\n',txt)
fichier3=re.sub('\\. ','.\n',fichier2)
fichier4=re.sub(r'\\!',r'!\n',fichier3)
fichier5=re.sub(r'\\:',r':\n',fichier4)
fichier6=re.sub(r'\\?',r'?\n',fichier5)
txt=re.sub('   ','\n\n\n',fichier6)


# In[74]:


#separartion des phrase, mise en place des balises phrase

find_ponctuation= re.compile('\\.\n|\\:\n|\\?\n|\\!\n')
remplace_ponctuation=find_ponctuation.split(txt)
texte=""
for i in remplace_ponctuation[:]:
	if len(i) > 0 :
		texte=texte+"<phrase> "+i+" .</phrase>%%%"+"\n"


aff=re.compile("%%%")



# In[75]:


#mise en place des balise de sentiments

affiche=""
affiche=aff.split(texte)

foo=0
while foo<len(Satisfaction):
    for i in range(0,len(affiche),1):
        index = affiche[i].find(" "+Satisfaction[foo]+" ")

        if(affiche[i].find(" "+Satisfaction[foo]+" ") != -1):

            affiche[i]=affiche[i][:index]+" <Satisfaction>"+affiche[i][index:]
            longueur=len(Satisfaction[foo])
            affiche[i]= affiche[i][:index+17+longueur]+"</Satisfaction> "+affiche[i][index+17+longueur:]

    foo=foo+1



bar=0
while bar<len(Dissatisfaction):
    for i in range(0,len(affiche),1):
        index = affiche[i].find(" "+Dissatisfaction[bar]+" ")

        if(affiche[i].find(" "+Dissatisfaction[bar]+" ") != -1):

            affiche[i]=affiche[i][:index]+" <Dissatisfaction>"+affiche[i][index:]
            longueur=len(Dissatisfaction[bar])
            affiche[i]= affiche[i][:index+20+longueur]+"</Dissatisfaction> "+affiche[i][index+20+longueur:]

    bar=bar+1




boo=0
while boo<len(Agreement):
    for i in range(0,len(affiche),1):
        index = affiche[i].find(" "+Agreement[boo]+" ")

        if(affiche[i].find(" "+Agreement[boo]+" ") != -1):

            affiche[i]=affiche[i][:index]+" <Agreement>"+affiche[i][index:]
            longueur=len(Agreement[boo])
            affiche[i]= affiche[i][:index+14+longueur]+"</Agreement>"+affiche[i][index+14+longueur:]

    boo=boo+1






far=0
while far<len(Disagreement):
    for i in range(0,len(affiche),1):
        index = affiche[i].find(" "+Disagreement[far]+" ")

        if(affiche[i].find(" "+Disagreement[far]+" ") != -1):

            affiche[i]=affiche[i][:index]+" <Disagreement>"+affiche[i][index:]
            longueur=len(Disagreement[far])
            affiche[i]= affiche[i][:index+16+longueur]+" </Disagreement>"+affiche[i][index+16+longueur:]

    far=far+1


with open('parseur.xml', encoding="UTF-8") as f:
    for item in affiche:
        f.write("%s" % item)


#               3E PARTIE

# In[81]:


file = open("parseur.xml",encoding="UTF-8")
chaine=file.read()


# In[82]:


a = re.findall('<Dissatisfaction>(.*?)</Dissatisfaction>', chaine)
ma_liste1=list(set(a))


with open('Dissatisfaction.csv', 'w') as f:
    for item in ma_liste1:
        f.write("%s \n" % item)


# In[83]:


#recuperation des mots Satisfaction dans la variable list Satisfaction


b = re.findall('<Satisfaction>(.*?)</Satisfaction>', chaine)
ma_liste2=list(set(b))


with open('Satisfaction.csv', 'w') as k:
    for item in ma_liste2:
        k.write("%s \n" % item)


# In[84]:


#recuperation des mots Disagreement dans la variable list Disagreement

c = re.findall('<Disagreement>(.*?)</Disagreement>', chaine)
ma_liste3=list(set(c))

with open('Disagreement.csv', 'w') as x:
    for item in ma_liste3:
        x.write("%s \n" % item)


# In[85]:


#recuperation des mots Agreement dans la variable list Agreement

d = re.findall('<Agreement>(.*?)</Agreement>', chaine)
ma_liste4=list(set(d))


with open('Agreement.csv', 'w') as w:
    for item in ma_liste4:
        w.write("%s \n" % item)
