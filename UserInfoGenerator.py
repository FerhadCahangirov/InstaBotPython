import random
from bs4 import BeautifulSoup
import requests
from ProxyRouter import ProxyRouter
import string

#https://www.behindthename.com/random/random.php?number=2&sets=1&gender=both&surname=&usage_aze=1

#Bu saytdan reqeust ile istifade ele accunt adlari gotur ve account info generate ele

class Info():

    def __init__(self, gender, country):
        self.gender = gender
        self.country = country
        self.name_list = []
        self.char_list = ['_', '.', '__', '._.' , '', '._', '_.']

    def GetInfo(self):
        with requests.Session() as rs:
            if self.gender == 'male':
                try:
                    url = 'https://www.behindthename.com/names/gender/masculine/usage/{}'.format(self.country)
                    response_info = requests.get(url=url)
                    ParseHtml = BeautifulSoup(response_info.content,'html.parser')

                    print('--------------')
                    print('\n')
                    print(response_info.status_code)
                    #AAAYYYYY BLEEEE Bu GIJDILLAX nie status codu 404 verir

                    scrap_names = ParseHtml.find_all('span', {'class' : 'listname'})

                    for name in scrap_names:
                        self.name_list.append(name.text)

                    
                    
                except Exception as e:
                    print(e) 
            elif self.gender == 'female':
                try:
                    url = 'https://www.behindthename.com/names/gender/feminine/usage/{}'.format(self.country)
                    response_info = requests.get(url=url) 
                    ParseHtml = BeautifulSoup(response_info.content,'html.parser')

                    print('--------------')
                    print('\n')
                    print(response_info.status_code)
                    #AAAYYYYY BLEEEE Bu GIJDILLAX nie status codu 404 verir

                    scrap_names = ParseHtml.find_all('span', {'class' : 'listname'})

                    for name in scrap_names:
                        self.name_list.append(name.text)


                except Exception as e:
                    print(e)


    def GenerateUserInfo(self):

        self.GetInfo()
        
        if self.country == 'azerbaijani':

            self.name = self.name_list[
                    random.randint(0, len(self.name_list) - 1)]
            
            if self.gender == 'male':
                self.surname = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'ov'    
                ])

                surname_v2 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'off'    
                ])

                surname_v3 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'ovv'    
                ])

                surname_v4 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'oov'    
                ])

                surname_v5 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'o0v'    
                ])

                surname_v6 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    '0ov'    
                ])

                surname_v7 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    '0v'    
                ])

                self.surname_list = [self.surname, surname_v2, surname_v3, surname_v4, surname_v5, surname_v6, surname_v7]

                self.full_name = ''.join([self.name, self.surname])
            
            elif self.gender == 'female':
                self.surname = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'ova'    
                ])

                surname_v2 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'offa'    
                ])

                surname_v3 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'ovva'    
                ])

                surname_v4 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'oova'    
                ])

                surname_v5 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'ovaa'    
                ])

                surname_v5 = ''.join([self.name_list[
                    random.randint(0, len(self.name_list) - 1)],
                    'oovvaaa'    
                ])

                self.surname_list = [self.surname, surname_v2, surname_v3, surname_v4, surname_v5]

                self.full_name = ''.join([self.name, self.surname])

            #Skim blet beynim yandi e bunu men nece versiyada cixardm

            #Name-2121

            username_v1 = self.char_list[
                random.randint(0, len(self.char_list) - 1)
            ].join ([
                self.name, 
                str([random.randint(0, 9) for i in range(random.randint(1, 4))])[1:-1].replace(',', '').replace(' ', '')
            ])
            
            #212-Name

            username_v2 = self.char_list[
                random.randint(0, len(self.char_list) - 1)
            ].join([
                str([random.randint(0, 9) for i in range(random.randint(1, 4))])[1:-1].replace(',', '').replace(' ', ''),
                self.name
            ])
            
            #Surname-211
            username_v3 = self.char_list[
                random.randint(0, len(self.char_list) - 1)
                ].join([
                    str([random.randint(0, 9) for i in range(random.randint(1, 4))])[1:-1].replace(',', '').replace(' ', ''),
                    self.surname_list[random.randint(0, len(self.surname_list) - 1)]
                ])
            
            #212-Surname
            username_v4 = self.char_list[
                random.randint(0, len(self.char_list) - 1)
            ].join([
                self.surname_list[random.randint(0, len(self.surname_list) - 1)],
                str([random.randint(0, 9) for i in range(random.randint(1, 4))])[1:-1].replace(',', '').replace(' ', '')
            ])

            username_list = [username_v1, username_v2, username_v3, username_v4]
            username = username_list[random.randint(0, len(username_list) - 1)]

            #Generate Passwd

            length = 10
            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            num = string.digits
            symbols = string.punctuation

            all = lower + upper + num + symbols

            temp = random.sample(all,length)
            password = "".join(temp)

            return self.full_name, username, password

if __name__ == '__main__':

    for i in range(20):
        print(Info('female', 'azerbaijani').GenerateUserInfo()) 
        print('-----------')
        print(Info('male', 'azerbaijani').GenerateUserInfo()) 