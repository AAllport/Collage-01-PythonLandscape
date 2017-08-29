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
    charles.speed(1000)
    for i in range(units.wu2px(screen, 45)):
        draw_peak(charles, units.vu2px(screen, 10))
    turtle.done()


def draw_peak(drawer, height):
    """ Draws a line with height """
    drawer.left(90)
    drawer.forward(height)
    drawer.right(90)
    drawer.forward(1)
    drawer.right(90)
    drawer.forward(height)
    drawer.left(90)


if __name__ == "__main__":
    main()
