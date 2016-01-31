# seminar

seminar is a simple time saving python module for automating seminar announcements.

## Dependencies
- python2 or python3
- python modules: smtplib, email, datetime, dateutil
- Optional: Google calendar API (see [Google Calendar Python Quickstart](https://developers.google.com/google-apps/calendar/quickstart/python))
- Job scheduler (e.g., cron).

## Some instructions
The seminar directory must be placed in a path pointed by the PYTHONPATH environment variable.

To use seminar, simply import the seminar module
```
import seminar
```
or 
```
from seminar import seminar, utils
```
seminar is the base class used to build seminar annoucements, utils include tools to access google calendar events (see utils.googlecalendar.getevents)







