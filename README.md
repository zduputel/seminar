# seminar

"seminar" is a simple time saving python module for automating seminar announcements.
It will format and send announcement and reminder emails via smtp. 

## Dependencies
- python2 or python3
- python modules: smtplib, email, datetime, dateutil
- Optional: Google calendar API (see [Google Calendar Python Quickstart](https://developers.google.com/google-apps/calendar/quickstart/python))
- Optional: Job scheduler (e.g., cron).

## Some instructions
The seminar directory must be placed in a path pointed by the PYTHONPATH environment variable.

To use seminar, simply import the seminar module
```
import seminar
```
or 
```
from seminar import seminar, meeting, utils
```
where
- seminar is the base class used to build seminar annoucements
- meeting is the class used to build group meeting annoucements
- utils include tools to access google calendar events (see utils.googlecalendar.getevents)

An example of driver script used to prepare and send email for a group meeting is included in examples/sismoclub







