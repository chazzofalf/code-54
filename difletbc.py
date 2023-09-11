import sys
import difletperms
import math
import dumb_bytes
def difletbc_func(name):
	perms=difletperms(name)	
	bs=dumb_bytes(perms)
	return len(bs)-1

class difletbc_callable(sys.modules[__name__].__class__):
	def __call__(self,name):
		return difletbc_func(name)
def main():
	if len(sys.argv) == 2:
		print(difletbc_func(sys.argv[1]))

if __name__ == "__main__":
	main()
else:
	sys.modules[__name__].__class__ = difletbc_callable

