import sys
import splitter
import decoder
class complete_decoder_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,ciphertext,key):
		return decoder(splitter(ciphertext,key),key)

if __name__=="__main__":
	print(complete_decoder_callable()(sys.argv[1],sys.argv[2]))
else:
	sys.modules[__name__].__class__ = complete_decoder_callable
