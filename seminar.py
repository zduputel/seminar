# Externals
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class seminar(object):

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

        # Initialization
        self.name    = name
        self.speaker = speaker
        self.title   = title
        self.program = program
        self.date    = date
        self.room    = room
        self.smtp    = None
        
        # Email body
        self.email = None        

    def smtpconnect(self,server,port,user,password):
        '''
        Connect to smtp server
        Args:
           server: string, smtp server
           port: string, smtp server port
           user: string, the user name to authenticate with
           password: string, the password for the authentication.
        '''

        # Instantiate smtp server object
        self.smtp = smtplib.SMTP(server,port)

        # SMTP ehlo command
        ehlo = self.smtp.ehlo()        
        assert ehlo[0]==250, 'SMTP ehlo command failed'

        # Put connection into TLS mode
        tls  = self.smtp.starttls()
        assert tls[0]==220, 'Cannot put the connection into TLS mode'

        # Login
        login  = self.smtp.login(user,password)
        assert login[0]==235, 'Cannot log in on the SMTP server'

        # All done
        return        

    def sendMSG(self,sender,toaddr,ccaddr=[]):
        '''
        Send announcement email
        Args:
            sender:    string, the address sending this mail
            toaddr: list, a list of addresses to send this mail to.        
            ccaddr: list, a list of addresses to send a copy of this mail to.        
        '''

        # Check that everything is here
        assert self.smtp is not None, 'Not connected to smtp server (use self.smtpconnect)'
        assert self.email is not None, 'No email'
        assert isinstance(toaddr,list), 'toaddr must be a list'
        assert isinstance(ccaddr,list), 'ccaddr must be a list'        

        # Complete email header
        self.email['From'] = sender
        self.email['To']   = ', '.join(toaddr)
        self.email['Cc']   = ', '.join(ccaddr)

        # Send email
        self.smtp.sendmail(sender,toaddr+ccaddr,self.email.as_string())

        # All done
        return
    
    def dayandtime(self):
        '''
        Returns day and time of seminar
        '''
        return self.date.strftime('%A %-d %B - %Hh%M')

    def day(self):
        '''
        Returns day of seminar
        '''
        return self.date.strftime('%A %-d/%m')
    
    def subject(self,prefix='',name=True,day=True,speaker=True):
        '''
        Set email subject
        Args:
           prefix: string, email subject prefix
           name: bool, if true append self.name
           day: bool, if true append seminar day
           speaker: bool, if true append speaker name
        '''

        # Append prefix
        subject = prefix

        # Append seminar name
        if name is True:    
            subject += self.name

        # Append seminar day
        if day is True:     
            subject +=' - '+self.day()

        # Append seminar speaker
        if speaker is True and self.speaker is not None:
            subject += ' - '+self.speaker
                
        # All done
        return subject
    
    def talkMSG(self,subject=None,head='',tail=''):
        '''
        Prepare a talk announcement email (self.email)
        Args:
           recipients: list of email addresses
           subject: if not None, ovewrites default email subject
           head: email body header
           tail: email body tail
        '''

        # Check that everything is there
        assert self.speaker is not None, 'Speaker name missing'
        assert self.title is not None,   'Title missing'
        assert self.date is not None,    'Date missing'
        assert self.room is not None,    'Location missing'
        assert self.program is not None, 'Abstract is missing'
        
        # Create a message
        ## Head
        msg  = head
        msg += '-- '+self.name+'-- \n\n'        
        ## Au programme
        msg += 'Orateur: '+self.speaker+'\n\n'
        msg += 'Titre: '+self.title+'\n\n'
        msg += 'Date: '+self.dayandtime()+'\n\n'
        msg += 'Salle:'+self.room+'\n\n'
        msg += 'Abstract:'+self.program+'\n\n'        
        ## Tail
        self.email += tail

        # Create a plain text email
        self.email = MIMEText(msg)

        # Create a subject
        self.email['Subject'] = subject                    
        if subject is None:
            self.email['Subject'] = self.subject()

        # All done
        return

    def meetingMSG(self,subject=None,head='',tail=''):
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

