import smart_bytes
import chunker
import sys
class smart_chunker_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,byteslike,key):
		return [smart_bytes(f) for f in chunker(byteslike,key)]


if __name__=="__main__":
	print(smart_chunker_callable()(bytes(sys.argv[1],encoding='utf8'),sys.argv[2]))
else:
	sys.modules[__name__].__class__ = smart_chunker_callable
