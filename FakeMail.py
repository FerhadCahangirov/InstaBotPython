from bs4 import BeautifulSoup
import requests
import time

class FakeMail():

    global email, soup, s
    s = requests.Session()

    url = s.get('https://10minutemail.net/')
    soup = BeautifulSoup(url.content, "html.parser")

    soup_mail = soup.find_all('input', {'class': 'mailtext'})

    email = soup_mail[0]['value']

    def GetMail():
        return email

    def VertificationCode():
        
        successful_return = 0

        while successful_return == 0:
            
            url = s.get('https://10minutemail.net/')
            soup = BeautifulSoup(url.content, "html.parser")

            soup_inbox_subject = soup.find_all('a', {'class': 'row-link'})[1].text


            print('Checking for confirmation code...')
            time.sleep(20)

            
            if soup_inbox_subject == "Hi, Welcome to 10 Minute Mail":

                time.sleep(5)
                print("No new email :(")

            else:
                
                print("New email !")

                for i in range(0, len(soup_inbox_subject)):
                    if soup_inbox_subject[i] == ' ':
                        soup_inbox_subject = soup_inbox_subject[0:i]
                        break


                print(soup_inbox_subject)

                successful_return = 1

        return soup_inbox_subject


