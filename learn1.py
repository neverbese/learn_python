#from termcolor import colored
#
#s = []
#for i in range(5):
    #s.append(i)
#print([i for i in s])
#
#a =[1,2,3,5]
#print(a[::-1])
#
#li = reversed(a)
#print(list(li))
#import sys
#
##
##args = sys.argv
##print('-------------')
##print(args[0])
##print(args[1])
##print(args[2])
##print('-------------')
#
#print(sys.argv[0])
#import math
#print('%1.2f' %(3.1415))
#print('%10.5f' %(3.1415))
#print('%11.2f' %(3.1415))

#def ask_ok(prompt, retries=4, complaint='yes or no please'):
    #while True:
        #ok = input(prompt)
        #if ok in ('y', 'yes', 'ye'):
            #return True
        #if ok in ('n', 'no', 'nop', 'nope'):
            #return False
        #retries = retries - 1
        #if retries < 0:
            #raise OSError('########')
        #print(complaint)
#ask_ok('enter:')

#def ask(kind, *arguments, **keywords):
    #print('Do you have any {}'.format(kind))
    #print('i am sorry we are out of {}'.format(kind))
    #for i in arguments:
        #print(i)
    #print('-'*40)
    #keys = sorted(keywords.keys())
    #print(keys)
    #for kw in keys:
        #print(kw, ':', keywords[kw])
#
#ask('wine', 'sorry', 'very much', client='aaa', shopkeeper='bbb')



#parts = [(1, 'one'), (2, 'two'), (4, 'three'), (3, 'four')]
#parts.sort(key=lambda part:part[0])
#print(parts)

#l = [1,2,3] #
##l[len(l):] = [4]#
###
##print(l)#
##print(l[::-1])#
###
##l.pop()#
##print(l)#
##l.pop(2)#
##print(l)#
#p = l + l#
##print(p)#
#s = list(map(lambda x: x**2,range(10)))
#print(s)
#
#s = [i**2 for i in range(10)]
#y = [lambda i: i**2,range(10)]
#print(s)
#print(y)
#for y in range(10):
    #return lambda y : y
#print(len([(x, y) for x in range(3) for y in range(3)]))

#print(type((x, x**2) for x in list(range(11,20))))
#print(list())
#print((range(11,20)))
#print(list(range(11,20)))

#from math import pi
#print([str(round(pi, i)) for i in range(6)])
#
#m = [[1,2,3],[11,12,13],[21,22,23]]
##y = [[row[i] for row in m] for i in range(3)]
##print(y)
#x =[]
#for i in range(3):
    #x.append([row[i] for row in m])
#print(x)    
##
##print(list(zip(*m)))
#t = 1, [1, 3, 3]
#print(t[0], t[1][1])
#t[1][1] = 0
#print(t[0], t[1][1])
#
#empty = ()
#print(type(empty))
#t = 'hello',
#print(len(t))

#s = set()
#print(type(s))
#s1 = set('23423423423423234554')
#s2 =set('999834075')
#
#weekday = ['c', 'a', 'Sat','Mon', 'b', 'Tue', 'Wed']
##food = ['pan', 'noodle', 'niku']
##drink = ['milk', 'beer', 'wine']
##
###r = list(zip(*s))
###print(r)
###for (w, f, d) in (weekday, food, drink):
    ###print(w, f, d)
##s = {}
##for i, day in enumerate(weekday):
    ##print(i, ':', day)
    ##s[i] = day
##print(s)
#
##for i in reversed(range(1,10)):
    ##print(i)
##print([(x ,x ** 2) for x in reversed((range(1,10)))])
#
#for i in sorted(set(weekday)):
    #print(i)

#
#def fib(num):
    #a, b = 0, 1
    #while b < num:
        #print(b, end=' ')
        #a, b = b, a+b
    #print()
#if __name__=='__main__':
    #import sys
    #fib(int(sys.argv[1]))
#23
##
#s = []
#for i in range(5):
    #s = [i]
#print(s)


# input 学習

import os
import numpy as np
from termcolor import cprint 
import colorama

s = []
while True:
    colorama.init()
    cprint('平均と合計を計算するPGです、exitする場合は[end]を入力:', 'green')
    t = input()
    if t == 'end' or t =='End':
        s.append(t)
        cprint('データ入力終了、結果発表:', 'yellow')
        break
    else:
        try:
            t = int(t)
            s.append(t)
        except ValueError:
            cprint('数値を入力してください！！！', 'red')       
print('初期データ:　', s)
s.pop()
print('計算データ: ', s)
print('データ数: ', len(s))
if len(s) > 0:
    print('平均値: ','%0.2f'%np.mean(s))
    print('合計値: ',sum(s))
else:
    cprint('対象データが存在しません')












