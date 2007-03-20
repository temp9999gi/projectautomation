#!/usr/bin/env python

#__all__ = ["echo", "surround", "reverse"]

__all__ = []

for subpackage in ['A', 'B', 'C']:
	try: 
		exec 'import ' + subpackage
		__all__.append( subpackage )
	except ImportError:
		pass
