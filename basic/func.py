def add(x, y):
  return x+y;
print(add(1,2));

# =================================================
def check(x):
  if not isinstance(x, (int, float, list)):
    raise TypeError('not int or float');
  print('int or float');
check([1])

# =================================================
def multiReturnVal(x, y):
  a = x+y;
  b = x-y;
  return a, b;
a, b = multiReturnVal(11,22);
print(a);

# =================================================
def log(a, b=11, c='cc'):
  print(a, b, c);
log(1)

# =================================================
def ff(l=None):
  if l is None:
    l = [];
  l.append('default');
  print(l);
ff()
ff()
ff()

# =================================================
def calc(a,b,*nums):
  sum = 0;
  for n in nums:
    sum += n;
  print(sum);
calc(1,2,3)

# =================================================
def keyArgs(a, b, **m):
  if 'name' in m:
    print('has name');
  if 'age' in m:
    print('has age');
  print(m);
keyArgs(1, 2, name='czg', age=25);

# =================================================
def namekeyArgs(a, b, *, name, age):
  print(a, b, name, age);
namekeyArgs(1, 2, name='zhiguang', age='33');

