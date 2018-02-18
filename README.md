# PyMeetups

Find information about upcoming Python conferences and meetups through your terminal

![PyMeetups screenshot](https://image.ibb.co/hcK9WS/carbon_1_1.png)

## Installation
`pip install pymeetups`

## Usage
Run the command `pymeetups` which displays information of upcoming Python conferences.

### Future 

- [ ] Apart from Pycon conferences show information about Python meetups.
- [ ] Feature to filter the list of conferences/meetups with the commands `pymeetups nearme` and `pymeetups <region name>` 

### Contributing

 - Pymeetups uses Google Calendar API. Follow instruction as per [this documentation](https://developers.google.com/google-apps/calendar/quickstart/python) to create and download a JSON file containing client id and client secret id.
 - Rename the JSON file to `project.json` and place it inside pymeetups package such that the path is `pymeetups/pymeetups/package.json`
- Start hacking.

### License
MIT
