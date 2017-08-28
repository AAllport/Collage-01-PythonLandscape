"""
Project: Collage-01-PythonLandscape
Author: Adam Allport<adam@allport.me.uk>
Description: Using Python to create a landscape silhouette
Licence: GPLv3
"""

import turtle
import units


def main():
    """ Main program function, Draws silhouette"""
    charles = turtle.Turtle()
    screen = charles.screen
    charles.penup()
    charles.goto(-screen.window_width() / 2, -screen.window_height() / 2)
    charles.setheading(0)
    charles.pendown()
    charles.speed(100)

    turtle.done()


if __name__ == "__main__":
    main()
