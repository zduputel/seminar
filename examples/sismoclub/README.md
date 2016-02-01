# Sismo-club

## Description
The Sismo-Club is a weekly meeting organized by the Strasbourg seismology team since 2011. Main organisers are Zacharie Duputel, Olivier Lengline, and Christophe Zaroli.

## Some instructions
"sismoclub.py" is the main driver script used to prepare Sismo Club announcements.

This script is based on google calendar events. To access google calendar API, follow the instructions detailed in the [Google Calendar Python Quickstart](https://developers.google.com/google-apps/calendar/quickstart/python).

This script is executed every morning using crontab:
- On announcement day (friday), an email is prepared and send if a meeting is scheduled next week.
- Reminders are sent the day before and the day of the Sismo club.

Input parameters are defined in "Arguments.py" (smtp server & port, email sender and recipients, calendar ID, ...). AnnoucementDay is the day of the weekly annoucement (5 is for friday).

The smtp user and password must be specified in environment variables SMTP_USER and SMTP_PASS.



