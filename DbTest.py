import pymssql
import sys

sys.path.append('python-fitbit/')
import fitbit
import gather_keys_oauth2 as Oauth2
import time
from  datetime import datetime
import json

now = datetime.now()
date = datetime.strftime(datetime.now(), '%Y-%m-%d')
USER_ID = "228P7W"
CLIENT_SECRET = "feb10d79fbcc77ae416f1f633fab43b1"

server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
server.browser_authorize()

token = server.fitbit.client.session.token
ACCESS_TOKEN = token["access_token"]
REFRESH_TOKEN = token["refresh_token"]
print("Access-token = {}".format(ACCESS_TOKEN))
print("Refresh-token = {}".format(REFRESH_TOKEN))
auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

fitbit_stats = auth2_client.intraday_time_series('activities/heart', base_date=now, detail_level='1sec')
stats = fitbit_stats
print(stats)

stats = fitbit_stats
with open('Heratrate' + date + '.json', 'w') as outfile:
    json.dump(stats, outfile, indent=4)

fitbit_stats2 = auth2_client.intraday_time_series('activities/steps', base_date=now, detail_level='1min')
stats2 = fitbit_stats2
print(stats2)

stats2 = fitbit_stats2['activities-steps-intraday']['dataset']
with open('Steps' + date + '.json', 'w') as outfile:
    json.dump(stats2, outfile, indent=4)


    data = json.loads(stats)








