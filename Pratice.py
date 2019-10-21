import sys
sys.path.append('python-fitbit/')
import fitbit
import gather_keys_oauth2 as Oauth2
import time
from  datetime import datetime
from ast import literal_eval
import json

now = datetime.now()
date = datetime.strftime(datetime.now(), '%Y-%m-%d')
USER_ID = "228L66"
CLIENT_SECRET = "a629081fd89cf39c6435477e2985609c"


server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
server.browser_authorize()

token = server.fitbit.client.session.token
ACCESS_TOKEN = token["access_token"]
REFRESH_TOKEN = token["refresh_token"]
print("Access-token = {}".format(ACCESS_TOKEN))
print("Refresh-token = {}".format(REFRESH_TOKEN))
auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
fitbit_stats = auth2_client.intraday_time_series('activities/heart', base_date="2017-09-07", detail_level='1sec')
stats = fitbit_stats
print(stats)

with open('Heratrate' + "2017-09-07" + '.json', 'w') as outfile:
        json.dump(stats, outfile, indent=4)

