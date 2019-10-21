import sys

sys.path.append('python-fitbit/')
import fitbit
import gather_keys_oauth2 as Oauth2
import matplotlib.pyplot as plt
import numpy as np
from  datetime import datetime
import time
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

while True :
    auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
    fitbit_stats = auth2_client.intraday_time_series('activities/heart', base_date="2017-08-07", detail_level='1sec')
    fitbit_stats2 = auth2_client.intraday_time_series('activities/steps', base_date="2017-08-07", detail_level='1min')


    stats = fitbit_stats['activities-heart-intraday']['dataset']
    stats2 = fitbit_stats2['activities-steps-intraday']['dataset']
    # print(stats)

    f1 = open('HR'+ date +'.txt', 'w')
    HR = []
    for var in range(0, len(stats)):
        f1.write(stats[var]['time'])
        f1.write("\t")
        f1.write(str(stats[var]['value']))
        f1.write("\n")
        HR = HR + [stats[var]['value']]

    f1.close()

    f2 = open('steps'+ date +'.txt', 'w')
    steps = []
    for var in range(0, len(stats2)):
        f2.write(stats2[var]['time'])
        f2.write("\t")
        f2.write(str(stats2[var]['value']))
        f2.write("\n")
        HR = HR + [stats2[var]['value']]
    f2.close()

    stats = auth2_client.activity_logs_list(after_date='2017-07-20')

    a = stats.get('activities')
    for i in (0, len(stats)):
        b = a[i]['logId']
        print(b)
        tcxd = auth2_client.activity_tcx(log_id=b)
        save = 'TCX' + date + str(b) + '.txt'
        f = open(save, 'w')
        f.write(ET.tostring(tcxd).decode('utf-8'))
        time.sleep(600)

