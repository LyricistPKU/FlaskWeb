# -*- encoding=UTF-8 -*-
import requests
import random
import re
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = "hello world"
    print stra.capitalize()
    print stra.replace('w', 'W')
    strb = '  \n\rhello world \r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 5, len(stra)
    print 7, '-'.join([stra, strb, strc])
    print 8, strc.split(' ')


def demo_operation():
    x = 2
    y = 2.3
    print x, y, type(x), type(y)


def demo_buildinfunction():
    print 1, max(2, 1), min(3, 5)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-2)  # fabs,Math.fabs
    print 4, range(1, 10, 3)
    print 5, dir(list)  # print all functions in list module
    x = 2
    print 6, eval('x + 3')
    print 7, chr(65), ord('a')  # chr transition from ascii code to char, ord is the opposite
    print 8, divmod(11, 3)


def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10
    # for (int i = 0; i < 10; ++i)
    # continue ,break, pass
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do_special
            # print 3, i
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break


def demo_list():
    lista = [1, 2, 3]  # vector<int> Arraylist
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb
    print 6, lista
    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)    # pop(element)
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)    # sort by reverse order
    print 12, listb
    print 13, listb * 2
    print 14, [0] * 14  # memset(src, 0, len)
    tuplea = (1, 2, 3)
    listaa = [1, 2, 3]
    listaa.append(4)
    print 15, listaa


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1)
    for k, v in dicta.items():
        print 'key-value', k, v
    dictb = {'+': add, '-': sub}
    print 4, dictb['+'](1, 2)
    print 5, dictb['-'](1, 2)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(4)
    print 6, dicta
    del dicta[1]
    print 7, dicta

if __name__ == '__main__':
    print 'hello world'
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    demo_dict()

