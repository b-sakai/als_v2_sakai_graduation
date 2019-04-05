from slacker import Slacker
import sys

token = ''

# name of channel
c_name = ''

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

