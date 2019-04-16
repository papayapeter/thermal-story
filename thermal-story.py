import os
import serial
import adafruit_thermal_printer
import re

uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.64)

printer = ThermalPrinter(uart)

log = open('log.txt', 'a+')

while (True):
    os.system('clear')
    print('Schreib die Geschichte weiter.')

    if printer.has_paper():
        text = input("> ")

        if text == '--test': # print test page
            printer.test_page()
            printer.feed(2)
        elif text == '--quit': # quit program
            break
        elif text == '--feed': # feed to lines of paper
            printer.feed(2)
        elif text == '--clear': # clear all logs
                log.close()
                os.system('rm -rf log.txt')
                log = open('log.txt', 'a+')
        else:
            to_print = ''

            to_print = re.sub(r'[^\x00-\x7F]', '_', text)

            log.write(text + '\n')
            printer.print(to_print)
    else:
        text = input('Papier muss nachgelegt werden. Frag an der Bar nach.')
        if text == '--quit':
            break

log.close()
