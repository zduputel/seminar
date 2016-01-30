from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getevents(calendar,timeMin,timeMax,maxResults=250):
    """
    Get Events in Google Calendar
    
    Args:
       calendar: string, Calendar identifier. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.
       timeMin: datetime, Lower bound (inclusive) for an event's end time to filter by.
       timeMax: datetime, Upper bound (exclusive) for an event's start time to filter by.
       maxResults: integer, Maximum number of events returned on one result page.
    
    Returns:
       List of event dictionaries
    """
    
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    
    eventsResult = service.events().list(
        calendarId=calendar, timeMin=timeMin,timeMax=timeMax, maxResults=maxResults,
        singleEvents=True,orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    return events



