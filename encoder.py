import smart_chunker
import shuffle
import sys
class encoder_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,byteslike,key):
		return [shuffle(f,key) for f in smart_chunker(byteslike,key)]

if __name__=="__main__":
	print(encoder_callable()(bytes(sys.argv[1],encoding='utf8'),sys.argv[2]))
else:
	sys.modules[__name__].__class__ = encoder_callable
