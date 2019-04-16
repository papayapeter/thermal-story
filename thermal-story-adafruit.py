# zeno gries
# thermal story
# 2019
# adafruit library version (no ä, ö, ü, ß)

import os
import serial
import adafruit_thermal_printer
import re

# establish objects
uart = serial.Serial('/dev/serial0', baudrate=9600, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.64)

printer = ThermalPrinter(uart)

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
        if text == '--test': # print test page
            printer.test_page()
            printer.feed(2)
        elif text == '--quit': # quit program
            break
        elif text == '--feed': # feed to lines of paper
            printer.feed(2)
        elif text == '--clear': # clear all logs
                os.remove('log.txt')
        else: # print
            # sort out unsupported characters
            to_print = ''
            to_print = re.sub(r'[^\x00-\x7F]', '#', text)

            # write to log and print
            log = open('log.txt', 'a+')
            log.write(to_print + '\n')
            log.close()

            printer.print(to_print)
    else: # if there is no paper then print that or quit
        text = input('Papier muss nachgelegt werden. Frag an der Bar nach.')
        if text == '--quit':
            break
