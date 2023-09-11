import sys
import encoder
import joiner
class complete_encoder_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,mesg,key):
		return joiner(encoder(mesg,key))	

if __name__=="__main__":
	print(complete_encoder_callable()(bytes(sys.argv[1],encoding='utf8'),sys.argv[2]))
else:
	sys.modules[__name__].__class__ = complete_encoder_callable
