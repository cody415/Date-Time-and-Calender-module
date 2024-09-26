import random
import time

def getRandomDate(StartDate, EndDate):
    print("printing random date between",StartDate,"and", EndDate)
    randomGenerator=random.random()
    dateFormat="%m/%d/%Y"

    startTime=time.mktime(time.strptime(StartDate, dateFormat))
    endTime=time.mktime(time.strptime(EndDate,dateFormat))

    randomTime= startTime + randomGenerator*(endTime-startTime)
    randomDate=time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date=", getRandomDate("1/1/2022","12/12/2024"))