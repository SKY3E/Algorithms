import random
import matplotlib.pyplot as plt
from faker import Faker
fake = Faker()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def ReturnInfo(self):
        return self.name, self.age

def CreateRandomPeople(times):
    people = []
    for i in range(times):
        person = Person(fake.name(), random.randint(1, 99))
        people.append(person)

    namesArr = []
    ageArr = []

    for person in people:
        namesArr.append(person.name)
        ageArr.append(person.age)

    return namesArr, ageArr

def SortPeople(namesArr, ageArr):
    for i in range(len(ageArr)):
        for j in range(len(ageArr)):
            if ageArr[i] < ageArr[j]:
                temp = ageArr[i]
                ageArr[i] = ageArr[j]
                ageArr[j] = temp

                temp = namesArr[i]
                namesArr[i] = namesArr[j]
                namesArr[j] = temp

    return namesArr, ageArr

def PlotArrays(names, ages):
    plt.bar(names, ages)
    plt.xlabel('Names')
    plt.ylabel('Ages')
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    plt.title('Names and Ages')
    plt.show()

namesArr, ageArr = CreateRandomPeople(10)
PlotArrays(namesArr, ageArr)
sortedNamesArr, sortedAgeArr = SortPeople(namesArr, ageArr)
PlotArrays(sortedNamesArr, sortedAgeArr)
