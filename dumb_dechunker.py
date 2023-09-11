import sys
import dechunker
import dumb_bytes
import ast
class dumb_dechunker(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,smart_chunks):
		return bytes([x for f in smart_chunks for x in dumb_bytes(f)])

if __name__=="__main__":
	print(dumb_dechunker()(ast.literal_eval(sys.argv[1])))
else:
	sys.modules[__name__].__class__ = dumb_dechunker
