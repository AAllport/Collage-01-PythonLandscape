"""
Project: Collage-01-PythonLandscape
File: units
Author: Adam Allport<adam@allport.me.uk>
Description: unit conversion lib
Licence: GPLv3
"""


def vu2px(screen, units):
    """ Returns the px's for a vertical unit (25ths of height)"""
    return int((screen.window_height() / 25) * units)


def wu2px(screen, units):
    """ Returns the px's for a horizontal unit (50ths of width)"""
    return int((screen.window_width() / 50) * units)
