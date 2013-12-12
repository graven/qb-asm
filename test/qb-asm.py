# THIS IS ONLY A TEST FILE TO TEST THE CLOB PARSER

import log
log = log.log

import sys, fs, parsers
paths = fs.find(sys.argv[1], parsers.parse)

from ptree import Path, PrefixTree

# expand dots into real paths
# replace with identity to disable
def exp_path(path):
  import string
  return path if path == [] else Path(reduce(list.__add__, map(lambda s: string.split(s, '.'), path)))
  
tree = PrefixTree({ exp_path(k): v for (k, v) in paths.items() })
# log(tree)

import yaml

def literal_presenter(dumper, data):
  return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

def dict_presenter(dumper, data):
  return dumper.represent_mapping('tag:yaml.org,2002:map', data.items())

yaml.add_representer(parsers.clob, literal_presenter)
yaml.add_representer(PrefixTree, dict_presenter)

yaml.safe_dump(tree, sys.stdout, default_flow_style=False)