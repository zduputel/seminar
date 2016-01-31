
# Externals
import datetime
import dateutil.parser

# Internals
from seminar import meeting,utils



# Import input parameters
from Arguments import *



# Search events in calendar
## Time stamps
Now = datetime.datetime.utcnow()
TimeSpan = 1                                       # Default time span is 1 day
TimeMax = Now + datetime.timedelta(days=TimeSpan) 
if Now.isoweekday() == AnnoucementDay:             # If we are on annoucement day
    TimeSpan = 7                                   # time span is 7 days
    TimeMax = Now + datetime.timedelta(days=TimeSpan)

## Get events
Now_s = Now.isoformat() + 'Z' #'Z' indicates UTC time
TimeMax_s = TimeMax.isoformat() + 'Z'
events = utils.googlecalendar.getevents(calendar,Now_s,TimeMax_s)
if not events and TimeSpan == 1:                   # If there is no events, we use a 
    TimeSpan = 2                                   # span of two days and search again
    TimeMax = Now + datetime.timedelta(days=TimeSpan)
    TimeMax_s = TimeMax.isoformat() + 'Z'
    events = utils.googlecalendar.getevents(calendar,Now_s,TimeMax_s)

if not events:
    print('No upcoming events found.')

# Parse events and send emails
for event in events:

    # When?
    date  = event['start'].get('dateTime')
    if date is None:
        date  = event['start'].get('date')+'T13:00:00+01:00'
    date = dateutil.parser.parse(date)

    # What?
    summary = event['summary'].strip()
    program = event['description']

    # Where?
    room = event.get('location')
    if room is None:
        room = default_room

    # Seminar instantiation
    s = meeting(name='Sismo Club',date=date,program=program,room=room)

    # Define email subject and header
    if TimeSpan == 7: # Weekly announcement
        subject = s.subject(prefix=summary,name=False,speaker=False)
        emailhead = ''
    else:             # Reminder
        if s.date.weekday() == Now.weekday(): # Sismoclub is today
            prefix = 'RAPPEL: Sismo Club - Aujourd\'hui '+s.time()
            subject = s.subject(prefix=prefix,name=False,speaker=False,
                                day=False,time=False,room=True)            
            emailhead = '-- RAPPEL --\n\n'        
        else:                             # Sismoclub is tomorrow
            prefix = 'RAPPEL: Sismo Club'
            subject = s.subject(prefix=prefix,name=False,speaker=False,
                                time=True,room=True)
            emailhead = '-- RAPPEL --\n\n'
        
    
    # Prepare email
    s.prepemail(subject=subject,head=emailhead,tail=emailtail)
    
    # Send email
    s.smtpconnect(smtp_serv,smtp_port,smtp_user,smtp_pass)
    s.sendemail(sender,toaddrs,ccaddrs)

    # Print email
    s.printemail()    
    

