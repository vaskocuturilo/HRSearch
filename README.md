# HRSearch
Smtp Server and Smtp Client. 


Smtp Server 
=================================================================================================================================
For start Smtp Server Usage : 
 - sudo python smtpserver --start 
 For help Usage: 
 - sudo python smtpserver --help 
=================================================================================================================================


Smtp Client 
=================================================================================================================================
For start Smtp client Usage: 
 - python smtpclient From To --start 
 For help Usage: 
   python smtpclient From To --help

From - domain from email 
To -   domain to email
Example: python smtpclient.py from.rambler.ru to.google.ru --start 
=================================================================================================================================

Config.ini
===============================================================================================================================
Configuration File
[smtpserver] - address smtp server
[port] - port for the smtp server
[smtp client] - address smtp server for client 
