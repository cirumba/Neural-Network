# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise


def question3a():
    """
    Prefira a saída próxima (+1), arriscando o penhasco (-10).
    """
    answerDiscount = 0.5    
    answerNoise = 0.0       
    answerReward = -1 
    return answerDiscount, answerNoise, answerReward


def question3b():
    """
    Prefira a saída próxima (+1), mas evitando o penhasco (-10).
    """
    answerDiscount = 0.5    
    answerNoise = 0.2       
    answerReward = -1 
    return answerDiscount, answerNoise, answerReward


def question3c():
    """
    Prefira a saída distante (+10), arriscando o penhasco (-10).
    """
    answerDiscount = 0.9    
    answerNoise = 0.0       
    answerReward = -2 
    return answerDiscount, answerNoise, answerReward


def question3d():
    """
    Prefira a saída distante (+10), evitando o penhasco (-10).
    """
    answerDiscount = 0.9    
    answerNoise = 0.2       
    answerReward = -0.5 
    return answerDiscount, answerNoise, answerReward


def question3e():
    """
    Evite as saídas e o penhasco (portanto, um episódio nunca deve terminar).
    """
    answerDiscount = 0.9    
    answerNoise = 0.0       
    answerReward = 10 
    return answerDiscount, answerNoise, answerReward

def question6():
    epsilon = 0.1  
    alpha = 0.5  
    return epsilon, alpha

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
