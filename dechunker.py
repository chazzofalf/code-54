import sys
import ast
class dechunker_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,chunks):
		out=bytearray([])
		for chunk in chunks:
			out.extend(chunk)
		return bytes(out)

if __name__=="__main__":
	print(dechunker_callable()(ast.literal_eval(sys.argv[1])))
else:
	sys.modules[__name__].__class__ = dechunker_callable
