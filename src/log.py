import pprint

printer = pprint.PrettyPrinter(indent=2)
def log(*x):
  printer.pprint(x)

def none(*x):
	pass