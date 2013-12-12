import log
#log = log.log
log = log.none

class Path(list):
  def __init__(self, l = []):
    list.__init__(self, l)

  def __hash__(self):
    h = hash(sum(map(hash, self)))
    log("HASH", self, h)
    return h

  def __eq__(self, other):
    log("EQ", self, other)
    return hasattr(other, '__iter__') and len(self) == len(other) and len(filter(lambda (x, y): x != y, zip(self, other))) == 0

  def __add__(self, other):
    return Path(list.__add__(self, other))

class PrefixTree(dict):
  def __init__(self, d = {}):
    dict.__init__(self)
    self.update(d)

  def __setitem__(self, path, value):
    log("PATH", path, "VALUE", value)

    assert(hasattr(path, '__iter__'))

    if len(path) == 1 and not isinstance(value, dict):
      log("LEAF", path, "VALUE", value)
      if(path[0] in self): raise KeyError("Cannot update leaf, delete leaf first")
      dict.__setitem__(self, path[0], value)
      return

    if len(path) == 0:
      log("DICT", path, "VALUE", value)
      assert(isinstance(value, dict))
      dict.update(self, value)
    
    if len(path) > 0:
      log("RECR", path, "VALUE", value)
      key = path[0]
      if not key in self: dict.__setitem__(self, key, PrefixTree())
      self[key][path[1:]] = value

  def update(self, other):
    log("UPDT", other)
    for (k, v) in other.items():
      self[k] = v
