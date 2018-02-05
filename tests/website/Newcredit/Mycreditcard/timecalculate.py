import datetime
import re

#startDate format '2018-08-08'
def calculateDelta(startDate):
    try:
        a = datetime.datetime.strptime(startDate, "%Y-%m-%d")
        c = datetime.datetime.now()
        #print(c)
        text = str(c-a)
        #print(text)
        reg ='(.*?) days,'
        days = int(re.findall(reg,text)[0])
        return days
    except:
        print('wrong startDate')
        return None

#print(calculateDelta('2019-0909'))
if __name__ == '__main__':
    calculateDelta()