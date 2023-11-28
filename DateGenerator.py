import random

class Date():

    def __init__(self):
        self.monthes = ['December' ,'January', 'February',
                      'March', 'April', 'May', 
                      'June', 'July', 'August', 
                      'September', 'October', 'November']
        self.years = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003]

    def GenerateDate(self):
        
        day = random.randint(0, 28)
        month = self.monthes[random.randint(0, len(self.monthes) - 1)]
        year = self.years[random.randint(0, len(self.years) - 1)]

        return int(day), str(month), int(year) 

#Peyseri yoxlamaqcun
if __name__ == '__main__':
    i = 0
    while i<10:
        print('------')
        print(Date().GenerateDate())
        print('------')
        i += 1
