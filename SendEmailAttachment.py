from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import csv

def SendEmailAttachment(recipients,attachments):


	#---------- prepare recipient list ---------------------#

	
	#emaillist = [elem.strip().split(',') for elem in recipients]
	emaillist = recipients

	#----------- prepare MIME Multipart message -----------#

	msg = MIMEMultipart()
	msg['Subject'] = 'COMS 103 Homework Feedback'   #subject of email
	msg['From'] = 'boudhayanbanerjee@gmail.com'     #sender's email
	msg['Reply-to'] = 'bbanerji@iastate.edu' #sender's email

	msg.preamble = 'Multipart massage.\n'
	
	#---------- email body goes here ------------#

	msg_html = """<html>
      		   <head></head>
               <body>
               <p>Hi,<br><br>
               Here is your week 3 graded homework.Please see detailed explanation in the attachment.<br>
               If you have any questions,please let me know.
               You can send me an email through Blackboard or come to my help desk hours in B17 Atanasoff during the following time:<br>
               <b>Tuesdays: 2pm-3pm</b><br><br>
               Best Regards,<br>Group 5 TA,Ronnie</p>
               </body>
               </html>"""

	part = MIMEText(msg_html,'html')
    
    #------- attach email body to message -------#

	msg.attach(part)
	
    #------- attach the email attachment to message ------#

	#part = MIMEApplication(open('JesusGilG5WK4HW.zip',"rb").read())
	part = MIMEApplication(open(attachments,"rb").read())  
	part.add_header('Content-Disposition', 'attachment', filename=attachments)
	msg.attach(part)
	 
    #------- stat the email server -------#
	server = smtplib.SMTP("smtp.gmail.com:587")
	#server.ehlo()
	try:
	    server.starttls()
	except:
	    print("Problem while starting mail server\n")
    
    #------ login to the server ----------#
	try:
	    server.login(msg['From'],"lqougbpjrqghrmeq") 
	except Exception as e:
	    print("Problem while login\n")
    
    #------ send the email -------#
	try: 
		server.sendmail(msg['From'], emaillist , msg.as_string())
		print("Email sent successfully")
	except:
		print("Could not send email.Please try again\n")

	

