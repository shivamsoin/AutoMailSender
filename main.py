import smtplib
import datetime as dt
import random
import time 
mail='YOUR_MAIL_ID'
password='YOUR_PASSWORD'
now = dt.datetime.now()
weekday = now.weekday()
if weekday==3:
    with open("quotes.txt",encoding='utf-8') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    connection=smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=mail,password=password)
    connection.sendmail(from_addr=mail,to_addrs='RECIEVERS_ADDRESS',msg=f'Subject: Motivation of the Day\n\n{quote}')
    time.sleep(3)
    connection.sendmail(from_addr=mail, to_addrs='RECIEVERS_ADDRESS',msg=f'Subject: Motivation of the Day\n\n{quote}')
    time.sleep(3)
    connection.sendmail(from_addr=mail, to_addrs='RECIEVERS_ADDRESS',msg=f'Subject: Motivation of the Day\n\n{quote}')
    time.sleep(3)
    connection.sendmail(from_addr=mail, to_addrs='RECIEVERS_ADDRESS',msg=f'Subject: Motivation of the Day\n\n{quote}')
    time.sleep(3)
    connection.sendmail(from_addr=mail,to_addrs='RECIEVERS_ADDRESS',msg=f'Subject: Motivation of the Day\n\n{quote}')
    time.sleep(3)
    connection.sendmail(from_addr=mail,to_addrs='RECIEVERS_ADDRESS',msg=f'Subject: Motivation of the Day\n\n{quote}')

    connection.close()

