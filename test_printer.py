# -*- coding: utf-8 -*-
from xmlescpos.exceptions import *
from xmlescpos.printer import Usb
from flask import Flask,request, make_response

import usb
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)
printer = Usb(0x0483,0x070b,0,0x81,0x02)
def printtest(test_temp):
    temp="<div>"+test_temp+"</div>"
    printer.receipt(temp)
#printtest("123")
#printer.receipt(u"<div>n你</div>")
#    pp.pprint(printer.get_printer_status())

