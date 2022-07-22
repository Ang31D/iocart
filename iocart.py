import argparse
from collections import OrderedDict
import os
import pathlib

class IOC_Repository:
	FILE = "file"
	URL = "url"
	UNKNOWN = "unknown"

class CoreSettings:
	def __init__(self, args):
		self.settings = OrderedDict()
		self.settings['ROOT_DIR'] = str(pathlib.Path(os.path.realpath(__file__)).parent)
		self.settings['REPOSITORY_DIR'] = str(os.path.join(self.settings['ROOT_DIR'], "repos"))
		self.settings['REPOSITORY_FILE'] = str(os.path.join(self.settings['ROOT_DIR'], "repositories.txt"))
		self.settings['REPOSITORY_FILE'] = CommonUtils.absolute_to_relative_path(self.settings['ROOT_DIR'], self.settings['REPOSITORY_FILE'])

		self.settings['Target_Path'] = None
		self.settings['Target_Type'] = IOC_Repository.UNKNOWN

		self.settings['Log_Info'] = True
		self.settings['Verbose_Mode'] = False
		self.settings['Extra_Verbose'] = False
		self.settings['Debug'] = False

	def _init_settings_by_args(self, args):
		if args.target_path is not None:
			self.settings['Target_Path'] = args.target_path
			if self.settings['Target_Path'].startswith("http"):
				self.settings['Target_Type'] = IOC_Repository.URL
			elif os.path.isfile(self.settings['Target_Path']):
				self.settings['Target_Type'] = IOC_Repository.FILE

		if args.no_log_info:
			self.settings['Log_Info'] = False
		self.settings['Verbose_Mode'] = args.verbose_mode
		self.settings['Extra_Verbose'] = args.extra_verbose
		if self.settings['Extra_Verbose']:
			self.settings['Verbose_Mode'] = True
		self.settings['Debug'] = args.debug
class CoreEngine:
	def __init__(self, args):
		self.settings = CoreSettings(args).settings

def main(args):
	core_engine = CoreEngine(args)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description="Magecart Hunter, match content on known regex IOCs.")

	parser.add_argument('-t', dest="target_path", help='Specify target path (URL, FILE) to match IOCs on.')
	parser.add_argument('-v', dest="verbose_mode", action='store_true', help='Enable verbose mode. Output value on matching IOC.')
	parser.add_argument('-vv', dest="extra_verbose", action='store_true', help='Enable extra verbose mode. Output info on repo, identity for matching IOC.')
	parser.add_argument('--debug', dest="debug", action='store_true', help='Log debugging information.')
	parser.add_argument('--no-info', dest="no_log_info", action='store_true', help='Disable informational logging.')

	args = parser.parse_args()

	main(args)
