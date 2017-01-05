# NEW MODIF
#!/usr/local/bin/python
# coding: latin-1
import sys
import re
import numpy as np
import matplotlib.pyplot as plt

fichier = open(sys.argv[1])

def count_ligne(f):
	c = 0
	for line in f:
		c += 1
	print 'Il y a : %d jugements.' % c
	f.seek(0)
	return c
	
def sort_jugement(f):
	
	jugement = []
	for line in f:
		new_field = line.split("|")
		jugement.append(new_field)
		
	# print(jugement)
	f.seek(0)
	return jugement


def count_utilisateur(jugement):

	list_user = []
	for element in jugement:
		if not element[0] in list_user:
			list_user.append(element[0])
			

	print 'Il y a : ' + str(len(list_user)) + ' utilisateurs'
	#print(list_user)
	return	list_user

def count_film(jugement):

	list_film = []
	for element in jugement:
		if not element[1] in list_film:
			list_film.append(element[1])
	
	print 'Il y a : ' + str(len(list_film)) + ' films.'
	#print(list_film)
	old_young_film(list_film)
	return list_film
	
def old_young_film(l):
	list_date = []
	date = []
	reg_date_exp = re.compile(r"\(([0-9])+\)")
	for x in l:
		list_date.append(x.split(" "))
			
	for x in list_date:
		for i in range(len(x)):
			if ("(" in x[i]):
				if  (re.match(reg_date_exp, x[i])):
					date.append(x[i])

	date_inf = date_sup = date[0]
	
	for x in date:
		if x > date_sup:
			date_sup = x
		elif x <= date_inf:
			date_inf = x
		
	print 'Le flim le plus ancien est de : %s' % date_inf
	print 'Le flim le plus recent est de : %s' % date_sup
	return list_date
	
def sort_note(jugement):
	
	list_note = []
	tmp_note = []
	for element in jugement:
		tmp_note.append(element[2][0:str.rfind(element[2],r"\d")])	
	
	list_note = tmp_note
	list_note = [list_note[i].replace(",","") for i in range(len(list_note))]
	
	print 'Il y a : ' + str(len(list_note)) + ' notes'
	print(list_note)
	return list_note
	
def trace_courbe(var): # traiter les jugements
	
	y = []
	print 'Tracer de la courbe des notes...'
	
	x = np.arange(0, int(len(var)))
	y = x
	
	plt.plot(x,y)			
	plt.show()

	
def Analyse(f):

	# Ajouter ici sort_jugement qui extrait les jugements et stock dans jugement
	count_ligne(f)
	jugement = sort_jugement(f)
	count_utilisateur(jugement)
	count_film(jugement)
	note = sort_note(jugement)
	trace_courbe(note)

Analyse(fichier)

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5, .01)
y = np.sin(2*np.pi*x)
plt.plot(x,y)
plt.show()
"""

