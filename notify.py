#!/usr/bin/python3
import sys
import credentials
from pushsafer import Client

#
credID = "myAPIkey" if "myAPIkey" in credentials.creds else "default"

pk = credentials.creds[credID].password

def sendItNowMsg(message="Test Message", privKey="blablabla", title="ffmpeg", device="gs1715", retry=60, icon="1", sound=12,
        vibration=2, url="", urltitle="",priority=0,time2live=5, answer=0, picture1="", picture2="",    picture3="",
        expire=600):
        #init(privKey)
        client = Client(privKey)
        client.send_message(message=message, title=title, device=device, retry=retry, icon=icon,  sound=sound,
                vibration=vibration, url=url, urltitle=urltitle, priority=priority, time2live=time2live, answer=answer,
                picture1=picture1, picture2=picture2, picture3=picture3, expire=expire )
        del client

if __name__=="__main__":
    sendItNowMsg(message=str(sys.argv),privKey=pk)
