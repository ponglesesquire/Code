#!/usr/bin/env python
"""
Code Copyright (C) 2012-2013 Liam Stanley
Credits: Sean B. Palmer, Michael Yanovich
ask.py - Code Ask Module
http://code.liamstanley.net/
"""

import random, time
import re

def ask(code, input):
    """.ask <item1> or <item2> or <item3> - Randomly picks from a set of items seperated by ' or '."""

    choices = input.group(2)
    random.seed()

    if choices == None:
        code.reply("Please try a valid question.")
    elif choices.lower() == "what is the answer to life, the universe, and everything?":
        code.reply("42")
    else:
        list_choices = choices.split(" or ")
        if len(list_choices) == 1:
            code.reply(random.choice(['yes', 'no']))
        else:
            choices = choices.replace('?','')
            choices = choices.replace('!','')
            code.reply((random.choice(list_choices)).encode('utf-8'))
ask.commands = ['ask']
ask.priority = 'low'
ask.example = '.ask today or tomorrow or next week'

def rand(code, input):
    """.rand <arg1> <arg2> - Generates a random integer between <arg1> and <arg2>."""
    if input.group(2) == " " or not input.group(2):
        code.say("I'm sorry, " + str(input.nick) + ', but you must enter at least one number.')
    else:
        random.seed()
        li_integers = input.group(2)
        li_integers_str = li_integers.split()
        if len(li_integers_str) == 1:
            li_integers_str = re.sub(r'\D', '', str(li_integers_str))
            if len(li_integers_str) > 0:
                if int(li_integers_str[0]) <= 1:
                    a = li_integers_str
                    a = int(a)
                    if a < 0:
                        randinte = random.randint(a, 0)
                    if a > 0:
                        randinte = random.randint(0, a)
                else:
                    a = li_integers_str
                    a = int(a)
                    randinte = random.randint(0, a)
                code.say(str(input.nick) + code.color('lime', ': your random integer is: ') + str(randinte))
            else:
                code.reply(code.bold('lolwut'))
        else:
            ln = li_integers.split()
            if len(ln) == 2:
                a, b = ln
                a = re.sub(r'\D', u'', a)
                b = re.sub(r'\D', u'', b)
                if not a:
                    a = 0
                if not b:
                    b = 0
                a = int(a)
                b = int(b)
                if a <= b:
                    randinte = random.randint(a, b)
                else:
                    randinte = random.randint(b, a)
                code.say(str(input.nick) + ': your random integer is: ' + str(randinte))
            else:
                code.reply(code.color('red', 'I\'m not sure what you want me to do!'))

rand.commands = ['rand']
rand.priority = 'medium'


if __name__ == '__main__':
    print __doc__.strip()
