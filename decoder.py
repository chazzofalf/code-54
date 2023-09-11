import unshuffle
import dumb_dechunker
import sys
import ast
class decoder_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,decks,key):
		return dumb_dechunker([unshuffle(f,key) for f in decks])

if __name__=="__main__":
	print(decoder_callable()(ast.literal_eval(sys.argv[1]),sys.argv[2]))
else:
	sys.modules[__name__].__class__ = decoder_callable
