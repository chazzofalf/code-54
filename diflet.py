import sys
def diflet_func(name):
	already_called_letters = []
	for letter in name:
		if letter not in already_called_letters:
			already_called_letters.append(letter)
	return already_called_letters

class diflet_callable(sys.modules[__name__].__class__):
	def __call__(self,name):
		return diflet_func(name)
def main():
	if len(sys.argv) == 2:
		print(diflet_func(sys.argv[1]))



if __name__ == "__main__":
	main()
else:
	sys.modules[__name__].__class__ = diflet_callable
