from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import *
from parser import *
import time

pnconfig = PNConfiguration()
 
pnconfig.subscribe_key = 'sub-c-5d82d684-ac53-11e6-b6b9-0619f8945a4f'
pnconfig.publish_key = 'pub-c-3d6b5072-f825-4fad-9a0f-099fc2cd6a4d'
 
pubnub = PubNub(pnconfig)
 
 
def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];
 
 
class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass
 
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass
 
        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            pubnub.publish().channel("leap_motion_gesture_channel").message("rasperri-pi connected to channel!").async(my_publish_callback)
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
 
    def message(self, pubnub, message):
	if message.message == 'parsing_done' or message.message == 'rasperri-pi connected to channel!':
		return
        parsed_msg = parse_message(message.message)
	if 'type' in parsed_msg and parsed_msg['type'] == 'swipe':
        	print parsed_msg	
		time.sleep(3)
	pubnub.publish().channel("leap_motion_gesture_channel").message("parsing_done").async(my_publish_callback)
        return parsed_msg
        # pass  # Handle new message stored in message.message
 
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('leap_motion_gesture_channel').execute()

