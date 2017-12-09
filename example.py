#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date    : 01-Dec-2017 8:48 PM
# @Authors : Nikolia
# @Python  : 3

from time import sleep
from random import randint
import operator

print("Привет, давай решать примеры.\n"
      "1. уровень простые примеры (сложение и вычитание)\n")
#level = int(input("выбери уровень...\n"))
level = 1


def level1():
    answer = False
    x = randint(1, 10)
    y = randint(1, 10)
    z = randint(1, 2)

    operation = "+" if z == 1 else "-"
    if z == 2 and x < y:
        x, y = y, x

    if z == 1:
        summ = operator.add(x, y)
        while answer != True:
            a = int(input("Сколько будет {0} {1} {2}\n".format(x, operation, y)) or '9999')
            if a == summ:
                print("правильно! ")
                sleep(5)
                answer = True
                level1()
            elif a != summ or a == 9999:
                print("подумай еще... ")
                sleep(2)
                continue
    elif z == 2:
        m = operator.sub(x, y)
        while answer != True:
            s = int(input("Сколько будет {0} {1} {2}\n".format(x, operation, y)) or '9999')
            if s == m:
                print("правильно! ")
                sleep(5)
                answer = True
                level1()
            elif s != m or s == 9999:
                print("подумай еще... ")
                sleep(3)
                continue


# def level2():
#     pass

if level == 1:
    level1()

# elif level == 2:
#     level2()
