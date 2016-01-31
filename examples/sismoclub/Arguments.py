
# Set locale
import locale
import os
locale.setlocale(locale.LC_ALL,'fr_FR')

# Announcement schedule
AnnoucementDay = 5 # On Friday

# email
smtp_serv = 'mailserver.u-strasbg.fr'
smtp_port = 587
smtp_user = os.getenv('SMTP_USER')
smtp_pass = os.getenv('SMTP_PASS')
sender  = 'zacharie.duputel@unistra.fr'
toaddrs = ['zacharie.duputel@gmail.com']  # email list
ccaddrs = ['zacharie.duputel@unistra.fr']

# Calendar ID
calendar = 'egeeicevj7j1hg1vjshqd1deac@group.calendar.google.com'

# Default location
default_room = 'Cafeteria du 4eme Etage'

# Email tail
emailtail = '''\n
Christophe, Olivier et Zacharie
\n
-- Subscribe to online calendar for sismo-club --

For iCal users (mozzila thunderbird,google calendar,apple calendar,...), use the following URL:
https://www.google.com/calendar/ical/egeeicevj7j1hg1vjshqd1deac%40group.calendar.google.com/public/basic.ics

An HTML format is also available at:
https://www.google.com/calendar/embed?src=egeeicevj7j1hg1vjshqd1deac%40group.calendar.google.com&ctz=Europe/Paris
'''
