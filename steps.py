import sys

sys.path.append('python-fitbit/')
import fitbit
import gather_keys_oauth2 as Oauth2
import matplotlib.pyplot as plt
import numpy as np

"""for OAuth2.0"""
USER_ID = "228HGC"
CLIENT_SECRET = "fa491321f0bbc0b83a6a2f59a6e725f9"


server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
server.browser_authorize()

token = server.fitbit.client.session.token
ACCESS_TOKEN = token["access_token"]
REFRESH_TOKEN = token["refresh_token"]
print("Access-token = {}".format(ACCESS_TOKEN))
print("Refresh-token = {}".format(REFRESH_TOKEN))


auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


"""Getting data"""
fitbit_stats = auth2_client.intraday_time_series('activities/steps',base_date="2017-06-28",detail_level="15min")


stats = fitbit_stats['activities-steps-intraday']['dataset']
print(stats)


'''
f1 = open('ondaystep.txt', 'w')
HR = []
for var in range(0, len(stats)):
    f1.write(stats[var]['time'])
    f1.write("\t")
    f1.write(str(stats[var]['value']))
    f1.write("\n")
    HR = HR + [stats[var]['value']]
'''
