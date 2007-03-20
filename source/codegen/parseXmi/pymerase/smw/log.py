"""log is generic module for logging messages produced during the
execution of Python	programs.

The singleton class Logger is the main class of the module. We can obtain an
adapter for a Logger by invoking getLogger(name), where name is a string
describing the sender of the messages.

Once we have a logger adapter object, we can send a message to the
log using the debug, info, warning and fatal methods of the logger.

Example:

import log
logger=log.getLogger("example")
logger.info("Hej, this is a message")

The debug, info, warning and fatal methods accept an arbitrary number
of paramters. The final message will be the concatenation of all the passed
parameters after being converted to a string with str().

It is also possible to report an exception using the exception
method. In this case the last exception will be logged.

try:
	a= 1 / 0
except:
	logger.exception("Something unexpected happened!")

The Logger class supports suppressing messages by sender and
redirecting messages to registered listeners, but this still needs
some work.
"""

__author__="Ivan Porres"
__email__ ="iporres@abo.fi"

import time
import string
import traceback
import sys
import os

theLogger=None

class LogListener:
		def onLogEvent(self,channel,severity,msg,extra):
				pass
		
class Logger:
		def __init__(self):
				global theLogger
				assert(not theLogger)
				theLogger=self
				self.observers=[]
				self.channels={}
				self.lastTime=None
				
		def subscribe(self,o):
				"""Add a LogListener object to this Logger."""
				if o!=self and o not in self.observers:
						self.observers.append(o)

		def unsubscribe(self,o):
				"""Remove a LogListerner object."""
				if o in self.observers:
						self.observers.remove(o)

		def notify(self,channel,severity,msg,extra):
				for o in self.observers:
						o.onLogEvent(channel,severity,msg,extra)						

		def setChannel(self,channel,on):
				self.channels[channel]=on
				m="Channel "+channel+" is "
				if on:
						m=m+"on"
				else:
						m=m+"off"
				self.info("Logger",m)
				
		def error(self,channel,msg,extra=None):
				self.newEvent("E",channel,msg,extra)

		def info(self,channel,msg,extra=None):
				self.newEvent("I",channel,msg,extra)

		def warning(self,channel,msg,extra=None):
				self.newEvent("W",channel,msg,extra)

		def debug(self,channel,msg,extra=None):
				self.newEvent("D",channel,msg,extra)

		def newEvent(self,severity,channel,msg,extra=None):
				self.notify(channel,severity,msg,extra)
				if not self.channels.has_key(channel) or self.channels[channel]:
						now= time.strftime("%a, %d %b %Y %H:%M",time.localtime())
						if now!=self.lastTime:
								print "I Logger			 Local time is",now
								self.lastTime=now

						header=" %-12s" % channel[:12]
						if msg.find(os.linesep)== -1:
								while len(msg):
										print severity+header+" "+msg[:64]
										msg=msg[64:]
										severity="+"
						else:
								print severity+header+" >>>"
								if msg.endswith(os.linesep):
										msg=msg[:-len(os.linesep)]
								print msg
								print "+"+header+" <<<"
										
class LogAdapter:
		def __init__(self,name,logger):
				self.channel=name
				self.logger=logger

		def fatal(self,*args):
				"""A fatal error. Logs the message and exists"""
				s="FATAL:"
				for a in args:
						s=s+str(a)				
				self.logger.error(self.channel,s)
				sys.exit(-1)

		def error(self,*args):
				"""An error"""
				s=""
				for a in args:
						s=s+str(a)				
				self.logger.error(self.channel,s)
				
		def info(self,*args):
				"""An information message"""
				s=""
				for a in args:
						s=s+str(a)				
				self.logger.info(self.channel,s)

		def warning(self,*args):
				"""A warning or a non-fatal message"""
				s=""
				for a in args:
						s=s+str(a)				
				self.logger.warning(self.channel,s)

		def debug(self,*args):
				"""Debug information that it is only interesting for the developer"""
				s=""
				for a in args:
						s=s+str(a)				
				self.logger.debug(self.channel,s)

		def exception(self,msg=''):
				"""An error. Logs the message and the last raised exception including
				the traceback."""
				s=string.join(
						traceback.format_exception(
						sys.exc_type, sys.exc_value, sys.exc_traceback, os.linesep)
						)
				if msg:
						s=msg+'\n'+s
				self.error(s)

		def getLogMaster(self):
				return self.logger

def getLogger(name=""):
		"""returns a log adapter object."""
		global theLogger
		
		if theLogger==None:
				prj=Logger()
				
		return LogAdapter(name,theLogger)
