from slacker import Slacker
import sys

token = 'xoxp-67087862611-358792453505-504475924961-8849924bd58116df7e2e4c0a1c9cb7e7'

# name of channel
c_name = 'result_als_v2'

# file path
f_path = "vtk/0127202757/1500_1599/301000_15"

# upload
slack = Slacker(token)
for i in range(100):
    if(i >= 93) :
        print(f_path+str(i).zfill(2)+".vtk")
        slack.files.upload(f_path+str(i).zfill(2)+".vtk", channels=[c_name])
