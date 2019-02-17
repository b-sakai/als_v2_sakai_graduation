from slacker import Slacker
import sys

token = 'xoxp-67087862611-358792453505-504475924961-8849924bd58116df7e2e4c0a1c9cb7e7'

# name of channel
c_name = 'result_als_v2'

# message
print sys.argv
message = sys.argv
while "-c" in message:
    message.remove("-c")
joined_message = '\n'.join(sys.argv)
#message = "test"


# upload
slack = Slacker(token)
slack.chat.post_message(c_name, joined_message)

