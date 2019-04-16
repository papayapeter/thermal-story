# zeno gries
# thermal story
# 2019
# loupio library version

import os
from printer import *

# establish objects
printer = ThermalPrinter()

# open file once (to make sure it is there)
log = open('log.txt', 'a+')
log.close()

# main loop
while (True):
    # clear screen
    os.system('clear')

    # check for paper
    if printer.has_paper():
        # print intruction
        print('Schreib die Geschichte weiter.\n\n')
        # print story so far line by line
        for line in open('log.txt'):
            print(line)
        # wait for input
        text = input("> ")

        # sort out special commands
        if text == '--quit': # quit program
            break
        elif text == '--feed': # feed to lines of paper
            printer.linefeed(2)
        elif text == '--clear': # clear all logs
                os.remove('log.txt')
        else: # print
            # write to log and print
            log = open('log.txt', 'a+')
            log.write(text + '\n')
            log.close()

            printer.print_text(text)
    else: # if there is no paper then print that or quit
        text = input('Papier muss nachgelegt werden. Frag an der Bar nach.')
        if text == '--quit':
            break
