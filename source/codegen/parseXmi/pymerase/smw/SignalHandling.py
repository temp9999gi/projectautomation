#
# General system for emitting and receiving signals.
#

from smw import log

logger = log.getLogger("SignalHandling.py")

signalEmitters = {}

def registerSignalEmitter(name):
		if signalEmitters.has_key(name):
				logger.info("Already have signal emitter %s" % name)
		else:
				signalEmitters[name] = []

#### Signal emitters are never unregistered
#def unregisterSignalEmitter(name):
#		if not signalEmitters.has_key(name):
#				logger.warning("Don't have signal emitter %s" % name)
#		else:
#				del signalEmitters[name]

def emit(name, params = None):
		"""Emits the signal with the given parameters. The signal name
		is the first parameter, the rest are given by the emitter itself."""
		# Note, it's a good idea to use dictionaries for parameter passing.
		if params == None:
				params = {}
		for (i, privateparams) in signalEmitters[name]:
				i(name, privateparams, params)

def registerReceiver(name, func, privateparams = None):
		registerSignalEmitter(name)
		assert(not func in map(lambda x: x[0], signalEmitters[name]))
		signalEmitters[name].append((func, privateparams))

def unregisterReceiver(name, func):
		registerSignalEmitter(name)
		assert(func in map(lambda x: x[0], signalEmitters[name]))
		for i in range(signalEmitters[name]):
				if signalEmitters[name][i][0] == func:
						signalEmitters[name].pop(i)
						break

		assert(not func in map(lambda x: x[0], signalEmitters[name]))
