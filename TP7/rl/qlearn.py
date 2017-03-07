
# coding=utf-8
import random

class QLearn:
    def __init__(self, actions, epsilon=0.1, alpha=0.2, gamma=0.9):
        self.q = {} # dictionnaire : état,action -> reward

        self.epsilon = epsilon # paramètre pour espilon-greedy
        self.alpha = alpha # poids des actions nouvelles
        self.gamma = gamma # paramètre pour la propagation des gains
        self.actions = actions # possibles actions (8 mvts)
    
        
    def chooseAction(self, state):		
		if random.random() < epsilon:
			return random.randrange(8)
		else :			
			maxReward = reward, q[state,0]
			for a in actions:
				maxReward = max(meilleur_reward, q[state,a])
				
		return q.hasValue(meilleur_reward)
		
	def learnbAI(self, lastState, lastAction, state, reward):
		
		# On recalcule comme pour chooseAction, la valeur du 
		self.q[lastState, lastAction] = q[lastState, lastAction] + alpha * (reward + max(q[state,newReward]) - q[lastState, lastAction]);
