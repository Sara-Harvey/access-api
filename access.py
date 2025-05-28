import csv
from time import sleep
import requests

url = "https://www.muckrock.com/api_v1/"
next_ = url + 'statistics/'

fields = (
    "date",
    "total_requests",
    "total_requests_success",
    "total_requests_denied"
)

page = 1

# make this true while exporting data to not crash on errors
SUPRESS_ERRORS = False 

while next_ is not None:
    r = requests.get(next_)
    try:
        json = r.json()
        next_ = json['next']
        for datum in json['results']:
            statistical_values = [datum[field] for field in fields]

            with open('output1.csv', 'a', newline='') as csvfile:
                statswriter = csv.writer(csvfile)
                statswriter.writerow(statistical_values)

        #print('Page %d of %d' % (page, json['count'] / 20 + 1))
        page += 1
    except Exception as e:
        print('Error'), e
        if not SUPRESS_ERRORS:
            raise
