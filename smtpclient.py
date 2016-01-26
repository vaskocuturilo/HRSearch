#! /usr/bin/python
# -*- encoding: utf-8 -*-
# Vasko Cuturuilo
import smtplib
import socket
import time
import datetime
import string
import random
import sys, getopt
from datetime import datetime
fromaddres = sys.argv[1]
toaddreses = sys.argv[2]
def prompt(prompt):
    return raw_input(prompt).strip()
def from_generator(size=3, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
def subject_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def to_generator(size=3, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
def data_generator(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def help():
 print 'Smtp Client v.1.0'
def run():
 fromaddr =from_generator()+'@'+"".join(fromaddres)
 subject = subject_generator()
 line = data_generator()
 IP =  "IP: " + (socket.gethostbyname(socket.gethostname()))
 Date = datetime.now().strftime("%d-%m-%Y_%H_%S")
 toaddrs  = to_generator()+'@'+"".join(toaddreses)
 msg = ("From: %s\r\nSubject: %s\r\nTo: %s\r\n"
       % (fromaddr, subject,toaddrs))
 msg = msg +IP+"\n"+Date+"\n"+"DATA: "+line
 server = smtplib.SMTP('localhost')
 server.set_debuglevel(1)
 server.sendmail(fromaddr,toaddrs,msg)
 server.quit()
commands = {
    "--start":run,
    "--help" :help
}
if __name__ == "__main__":
 #  try:
  #    commands[" ".join(sys.argv[3:])]()
  # except KeyError:
  #   print "Usage: --start for start service. Or --help for Help."
  run()
