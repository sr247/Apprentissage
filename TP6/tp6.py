import random


class BernoulliArm:
    def __init__(self, p):
        self.p = p
    def draw(self):
        return 0.0 if random.random() > self.p else 1.0

class EpsilonGreedy:
    # constructor
    # epsilon (float): tradeoff exploration/exploitation
    def __init__(self, epsilon):
        self.epsilon = epsilon

    # re-initialize the algorithm in order to run a new simulation
    # n_arms (int): number of arms
    def initialize(self, n_arms): pass
    # return a index of the chosen decision
        # self.n_arms = n_arms

    def select_arm(self):
    # update knowledge

    # chosen_arm (int): the decision that has been made
        return chosen_arm

# horizon = nombre de tour
def test_algorithm(algo, means, num_sims, horizon):
# init. all decisions
    arms = [BernoulliArm(mu) for mu in means]
    rewards = []

    for sim in range(num_sims):
        algo.initialize(len(arms))
        for t in range(horizon):
            chosen_arm = algo.select_arm()
            reward = arms[chosen_arm].draw()
            algo.update(chosen_arm, reward)
            rewards.append(reward)




# q1
            # pour 100 choix avec une valeur moyenne de v
            # rt = probabilité de choisir
# ri =
# rt =  /t
# pt+1 = pt +

# q2
# q3
# l'interet de la relation précédente est : On a une valeur de moins à stocker.