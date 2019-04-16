import os
import serial
import adafruit_thermal_printer

uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.64)

printer = ThermalPrinter(uart)

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
                printer.feed(2)
        else:
            to_print = ''

            for s in text:
                if s == 'ä':
                    to_print += chr(0x84)
                if s == 'Ä':
                    to_print += chr(0x8E)
                elif s == 'ö':
                    to_print += chr(0x94)
                elif s == 'Ö':
                        to_print += chr(0x99)
                elif s == 'ü':
                    to_print += chr(0x80)
                elif s == 'Ü':
                        to_print += chr(0x9A)
                elif s == 'ß':
                    to_print += chr(0xE0)
                else:
                    to_print += s


            printer.print(to_print)
    else:
        text = input('Papier muss nachgelegt werden. Frag an der Bar nach.')
        if text == '--quit':
            break
