# -*- coding: utf-8 -*-
s1 = {
    'name': 'S1',
    'score': 11
}
s2 = {
    'name': 'S2',
    'score': 22
}

def log(std):
    print('%s: %s' %(std['name'], std['score']))

log(s2)