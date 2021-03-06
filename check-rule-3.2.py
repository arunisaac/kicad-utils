#!/usr/bin/env python
# -*- coding: utf-8 -*-

from schlib import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('libfiles', nargs='+')
parser.add_argument('-v', '--verbose', help='Print output for all pins - violating or not', action='store_true')
args = parser.parse_args()

def select_violating_pins(pins):
    violating_pins = []
    for pin in pins:
        length = int(pin['length'])
        if (length < 100) or (length - 100) % 50 != 0:
            violating_pins.append(pin)
    return violating_pins

for libfile in args.libfiles:
    lib = SchLib(libfile)
    print 'library: %s' % libfile

    for component in lib.components:
        violating_pins = select_violating_pins(component.pins)
        if len(violating_pins) > 0:
            print '\tcomponent: %s' % component.name
            for pin in violating_pins:
                print '\t\tpin: %s (%s), dir: %s, length: %s' % (pin['name'], pin['num'], pin['direction'], pin['length'])
        else:
            if args.verbose:
                print '\tcomponent: %s......OK' % component.name
