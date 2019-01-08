def log(func):
  def warpper(*args, **kv):
    print('call: ' + func.__name__);
    return func(*args, **kv);
  return warpper;

@log
def now():
  print('1010110');


now();