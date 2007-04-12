# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start

import logging

#create logger with "app_name"
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

#create file handler and set level to debug
fh = logging.FileHandler("app.log")
fh.setLevel(logging.DEBUG)

#create console handler and set level to error
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

#create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#add formatter to fh
fh.setFormatter(formatter)
#add formatter to ch
ch.setFormatter(formatter)
#add fh to logger
logger.addHandler(fh)
#add ch to logger
logger.addHandler(ch)

import sys, types
# import logging
# log = logging.getLogger('ExcelMain')

class LoggerAspect(object):

	def __init__(self, method):
		self.method = method

	def before(self,*args, **kwargs):
		#logger.debug("argv0: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
		logger.debug("before: self.method : ['%s']",self.method)
		logger.debug("        args        : ['%s']",args)

	def after(self, retval, aException, *args, **kwargs):
		if aException:
##			print exc
##			print args, kwargs
			logger.error("after: self.method : ['%s']",self.method)
			logger.error("       args        : ['%s']",args)
			logger.error("       kwargs      : ['%s']",kwargs)
			logger.error("       aException  : ['%s']",aException)
		else:
			logger.debug("after: self.method : ['%s']",self.method)
			logger.debug("       args        : ['%s']",args)

def weave_method(method, advice_class, *advice_args, **advice_kwargs):
	advice = advice_class(method, *advice_args, **advice_kwargs)
	advice_before = advice.before
	advice_after = advice.after

	def invoke_advice(*args, **kwargs):
		advice_before(*args, **kwargs)
		try:
			retval = method(*args, **kwargs)
		except Exception, e:
			advice_after(None, e, *args,**kwargs)
			raise
		else:
			advice_after(retval, None, *args,**kwargs)
			return retval

	try:
		class_ = method.im_class
	except:
		method.func_globals[method.func_name] = invoke_advice
	else:
		setattr(class_, method.__name__, invoke_advice) #setattr( object, name, value)

	return invoke_advice


def weave(): #weave <피륙을> 짜다, 뜨다, 엮다, 치다
	frame = sys._getframe(1) #Return a frame object from the call stack.
	for k,v in frame.f_locals.items():
		if not k.startswith('__'):
			#if not isinstance(v, types.FunctionType) and not isinstance(v, types.ModuleType):
			if isinstance(v, types.ClassType):
				_class_weave(v)

def weaveAtionForClass(inClass): #weave <피륙을> 짜다, 뜨다, 엮다, 치다
	for k in inClass:
		#if not isinstance(v, types.FunctionType) and not isinstance(v, types.ModuleType):
		if isinstance(k, types.ClassType):
			_class_weave(k)

def _class_weave(clazz):
	for key, value in clazz.__dict__.items():
		if not key.startswith('__') and isinstance(value, types.FunctionType):
			#logging example
			weave_method(getattr(clazz, key), LoggerAspect)

