from google.oauth2 import service_account
import googleapiclient.discovery
import datetime
import texttable
import os


class PyMeetups:
    def __init__(self):
        self.calendar_id = "j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com"
        self.calendar_id_groups = "3haig2m9msslkpf2tn1h56nn9g@group.calendar.google.com"
        self.SERVICE_ACCOUNT_FILE = ("{}/project.json".format(os.path.dirname(os.path.realpath(__file__))))
        self.SCOPES = [
            'https://www.googleapis.com/auth/calendar',
            'https://www.googleapis.com/auth/calendar.readonly',
        ]
        self.time_min = datetime.datetime.now().strftime('%Y-%m-%dT00:00:00.000Z')

    def fetch_events_from_calendar(self, cal_id):
        page_token = None
        credentials = service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        calendar = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
        events = []
        while True:
            response = calendar.events().list(
                calendarId=cal_id, timeMin=self.time_min, pageToken=page_token
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
                if key in headers_to_show:
                    if key == headers_to_show[2]:
                        d[key] = value.get('dateTime', value.get('date'))
                    else:
                        d[key] = value

            if len(d):
                filtered_events.append(d)
        return filtered_events

    def populate_texttable(self):
        events1 = self.fetch_events_from_calendar(self.calendar_id)
        events2 = self.fetch_events_from_calendar(self.calendar_id_groups)
        events = events1 + events2
        filtered_events = self.filter_events(events)
        rows = [i.values() for i in filtered_events]
        table = texttable.Texttable()
        table.header(filtered_events[0].keys())
        table.set_cols_align(["l", "l", "l"])
        table.set_cols_valign(["m", "m", "m"])
        table.add_rows(rows,header=False)
        print(table.draw())