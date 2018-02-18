from google.oauth2 import service_account
import googleapiclient.discovery
import datetime
import tabulate
import os


class PyMeetups:
    def __init__(self):
        self.calendar_id = "j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com"
        self.SERVICE_ACCOUNT_FILE  = ("{}/project.json".format(os.path.dirname(os.path.realpath(__file__))))
        self.SERVICE_ACCOUNT_FILE  = ("{}/project.json".format(os.path.dirname(os.path.realpath(__file__))))
        self.SCOPES = [
            'https://www.googleapis.com/auth/calendar',
            'https://www.googleapis.com/auth/calendar.readonly',
        ]
        self.time_min = datetime.datetime.now().strftime('%Y-%m-%dT00:00:00.000Z')

    def fetch_events_from_calendar(self):
        page_token = None
        credentials = service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        calendar = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
        events = []
        while True:
            response = calendar.events().list(
                calendarId=self.calendar_id, timeMin=self.time_min, pageToken=page_token
            ).execute()
            events.extend([event for event in response['items']])
            page_token = response.get('nextPageToken')
            if not page_token:
                break
        return events

    def filter_events(self, events):
        headers_to_show = ['summary', 'location','start']
        filtered_events = []
        for event in events:
            d = {}
            for key, value in event.items():
                if key in headers_to_show and isinstance(value, str):
                    d[key] = value
                elif key in headers_to_show and not isinstance(value, str):
                    d[key] = value['date']

            if len(d):
                filtered_events.append(d)
        return filtered_events

    def populate_tabulate(self):
        events = self.fetch_events_from_calendar()
        filtered_events = self.filter_events(events)
        headers = filtered_events[0].keys()
        rows = [i.values() for i in filtered_events]
        print(tabulate.tabulate(rows,headers, tablefmt="rst"))