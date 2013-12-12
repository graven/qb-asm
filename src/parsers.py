import yaml, os

class clob(str):
  pass

def parse(fpath):
  def p_yaml(fpath):
    import yaml
    return yaml.load(open(fpath))

  def p_clob(fpath):
    return clob(open(fpath).read())

  parsers = {
    "yml": p_yaml,
    "yaml": p_yaml,
    "json": p_yaml,
  }

  ext = fparts(fpath)[1]
  parser = p_clob if ext == [] or not ext in parsers.keys() else parsers[ext]
  return parser(fpath)

def fparts(path):
  bname = os.path.basename(path)
  idx = bname.rfind('.')
  return (bname, '') if idx < 0 else (bname[:idx], bname[idx+1:])