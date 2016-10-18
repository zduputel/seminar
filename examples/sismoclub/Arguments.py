
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
if os.path.exists('signature.txt'):
	emailtail=open('signature.txt','r').read()
else:
	emailtail = '\n'
