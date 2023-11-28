from typing import Counter
from bs4 import BeautifulSoup
import requests
from FakeMail import FakeMail
from fake_useragent import UserAgent
from datetime import datetime
import re
import sys
from UserInfoGenerator import Info
from DateGenerator import Date
from ProxyRouter import ProxyRouter

class Auth():

    def __init__(self, fmail, uname, fname, passwd, day, month, year, proxy):
        self.uname = uname
        self.fname = fname
        self.passwd = passwd
        self.day = day
        self.month = month
        self.year = year
        self.proxy = proxy
        self.fmail = fmail

    def create_payload(self):

        time = int(datetime.now().timestamp())

        payload = {
            'email': self.fmail,
            'username': self.uname,
            'first_name:': self.fname,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{self.passwd}', 
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        date_payload = {
            'day': self.day,
            'month': self.month,
            'year': self.year
        }

        send_vertification_data = {
            'device_id': 'Yh4XGQAEAAGsqDLUWFSJQ_d9CNbg',
            'email': self.fmail
        }

        if 'http' in self.proxy.lower():
            proxy_data = {
                'http': self.proxy
            }
        elif 'https' in self.proxy.lower():
            proxy_data = {
                'https': self.proxy
            }

        return payload, date_payload, send_vertification_data, proxy_data

    def create_account(self):

        #Gotun Catir Bu Accountu Yaratmada

        link = 'https://www.instagram.com/accounts/emailsignup/'
        signup_url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        date_url = 'https://www.instagram.com/web/consent/check_age_eligibility/'

        payload, date_payload, send_vertification_data, proxy_data = self.create_payload()
        
        with requests.Session() as s:
            try:
                s.proxies.update(proxy_data)
                user_agent = UserAgent().random
                r = s.get(link)
                csrf = re.findall(r"csrf_token\":\"(.*?)\"",r.text)[0]
                
                r = s.post(signup_url,data=payload,headers={
                    "user-agent": user_agent,
                    "x-requested-with": "XMLHttpRequest",
                    "referer": "https://www.instagram.com",
                    "x-csrftoken":csrf
                })
                print('---------------------------')
                print('\n')
                print(r.status_code)
                print(r.url)
                print(r.text)
                print('---------------------------')
                print('\n')

                check_response = '"dryrun_passed":true'

                if check_response in r.text and str(r.status_code) == '200':
                    #Isdemiiirrr

                    r = s.post(date_url, data=date_payload, headers={
                        "user-agent": user_agent,
                        "x-requested-with": "XMLHttpRequest",
                        "referer": "https://www.instagram.com",
                        "x-csrftoken":csrf
                    })

                    print('---------------------------')
                    print('\n')
                    print(r.status_code)
                    print(r.url)
                    print(r.text)
                    print('---------------------------')
                    print('\n')

                    check_egligible_content = '"eligible_to_register":true'

                    if check_egligible_content in r.text and str(r.status_code) == '200':

                        r = s.post('https://i.instagram.com/api/v1/accounts/send_verify_email/', data=send_vertification_data, headers={
                            "user-agent": user_agent,
                            "x-requested-with": "XMLHttpRequest",
                            "referer": "https://www.instagram.com",
                            "x-csrftoken":csrf
                        })
                        
                        print('---------------------------')
                        print('\n')
                        print(r.status_code)
                        print(r.url)
                        print(r.text)
                        print('---------------------------')
                        print('\n')

                        email_send_response = '"email_sent":true'

                        if email_send_response in r.text and str(r.status_code) == '200': 

                            r = s.post('https://i.instagram.com/api/v1/accounts/check_confirmation_code/', data={
                                'code': FakeMail.VertificationCode(),
                                'device_id': 'Yh4XGQAEAAGsqDLUWFSJQ_d9CNbg',
                                'email': self.fmail
                            },
                            
                            headers={
                                "user-agent": user_agent,
                                "x-requested-with": "XMLHttpRequest",
                                "referer": "https://www.instagram.com",
                                "x-csrftoken":csrf
                            })

                            print('---------------------------')
                            print('\n')
                            print(r.status_code)
                            print(r.url)
                            print(r.text)
                            print('---------------------------')
                            print('\n')

                            if str(r.status_code) == '200':
                                print('************************')
                                print('      ************      ')
                                print('         ******         ')

                                print('Account Is Created')

                                print('Full_Name ==> {}'.format(self.fname))
                                print('Username ==> {}'.format(self.uname))
                                print('Password ==> {}'.format(self.passwd))

                                print('         ******         ')
                                print('      ************      ')
                                print('************************')
                            else:
                                print('XXXXXXXXXXXXXXXXXXXXXXXX')
                                print('Account Was Not Created')
                                print('XXXXXXXXXXXXXXXXXXXXXXXX')
                                exit(0)
                        else:
                            print('XXXXXXXXXXXXXXXXXXXXXXXX')
                            print('Account Was Not Created')
                            print('XXXXXXXXXXXXXXXXXXXXXXXX')
                            exit(0)

                    else:
                        print('XXXXXXXXXXXXXXXXXXXXXXXX')
                        print('Account Was Not Created')
                        print('XXXXXXXXXXXXXXXXXXXXXXXX')
                        exit(0)

                else:
                    print('XXXXXXXXXXXXXXXXXXXXXXXX')
                    print('Account Was Not Created')
                    print('XXXXXXXXXXXXXXXXXXXXXXXX')
                    exit(0)

            except Exception as e:
                print(e)


if __name__ == '__main__':

    print('********************')
    print('1.Create Account')
    print('********************')
    operation = input('Please Select Operation ')
    gender = input('Please type user gender ')
    country = input('Please type user country ')
    loop_limit = int(input('Please type account number '))

    counter = 0
    if operation == '1':
        if gender == 'male':
            if country == 'Azerbaycan':
                while counter < loop_limit:
                    fmail = FakeMail.GetMail()
                    fname, uname, paswd = Info('male', 'azerbaijani').GenerateUserInfo()
                    day, month, year = Date().GenerateDate()
                    proxy = ProxyRouter().FindProxsy()
                    try:
                        Auth(fmail, uname, fname, paswd, day, month, year, proxy).create_account()
                        print('\n')
                        print('----------------------')
                        print('Account Info =====> {}, {}'.format(uname, paswd))
                        print('----------------------')
                        print('\n')
                    except:
                        print("Account Was Not Created")
                        break
                    
                    counter += 1
        elif gender == 'female':
            if country == 'Azerbaycan':
                while counter < loop_limit:
                    fmail = FakeMail.GetMail()
                    fname, uname, paswd = Info('female', 'azerbaijani').GenerateUserInfo()
                    day, month, year = Date().GenerateDate()
                    proxy = ProxyRouter().FindProxsy()
                    try:
                        Auth(fmail, uname, fname, paswd, day, month, year, proxy).create_account()
                        counter += 1
                    except:
                        print("Account Was Not Created")
                        break

   

  
