import sys
import get_scramble
# alias for get_scramble
class shuffle_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,idx,key):
		return get_scramble(idx,key)

if __name__=="__main__":
	print(shuffle_callable()(int(sys.argv[1]),sys.argv[2]))
else:
	sys.modules[__name__].__class__ = shuffle_callable
