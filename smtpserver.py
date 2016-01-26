#! /usr/bin/python
# -*- encoding: utf-8 -*-
 
import os
import signal 
import asyncore
import email.utils
import time
import datetime
import sys, getopt
from smtpd import SMTPServer
from datetime import datetime

path = os.getcwd() + "/messsages"


class SmtpServer(SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        message = datetime.now().strftime("%d-%m-%Y_%H_%S") + ".csv"
        if not os.path.exists(path):
            os.mkdir(path)
        f = open(path + "/" + message, "w")
        f.write(data)
        f.close()
        print "%s saved." % message
def run():
    if not os.path.exists(path):
        os.mkdir(path)
    SmtpServer(("localhost", 25), None)
    print "SMTP server is runing ..... "
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass
def stop():
    print 'For stop service usage Ctrl-C'
def static():
  for root, dirs, files in os.walk(path):
   for f in files:
       print os.path.join(root,f)
def help():
  print "The SMTP server version 1.0"
commands = {
    "--start":run,
    "--stop" :stop,
    "--stat" :static,
    "--help" :help
}
if __name__ == "__main__":
   try:
    commands[" ".join(sys.argv[1:])]()
   except KeyError:
     print "Usage: --start or --stop(Usage Ctrl-C for stop service). For More information please use --help. For Statistics usage --stat" 
      
