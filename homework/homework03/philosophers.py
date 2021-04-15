philosophers = {
    0: {"Lfork": 0, "Rfork": 4, "eating": False},
    1: {"Lfork": 1, "Rfork": 0, "eating": False},
    2: {"Lfork": 2, "Rfork": 1, "eating": False},
    3: {"Lfork": 3, "Rfork": 2, "eating": False},
    4: {"Lfork": 4, "Rfork": 3, "eating": False},
}

forks = {
    0: "False",
    1: "False",
    2: "False",
    3: "False",
    4: "False",
}


# Uses Dijkstra's resource hierarchy algorithm to determine who is eating: 
# all but one philosopher grabs their left fork, leaving 1 fork on a philosopher's right resulting in that philosopher eating
# @param philoNoEat the index of the philosopher who will not grab a fork 
def eat(philoNoEat):
    for philo in philosophers:
        if philo == philoNoEat:
            unusedFork = philosophers[philo]["Lfork"]
            forks[unusedFork] = False
        else:
            forks[philosophers[philo]["Lfork"]] = True
    for philo in philosophers:
        if philosophers[philo]["Rfork"] == unusedFork:
            forks[philosophers[philo]["Rfork"]] = True
            philosophers[philo]["eating"] = True
            break
    whoEatin()
    forksDown()
            

        
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
            

# extra function that allows you to choose which philosopher you want to feed with index 0-4
def feed(philosopher):
    if philosopher == 0:
        eat(4)
    elif philosopher == 1:
        eat(0)
    elif philosopher == 2:
        eat(1)
    elif philosopher == 3:
        eat(2)
    elif philosopher == 4:
        eat(3)
    else:
        raise ValueError('Non-existant philosophers cannot be feed, expected a value 0-4')


# for rounds in range(5):
#     print("")
#     print("-----------ROUND {}-----------".format(rounds+1))
#     for munch in range(5):
#         print("------MUNCH ROUND {}------".format(munch+1))
#         eat(munch)
    
# feed(0)
# feed(1)
# feed(2)
# feed(3)
# feed(4)