import sys
sys.path.append('python-fitbit/')
import fitbit
import gather_keys_oauth2 as Oauth2
import time
from  datetime import datetime
import threading
import json
import xml.etree.ElementTree as ET



now = datetime.now()
date = datetime.strftime(datetime.now(), '%Y-%m-%d')
USER_ID = "228LFN"
CLIENT_SECRET = "642a48bcac2f5f0161a03279a1495d89"


server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
server.browser_authorize()

token = server.fitbit.client.session.token
ACCESS_TOKEN = token["access_token"]
REFRESH_TOKEN = token["refresh_token"]
print("Access-token = {}".format(ACCESS_TOKEN))
print("Refresh-token = {}".format(REFRESH_TOKEN))
auth2_client = fitbit.Fitbit(USER_ID,CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)




now = datetime.now()
date = datetime.strftime(datetime.now(), '%Y-%m-%d')
USER_ID = "228LFN"
CLIENT_SECRET = "642a48bcac2f5f0161a03279a1495d89"


server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
server.browser_authorize()

token = server.fitbit.client.session.token
ACCESS_TOKEN = token["access_token"]
REFRESH_TOKEN = token["refresh_token"]
print("Access-token = {}".format(ACCESS_TOKEN))
print("Refresh-token = {}".format(REFRESH_TOKEN))

auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
fitbit_stats = auth2_client.intraday_time_series('activities/heart',start_time="14:00", end_time="15:00", base_date=now, detail_level='1sec')
stats = fitbit_stats
print(stats)

with open('c:\HR\Heratrate' + date+ '.json', 'r') as outfile:
    json.dump(stats, outfile, indent=4)

fitbit_stats2 = auth2_client.intraday_time_series('activities/steps', start_time="14:00", end_time="15:00",base_date=now, detail_level='1min')
stats2 = fitbit_stats2
print(stats2)


with open('c:\STEPS\Steps' + date+ '.json', 'r') as outfile:
    json.dump(stats2, outfile,indent=4)

stats = auth2_client.activity_logs_list(after_date='2017-08-25')

a = stats.get('activities')
for i in (0, len(stats)):
    b = a[i]['logId']
    print(b)
    tcxd = auth2_client.activity_tcx(log_id=b)
    save = 'c:\TCX\TCX' + date + '.xml'
    f = open(save, 'w')
    f.write(ET.tostring(tcxd).decode('utf-8'))



