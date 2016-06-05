
# -*- coding: utf-8 -*-


def main(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


#test = u'éáé123456tgreáé@€æ'
#print test

