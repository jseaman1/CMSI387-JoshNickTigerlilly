import random

philosophers = {
    0: {"Lfork": 0, "Rfork": 4, "eating": False, "waiting": False, "waitTime": 0},
    1: {"Lfork": 1, "Rfork": 0, "eating": False, "waiting": False, "waitTime": 0},
    2: {"Lfork": 2, "Rfork": 1, "eating": False, "waiting": False, "waitTime": 0},
    3: {"Lfork": 3, "Rfork": 2, "eating": False, "waiting": False, "waitTime": 0},
    4: {"Lfork": 4, "Rfork": 3, "eating": False, "waiting": False, "waitTime": 0},
}
#locking/releasing (thinking vs eating)
#spawn 5 threads (philos) 3 states: hungry, eating, thinking

forks = {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
}


# Uses Dijkstra's resource hierarchy algorithm to determine who is eating: 
# all but one philosopher grabs their left fork, leaving 1 fork on a philosopher's right resulting in that philosopher eating
# @param philoNoEat - the index of the philosopher who will not grab a fork 
def eat(philoNoEat):
    for philo in philosophers:
        if philo == philoNoEat:
            unusedFork = philosophers[philo]["Lfork"]
            forks[unusedFork] = False
        else:
            forks[philosophers[philo]["Lfork"]] = True
    for philo in philosophers:
        if philosophers[philo]["Rfork"] == unusedFork & philosophers[philo]["waiting"] == False:
            forks[philosophers[philo]["Rfork"]] = True
            philosophers[philo]["eating"] = True
            break
    whoEatin()
    forksDown()
    decrementWaitTime()

            
            
def decrementWaitTime():
    for philo in philosophers:
        if philosophers[philo]["waiting"] == True & philosophers[philo]["waitTime"] > 1:
            philosophers[philo]["waitTime"] = philosophers[philo]["waitTime"] - 1
            print("Philosopher {} is now waiting {} seconds".format(philo, philosophers[philo]["waitTime"]))
        elif philosophers[philo]["waiting"] == True & philosophers[philo]["waitTime"] == 0:
            philosophers[philo]["waiting"] == False
            print("Philosopher {} is no longer waiting".format(philo))
        
# outputs who is currently eating
def whoEatin():
    for philo in philosophers:
        if philosophers[philo]["eating"] == True:
            print('Philosopher {} is eating'.format(philo))

# all philosophers currently holding a fork(s) places then down and eating status is changed to false
def forksDown():
    for fork in forks:
        forks[fork] = False;
    for philo in philosophers:
        philosophers[philo]["eating"] = False;   
            

def initializePhilos():
    for i in range(5):
        if random.randrange(0, 3, 1) != 1:
            philosophers[i]["waiting"] = True
            philosophers[i]["waitTime"] = random.randrange(0, 5, 1)
    for i in range(5):
        if philosophers[i]["waiting"] == True:
            print("Philosopher {} is currently waiting {} seconds".format(i, philosophers[i]["waitTime"]))
        else:
            print("Philosopher {} is not waiting".format(i))

def resetWaitTimes():
    for i in range(5):
        philosophers[i]["waiting"] = False
        philosophers[i]["waitTime"] = 0

for round in range(5):
    print("-----Round {}-----".format(round))
    initializePhilos()
    for munch in range(5):
        eat(munch)


# for rounds in range(5):
#     initializePhilos()
#     print("")
#     print("-----------ROUND {}-----------".format(rounds+1))
#     for munch in range(5):
#         eat(munch)
#     resetWaitTimes()
    
