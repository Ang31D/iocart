import argparse
from collections import OrderedDict

class CoreSettings:
	def __init__(self, args):
		self.settings = OrderedDict()

class CoreEngine:
	def __init__(self, args):
		self.settings = CoreSettings(args).settings

def main(args):
	core_engine = CoreEngine(args)
	print("test")
	if args.target_path is not None:
		print(args.target_path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description="Magecart Hunter, match content on known regex IOCs.")

	parser.add_argument('-t', dest="target_path", help='Specify target path (URL, FILE) to match IOCs on.')

	args = parser.parse_args()

	main(args)
