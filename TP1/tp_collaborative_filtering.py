# -*- coding: utf-8 -*-

###############################################################################
# Nicolas Pecheux <nicolas.pecheux@limsi.fr>
# Wednesday, 09 January 2013
# LIMSI-CNRS
###############################################################################

"""Collaborative filter assignment, M1-RDF course 2013. See pdf instructions.

Notes
-----
CVS file is not checked, suppose to be well formated and duplicates are not
taken into account.

"""

from __future__ import division, print_function

import re
import codecs
import time

import collections

import numpy as np
import pylab as pl


def load_data(filepath):
    """Load data in a (redundant) users and movies dictionnaries.

    Return
    ------
    users : dict of (str, int)
        Map author to a dictionnary of movie to rate
    movies : dict of dict of int
        Map movie to a dictionnary of author to rate
    """

    users = collections.defaultdict(dict)
    movies = collections.defaultdict(dict)
    with codecs.open(filepath, encoding="utf-8") as file_:
        for line in file_:
            aut, mov, rate = line.strip().split("|")
            aut, rate = int(aut), int(rate)
            users[aut][mov] = rate
            movies[mov][aut] = rate

    return users, movies


def basic_analysis(users, movies):
    """Print to standart output basic statistics about corpora."""
    print("Il y a {:,} utilisateurs".format(len(users)))

    rates = [r for a2r in movies.values() for r in a2r.values()]
    print("Il y a {:,} jugements".format(len(rates)))
    print("Il y a {:,} films".format(len(movies)))

    date_regexp = re.compile("\((\d\d\d\d)\)$")
    dates = (date_regexp.search(
        m).group(1) for m in movies if date_regexp.search(m))
    dates = [int(d) for d in dates if d is not None]

    print("Le plus vieux date de {}, le plus récent de {}.".format(
        min(dates), max(dates)))
    pl.hist(rates, bins=5, range=(0.5, 5.5))
    pl.xlabel("Note")
    pl.ylabel("n. occurences")
    pl.title("Distribution des notes")
    pl.show()
    users_rate_nb = [len(mov) for mov in users.itervalues()]
    print("Il y a en moyenne {:.2f} (±{:.2f}) jugements par utilisateur, au plus {}"
          " et au moins {}.".format(np.mean(users_rate_nb),
                                    np.std(users_rate_nb),
                                    max(users_rate_nb),
                                    min(users_rate_nb)))


def cov(v1, v2):
    """Return (unbiased) covariance of list (vectors) v1 and v2."""
    mean1 = sum(v1) / len(v1)
    mean2 = sum(v2) / len(v2)
    return sum([(e1 - mean1) * (e2 - mean2) for e1, e2 in zip(v1, v2)]) / (len(v1) - 1)


def corr(v1, v2):
    """Return correlation between v1 and v2."""
    try:
        res = cov(v1, v2) / np.sqrt(cov(v1, v1) * cov(v2, v2))
        res = (1 + res) / 2  # so that similarity is between 0 and 1
        return res
    except ZeroDivisionError:
        return 0.0


def similarity(mov1, mov2):

    mov1_users = movies[mov1]
    mov2_users = movies[mov2]

    common_users = set(mov1_users.keys())
    common_users.update(mov2_users.keys())

    rates_vect1 = [mov1_users.get(u, 0) for u in common_users]
    rates_vect2 = [mov2_users.get(u, 0) for u in common_users]

    return corr(rates_vect1, rates_vect2)


def compute_similarities(mov, movies):
    """Return all similarities betwen `mov` and a movie"""
    mov1 = mov
    res = {}
    for mov2 in movies:
        res[mov2] = similarity(mov1, mov2)
    return res


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--file', help="Mouvie Lens csv file",
                        required=True)
    args = parser.parse_args()

    users, movies = load_data(args.file)

    basic_analysis(users, movies)

    mov1 = "Demolition Man (1993)"
    mov2 = "Stargate (1994)"
    print("Similarity betwenn '{}' and '{}' is {:.3f}".format(mov1, mov2,
                                                              similarity(mov1, mov2)))

    start = time.time()
    sim1 = compute_similarities(mov2, movies)
    end = time.time()
    print("Computing all similarities for '{}' took {:.2}s".format(mov2,
                                                                   end - start))
