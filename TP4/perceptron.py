# -*- encoding: utf-8 -*-
import numpy as np
n = 10 ** 6
data = 10 ** 9 + np.random.uniform(0,1,n)

def moyenne(d, size):
    tmp = 0.0

    for i in d:
        tmp+= i

    return tmp/size

def variance(d, size, moy):
    tmp = 0.0

    for i in d:
        tmp+= (i - moy) ** 2

    return tmp/size

def welford(d, moy, var, size):
    i = 0
    while i < size:
        el = d[i]
        i += 1
        m = moy + (el - moy) / i
        v = var + (el - moy) * (el - m)
        moy = m
        var = v
    return moy, (var / size)



test = [15,15,15]
moy, var = welford(data, 0, 0, n)
print(moy)
print(var)
# y = moyenne(test,len(test))
x = moyenne(data,n)


#variance(test,len(test),y)
print(variance(data, n, x))


def data_reader(filename):
    to_binary = {"?": 3, "y": 2, "n": 1}
    labels = {"democrat": 1, "republican": -1}

    data = []
    for line in open(filename, "r"):
        line = line.strip()

        label = int(labels[line.split(",")[0]])
        observation = np.array([to_binary[obs] for obs in line.split(",")[1:]] + [1])
        data.append((label, observation))

    return data


def spam_reader(filename):
    to_binary = {1: 1, 0: -1}
    data = []
    for line in open(filename, "r"):
        line = line.strip()
        label = to_binary[int(line.split(",")[-1])]
        observation = [float(obs) for obs in line.split(",")[:-1] + [1.0]]

        data.append((label, np.array(observation)))

    return data

def classify(obs):
    etiquette, vec = obs
    return etiquette

def test(corpus,vec):




data = data_reader("house-votes-84.txt")
print(data)
np.random.shuffle(data)
print(data)
