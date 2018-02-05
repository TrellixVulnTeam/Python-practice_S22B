#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


class Timer(object):
    def run(self):
        print('Start...')

def run_run(animal):
    animal.run()


cat = Cat()
timer = Timer()

run_run(cat)
run_run(timer)

