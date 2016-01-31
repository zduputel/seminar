
# Externals
import datetime
import dateutil.parser

# Internals
from seminar import meeting,utils

# Arguments
from Arguments import *

# Time stamps
Now = datetime.datetime.utcnow()
TimeSpan = 1
TimeMax = Now + datetime.timedelta(days=TimeSpan)
if Now.isoweekday() == AnnoucementDay:
    TimeSpan = 7
    TimeMax = Now + datetime.timedelta(days=TimeSpan)

# Get events
Now_s = Now.isoformat() + 'Z' #'Z' indicates UTC time
TimeMax_s = TimeMax.isoformat() + 'Z'
events = utils.googlecalendar.getevents(calendar,Now_s,TimeMax_s)
if not events and TimeSpan == 1:
    TimeSpan = 2
    TimeMax = Now + datetime.timedelta(days=TimeSpan)
    TimeMax_s = TimeMax.isoformat() + 'Z'
    events = utils.googlecalendar.getevents(calendar,Now_s,TimeMax_s)
print(TimeSpan,events)

# Parse info
if not events:
    print('No upcoming events found.')

# Parse events
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
    subject = s.subject(prefix=summary,name=False,speaker=False)
    emailhead = ''
    if TimeSpan == 1:
        subject = 'RAPPEL - Sismo Club - '+s.time()+' - '+s.room
        emailhead = '-- RAPPEL --\n\n'
    
    # Prepare email
    s.prepemail(subject=subject,head=emailhead,tail=emailtail)
    
    # Send email
    s.smtpconnect(smtp_serv,smtp_port,smtp_user,smtp_pass)
    s.sendemail(sender,toaddrs,ccaddrs)

    # Print email
    s.printemail()    
    

