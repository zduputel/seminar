

# Externals
import datetime
import dateutil.parser

# Internals
from googlecalendar import getevents
from seminar import seminar

# Arguments
from Arguments import *

# Time stamps
Now       = datetime.datetime.utcnow()
inOneWeek = Now + datetime.timedelta(days=7)
Now       = Now.isoformat() + 'Z' #'Z' indicates UTC time
inOneWeek = inOneWeek.isoformat() + 'Z'

# Get events
events = getevents(calendar, Now, inOneWeek)

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
    s = seminar(name='Sismo Club',date=date,program=program,room=room)    
    subject = s.subject(prefix=summary,name=False,speaker=False)
    
    # Prepare email
    s.meetingMSG(subject=subject,tail=emailtail)
    
    # Send email
    s.smtpconnect(smtp_serv,smtp_port,smtp_user,smtp_pass)
    s.sendMSG(sender,toaddrs,ccaddrs)

    # Print email
    s.printMSG()    
    

