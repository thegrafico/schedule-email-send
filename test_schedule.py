#Dependencies
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

#Send mail function
def sendEmail():
    """Function to send mail from user to user """
    fromaddr = "test@gmail.com"
    toaddr = "burnsjosep@hotmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "HOUR send 11:20"

    body = "This message was send by python"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "PASSWORD GOES HERE")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Email was send to", toaddr)
    

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(sendEmail, 'cron', day_of_week='0-6',hour=12, minute=46)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


#LINKS References
# https://github.com/agronholm/apscheduler/tree/master/examples
# https://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html#module-apscheduler.triggers.cron
# https://apscheduler.readthedocs.io/en/latest/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.add_job
# https://apscheduler.readthedocs.io/en/latest/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.add_job