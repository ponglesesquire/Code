#!/usr/bin/env python
"""
Code Copyright (C) 2012-2013 Liam Stanley
Credits: Sean B. Palmer, Michael Yanovich
fun.py - Fun Module
http://code.liamstanley.net/
"""

import random
#from random import randint

def sexymeter(code, input):
    text = input.group().split()
    """.sexymeter <target> - rates <target> on sexiness"""
    if len(text) < 2: return
    nick = text[1]
    try:
        if nick.lower() == code.nick.lower() or input.admin:
            code.say('I rated %s on a scale of 1-100 of sexiness. Result: %s.' % (code.bold('myself'), code.bold('100')))
        else:
            rand = str(random.randint(1,100))
            code.say('Rating %s on a scale of 1-100 of sexiness. Result: %s.' % (code.bold(nick), code.bold(rand)))
    except:
        rand = str(random.randint(1,100))
        code.say('Rating %s on a scale of 1-100 of sexiness. Result: %s.' % (code.bold(input.nick), code.bold(rand)))
sexymeter.commands = ['sm', 'sexymeter']
sexymeter.priority = 'low'
sexymeter.example = '.sexymeter Code'
#sexymeter.rate = 60 because taq is a ugly mofo.

def slap(code, input):
    """.slap <target> - Slaps <target>"""
    text = input.group().split()
    if len(text) < 2 or text[1].startswith('#'): return
    if text[1].lower() == code.nick.lower() or text[1].lower() == 'everyone' or text[1].lower() == 'himself':
        if (input.nick not in code.config.admins):
            text[1] = input.nick
        else: text[1] = 'himself'
    if text[1].lower() in code.config.admins.lower():
        if (input.nick not in code.config.admins):
            text[1] = input.nick

    verb = random.choice(('slaps', 'kicks', 'destroys', 'annihilates', 'punches', \
    'roundhouse kicks', 'rusty hooks', 'pwns', 'owns', 'karate chops', 'kills', \
    'disintegrates', 'demolishes', 'Pulverizes'))
    afterfact = random.choice(('to death', 'out of the channel', \
    'into a hole, till death', 'into mid-air disintegration', \
    'into a pancake'))
    code.write(['PRIVMSG', input.sender, ' :\x01ACTION', verb, text[1], afterfact, '\x01'])
slap.commands = ['slap', 'slaps']
slap.priority = 'medium'
slap.rate = 60
if __name__ == '__main__':
    print __doc__.strip()
