import copy

from diff_commands import *

def myers_default_patch(private_data, result, command, editscript):
		index = editscript[2]
		if command == delete_command:
				result.pop(index) 
		elif command == insert_command:
				value = editscript[1]
				result.insert(index, value)
		else:
				assert(0)

def myers_patch(editscript, original, reverse = 0, func_to_update = myers_default_patch, private_data = None):
		"""Patches a list, given the editscript. If reverse is set, then
		original is assumed to be the _result_, and editscript is applied
		in reverse.

		func_to_update is the address of a function that takes three
		parameters: the private_data, the resulting array, the command,
		index, and value (available only for insert commands)
		"""

		print "MYERS PATCH"
		print original
		print editscript

		result = copy.copy(original)
		_editscript = copy.copy(editscript)

		inscmd = "ins"
		delcmd = "del"

		if reverse:
				_editscript.reverse()
				inscmd, delcmd = delcmd, inscmd
				
		for e in _editscript:
				command = e[0]
				if command == delcmd:
						#result.pop(index)
						func_to_update(private_data, result, delete_command, e)
				elif command == inscmd:
						#result.insert(index, value)
						func_to_update(private_data, result, insert_command, e)
				else:
						assert(0)
						
		return result
		

