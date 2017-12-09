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
        print(x,y)
        x, y = y, x
        print(x, y)

    if z == 1:
        while answer != True:
            a = int(input("Сколько будет {0} {1} {2}\n".format(x, operation, y)))
            if a == operator.add(x,y):
                print("правильно! ")
                sleep(5)
                answer = True
                level1()
            else:
                print("подумай еще... ")
                sleep(2)
                continue
    elif z == 2:
        while answer != True:
            a = int(input("Сколько будет {0} {1} {2}\n".format(x, operation, y)))
            if a == operator.sub(x,y):
                print("правильно! ")
                sleep(5)
                answer = True
                level1()
            else:
                print("подумай еще... ")
                sleep(3)
                continue


# def level2():
#     pass

if level == 1:
    level1()

# elif level == 2:
#     level2()
