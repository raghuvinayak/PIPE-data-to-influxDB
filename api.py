
import sys
import socket
import threading
from flask import Flask
from flask import send_file
import os
import time
from multiprocessing import Process
import subprocess, shlex


app = Flask(__name__)



#DPMI strings 
@app.route('/run/<string:stream>', methods = ['GET'])
def start_process(stream):
        address = stream.split('_')
        global gstream
        gstream = '::'.join(address)
        Process(target = start_king(stream)).start()
        return "please wait........"

#stop DPMI utils

@app.route('/stop', methods=['GET'])
def stop_service():
         os.system("sudo pkill bitrate")
#pkill bitrate
         return "DPMI bitrate stoped\n"

#add New stream

@app.route('/add/<string:NewStream>', methods=['GET'])
def add_stream(NewStream):

        gstream=start_process(stream)
	address = NewStream.split('_')
	addstream = '::'.join(address)
        stop_service()
        time.sleep(1)
        start_process(gstream+' '+addstream)
        return "stream added\n"
