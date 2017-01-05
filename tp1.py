# NEW MODIF
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
def sort_jugement(f)
	jugement = []    
	return jugement 
# Remplacer fichier par jugement (dont une fonction l'aura extraite au préalable de fichier et stocker dans dico)	
def count_utilisateur(f): 
	c = 0
	list_user = []	
	for line in f:		
		jugement = line.split("|")		
		if not jugement[0] in list_user:
			list_user.append(jugement[0])
	
	print 'Il y a : ' + str(len(list_user)) + ' utilisateurs'
	f.seek(0)
	return	list_user

# Remplacer fichier par jugement (dont une fonction l'aura extraite au préalable de fichier et stocker dans dico)		
def count_film(f):
	c = 0
	jugement = []
	list_film = []	
	for line in f:		
		jugement = line.split("|")		
		if not jugement[1] in list_film:
			list_film.append(jugement[1])
	
	print 'Il y a : ' + str(len(list_film)) + ' films.'
	old_young_film(list_film)
	f.seek(0)
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
	
def count_note(f)
	
def trace_courbe(jugement): # traiter les jugements

	x = np.arange(-5, 5, .01)
	y = np.sin(2*np.pi*x)
	plt.plot(x,y)
	plt.show()

	
def Analyse(f):

	jugement = []
	# Ajouter ici sort_jugement qui extrait les jugements et stock dans jugement
	count_ligne(f)
	count_utilisateur(f)
	count_film(f)
	trace_courbe(jugement)

# count_ligne(f2)		
# count_ligne(f3)

# count_film(f1)
# count_film(f3)
# count_film(f1)

Analyse(fichier)

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5, .01)
y = np.sin(2*np.pi*x)
plt.plot(x,y)
plt.show()
"""

