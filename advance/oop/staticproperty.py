class People(object):
    name = 'People'

print(People.name)

p = People()
print(p.name)

p.name = 'ppp'
print(p.name)

del p.name
print(p.name)