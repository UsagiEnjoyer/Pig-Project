import random

def roll():
    return random.randint(1,6)

def holdAt20Turn():
    turnTotal = 0
    pig = False
    while turnTotal < 20 and not pig:
        side = roll()
        print("Roll:", side)
        if side == 1:
            turnTotal = 0
            pig = True
        else:
            turnTotal += side
    print("Turn Total:", turnTotal)
    return turnTotal

"""
def holdAtXTurn(target = 20):
    turnTotal = 0
    pig = False
    while turnTotal < target and not pig:
        side = roll()
        #print("Roll:", side)
        if side == 1:
            turnTotal = 0
            pig = True
        else:
            turnTotal += side
    #print("Turn Total:", turnTotal)
    return turnTotal
holdAtXTurn()
def holdAtXTurn(target = 20, score = 0):
    turnTotal = 0
    pig = False
    while turnTotal < target and not pig and score + turnTotal < 100:
        side = roll()
        #print("Roll:",side)
        if side == 1:
            turnTotal = 0
            pig = True 
        else:
            turnTotal += side
    #print("Turn Total:", turnTotal)
    return turnTotal
def holdAt20Outcome(trials):
    result = {}
    results[0] = 0
    #initialize possible scores

    for score in range(20,26):
        results[score] = 0

    # simulate the  turn "trials" times    
    for _ in range(trials):
        outcome = holdAt20Turn()
        results[outcome] += 1
    #print those possibilities
    print("score" + "\t" + results[score]/trials)
    for score in results:
        print(score + "\t" + results[score]/trials)

def holdAtXOutcome(trials, target = 20):
    results = {}
    results[0] = 0
    # initialize possible scores
    for score in range(target,target+6):
        results[score] = 0 
    
    # simulate the turn "trials" times
    for _ in range(trials):
        outcome =  holdAtXTurn(target)
        results[outcome] += 1
    
    # print those probabilities
    print("Score","\t","Estimated Prob.")

    for score in results:
        print(score,"\t",results[score]/trials)
trials = 100_000
#trials = int(input("How many Hold-at-20 turn stuff?\n"))   # edit this later also
holdAtXOutcome(trials, 100)

"""


#Second half


def holdAt20orGoal():
    complete_turnTotal = 0
    TotalTurnsTaken = 0
    while complete_turnTotal < 100:
        turnTotal = holdAt20Turn()
        complete_turnTotal += turnTotal
        print("\tTurn total:", turnTotal) 
        print("Complete Total:", complete_turnTotal)
        TotalTurnsTaken += 1
    return TotalTurnsTaken


holdAt20orGoal()

# def avgPigTurns():
#     sim = int(input("Games?:"))
#     simsRan = 0
#     completeturnstaken = 0 #for Avg calculate

#     while simsRan < sim:
#         simsRan += 1
#         completeturnstaken += holdAt20orGoal()
#     avgTurns = completeturnstaken / sim 

#     print("Average Turns:" + "\n", str(avgTurns) + "\n", "Games:" + "\n", str(sim) + "\n")

#     return 
# avgPigTurns()

def TwoPlayerPig():
    player1 = 
    player1_score = 
    player2 = 
    player2_count = 

    return
TwoPlayerPig()

def Pig_Game():
    return
