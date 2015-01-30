RIMS
====

Usage
------

::
  $ python RIMSApp.py -h
  usage: RIMSApp.py [-h] [-server HSERVER] [-port HPORT]

  Start the listener for the demo RIMS app

  optional arguments:
    -h, --help       show this help message and exit
    -server HSERVER  Hostname to listen on. Default is 0.0.0.0
    -port HPORT      Port number of host to listen on. Default is 5000

Example Deployments
--------------------

To deploy externally on port 3509, execute:
::
  python RIMSApp.py -port 3509
    
To deploy to localhost on port 500 only, execute: 
::
  python RIMSApp.py -server 127.0.0.1 -port 5000
  
  