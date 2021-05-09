#Vaccine Notifier by Sahil Sharma

#///////////////////////////////////////////////////////////////////////////////////////
#//Terms of use
#///////////////////////////////////////////////////////////////////////////////////////
#//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#//IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#//FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#//AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#//LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#//OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#//THE SOFTWARE.
#///////////////////////////////////////////////////////////////////////////////////////
# Copyright (c) 2021, Sahil Sharma, All rights reserved.

import smtplib   
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
from suds.client import Client
from email.message import EmailMessage
from datetime import date
import time

age = 18 #Age 18 for (18-44) group and age 45 gor (45+) group
district_id = 230 #Your District Id [Example - 230 for JAMMU]
max_search_days = 12 #Number of days - search region
to_list = ['receiver_1@gmail.com','receiver_2@gmail.com']#receiver list
gmail_user = 'sender' #Sender email account (DON'T ENTER @gmail.com)
gmail_password = '**password**' #Sender email password 

while True:
    today_date = str(date.today())
    vax_date = int(today_date[8:])

    session_date = []
    session_capacity = []
    center_name = []
    center_address = []
    center_pincode = []

    for i in range(max_search_days):
        print("Searched Completed for Date: "+str(today_date[:7])+"-{}".format(vax_date))
        slot_avaiable = False
        url = Request("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&amp;date="+str(vax_date)+"-05-2021",headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(url, timeout=10).read()
        soup = BeautifulSoup(html)

        for script in soup(["script", "style"]):
            script.decompose()

        required_dict = json.loads(soup.get_text())
        final_list = required_dict['centers']
        for i in range(len(final_list)):
            for k in range(len(final_list[i]['sessions'])):
                if final_list[i]['sessions'][k]['available_capacity'] > 0 and final_list[i]['sessions'][k]['min_age_limit'] == age and int(final_list[i]['sessions'][k]['date'][:2]) == vax_date :
                    session_date.append(final_list[i]['sessions'][k]['date'])
                    session_capacity.append(final_list[i]['sessions'][k]['available_capacity'])
                    center_name.append(final_list[i]['name'])
                    center_address.append(final_list[i]['address'])
                    center_pincode.append(final_list[i]['pincode'])
                    slot_avaiable = True
                
        if slot_avaiable:
            #Fast Alert
            sent_from = gmail_user
            to = to_list
            subject = 'Slot Avaiable'
            email_text = 'Slot Available'

            #email send request
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            #Detalied Alert
            string=''
            for i in range(len(session_date)):
                string += str(i)+'. '+str(session_date[i])+' | '+'CAPACITY:'+str(session_capacity[i])+' | '+"PINCODE:"+str(center_pincode[i])+' | '+'CENTER:'+str(center_name[i])+' | '+"ADDRESS:"+str(center_address[i])+'\n'

            msg = EmailMessage()
            msg.set_content(string)

            msg['Subject'] = 'Slot Available'
            msg['From'] = gmail_user
            msg['To'] = to_list

            # Send the message via our own SMTP server.
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(gmail_user, gmail_password)
            server.send_message(msg)
            server.quit()
            print('Mail_Sent!! Book your slot on cowin.gov.in')
            time.sleep(30)
        vax_date += 1
        time.sleep(5)
    time.sleep(30)
