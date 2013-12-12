import log
log = log.log

import os
from ptree import Path

def find(sysbase, parse, path = Path(), scope = {}):
  def ospath(p):
    import string
    return string.join([sysbase] + p, os.sep) 

  import string
  if os.path.isdir(ospath(path)):
    for node in os.listdir(ospath(path)):
      log("PATH", ospath(path + [node]))
      scope[path] = {}
      find(sysbase, parse, path + [node], scope)
  else:
    # get rid of the file extension
    fname = fparts(path[-1])[0]
    fixpath = Path(path[:-1] + [fname]) if len(path) > 0 else path
    scope[fixpath] = parse(ospath(path))
  return scope

def fparts(path):
  bname = os.path.basename(path)
  idx = bname.rfind('.')
  return (bname, '') if idx < 0 else (bname[:idx], bname[idx+1:])