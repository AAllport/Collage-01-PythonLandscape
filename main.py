"""
Project: Collage-01-PythonLandscape
Author: Adam Allport<adam@allport.me.uk>
Description: Using Python to create a landscape silhouette
Licence: GPLv3
"""

import turtle


def main():
    """ Main program function, Draws silhouette"""
    charles = turtle.Turtle()
    screen = charles.screen


def vunits2px(scrn, units):
    """ Returns the px's for a vertical unit (25ths of height)"""
    return (scrn.window_height() / 25) * units


def wunits2px(scrn, units):
    """ Returns the px's for a vertical unit (50ths of width)"""
    return (scrn.window_width() / 50) * units


if __name__ == "__main__":
    main()
