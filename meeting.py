
# Externals
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Internals
from .seminar import seminar

class meeting(seminar):

    def __init__(self,name,speaker=None,title=None,program=None,date=None,room=None):
        '''
        Args:
            name: string, Instance name
            speaker: string, speaker and affiliation
            title: string, seminar title
            program: string, program or abstract
            date: datetime, seminar date and time
            location: seminar location (room)
        '''

        # Base class init
        super(meeting,self).__init__(name,speaker,title,program,date,room)
        
    def prepemail(self,subject=None,head='',tail=''):
        '''
        Prepare a group meeting announcement email (self.email)
        Args:
           subject: if not None, ovewrites default email subject
           head: email head
           tail: email tail
        '''
        
        # Check that everything is there
        assert self.date is not None,    'Date missing'
        assert self.room is not None,    'Location missing'
        assert self.program is not None, 'Description is missing'

        # Create a message
        ## Head
        msg = head 
        msg += self.name+' - '+self.dayandtime()+' - '+self.room+'\n\n'
        ## Au programme
        msg += 'Au programme:\n\n'
        msg += self.program
        ## Tail
        msg += tail

        # Create a plain text email
        self.email = MIMEText(msg)

        # Create a subject
        self.email['Subject'] = subject            
        if subject is None:
            self.email['Subject'] = self.subject()

        # All done
        return

    def printMSG(self):
        '''
        Print announcement email
        '''
        if self.email is None:
            print('No announcement email')
        else:
            print('====')            
            if self.email['From'] is not None:
                print('From: '+self.email['From'])
            if self.email['To'] is not None:                
                print('To: '+self.email['To'])
            if self.email['Cc'] is not None:                
                print('Cc: '+self.email['Cc'])
            if self.email['Subject'] is not None:                
                print('Subject: '+self.email['Subject'])
            print(self.email.get_payload(decode=True).decode('utf-8'))
            print('====')            

