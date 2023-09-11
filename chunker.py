import sys
import math
import dumb_bytes
import diflet
class chunker_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,byteslike,key):
		my_cards=diflet(key)
		max_value=math.factorial(len(my_cards))-1
		dumb_max_value=dumb_bytes(max_value)
		max_len=len(dumb_max_value)-1
		chunksize=max_len
		chunks=[]
		byteslikerw=byteslike
		while len(byteslikerw) > 0:
			chunks.append(bytes(byteslikerw[:chunksize]))
			byteslikerw = byteslikerw[chunksize:]
		return	chunks

if __name__=="__main__":
	print(chunker_callable()(bytes(sys.argv[1],encoding='utf8'),sys.argv[2]))
else:
	sys.modules[__name__].__class__ = chunker_callable
