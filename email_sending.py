from setup import *
from assassin_class import *
from login_details import username, pwd, author
import smtplib
 
def send_email(to_addresses, message, cc_addresses=[], from_address='assassins.guild.cambridge@gmail.com',
              subject='The Assassins\' Guild',
              login=username, password=pwd,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_address
    header += 'To: %s\n' % to_addresses
    header += 'Cc: %s\n' % cc_addresses
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(username,password)
    problems = server.sendmail(from_address, to_addresses, message)
    server.quit()
    return problems

def sned_hlep(issue):
    problems = send_email(author, issue)
    if problems != {}:
        print('Connection issue, please try again later.')
    else:
        print('Request successful. Help is on its way!')
    
