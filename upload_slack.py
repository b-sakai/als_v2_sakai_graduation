from slacker import Slacker
import sys

token = ''

# name of channel
c_name = ''

# file path
f_path = sys.argv[1]

# upload
slack = Slacker(token)
slack.chat.post_message(c_name, 'Hello')
slack.files.upload(f_path, channels=[c_name])
