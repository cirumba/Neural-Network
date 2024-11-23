# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues - feito
        - computeActionFromQValues - feito
        - getQValue - feito
        - getAction - feito
        - update - feito
        5/5

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        self.qValues = util.Counter()

    def getQValue(self, state, action):
        return self.qValues[(state, action)]


    def computeValueFromQValues(self, state):
        legal_actions = self.getLegalActions(state)
        if not legal_actions:
          return 0.0  
        return max(self.getQValue(state, action) for action in legal_actions)

    def computeActionFromQValues(self, state):
        legal_actions = self.getLegalActions(state)
        if not legal_actions:
            return None

        max_value = self.computeValueFromQValues(state)
        best_action = [
            action for action in legal_actions
            if self.getQValue(state, action) == max_value
        ]

        return random.choice(best_action)

    def getAction(self, state):
        legal_actions = self.getLegalActions(state)
        if not legal_actions:
            return None

        if util.flipCoin(self.epsilon):
            return random.choice(legal_actions)  
        else:
            return self.computeActionFromQValues(state)  

    def update(self, state, action, nextState, reward):
        sample = reward + self.discount * self.computeValueFromQValues(nextState)
        self.qValues[(state, action)] = (
            (1 - self.alpha) * self.qValues[(state, action)] + self.alpha * sample)

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        features = self.featExtractor.getFeatures(state, action)
        return sum(self.weights[feature] * value for feature, value in features.items())

    def update(self, state, action, nextState, reward):
        features = self.featExtractor.getFeatures(state, action)
        q_value = self.getQValue(state, action)
        max_next_q = 0.0 if not self.getLegalActions(nextState) else max(
            self.getQValue(nextState, next_action) for next_action in self.getLegalActions(nextState))
        td_error = reward + self.discount * max_next_q - q_value

        for feature, value in features.items():
            self.weights[feature] += self.alpha * td_error * value

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        if self.episodesSoFar == self.numTraining:
            print("Treinamento concluído. Pesos finais:")
            print(self.weights)
