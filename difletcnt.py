import sys
def difletcnt_func(name):
	already_called_letters = []
	for letter in name:
		if letter not in already_called_letters:
			already_called_letters.append(letter)
	return len(already_called_letters)

class difletcnt_callable(sys.modules[__name__].__class__):
	def __call__(self,name):
		return difletcnt_func(name)
def main():
	if len(sys.argv) == 2:
		print(difletcnt_func(sys.argv[1]))



if __name__ == "__main__":
	main()
else:
	sys.modules[__name__].__class__ = difletcnt_callable
