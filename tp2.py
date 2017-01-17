#! /usr/bin/python2.7
# coding: utf-8



import pickle
import gzip
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
with gzip.open('mnist.pkl.gz', 'rb') as ifile :
train_set, valid_set, test_set = pickle.load(ifile, encoding=''latin-1'')


im = train_set[0][0].reshape(28,28)
plt.imshow(im, plt.cm.gray)
plt.show()

def bin_img(imgMat, threshold):
  """
  Faire une fonction qui récupère l'image sous forme de matrice avec des valeurs comprises  entre 0 et 1
  Et pour toute case où si contenu > thesrhold alors contenu = 1
                        Sinon contenu = 0
  Initialisé un tableau a 0 peut réduire le nombre d'affectation
  """


def histo_img():
  """
  Ici on fait un array de 28 cases qui compte combien de 1 il y à par lignes i.e les endroits ou est tracé le chiffre sur la bitmap
  """
def affichage():
  for i in range(len(histogramme)-1):
    plot.barh(i,histogramme[i])
  plt.show()
