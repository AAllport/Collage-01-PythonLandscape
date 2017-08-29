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
    template = [10, 10, 0, 8, 8, 0, 20, 18, 25, 18, 20, 0, 10, 10, 10, 0, 21, 22, 24, 22, 21, 0, 12, 14, 12, 0, 18, 16,
                20, 0, 20, 22, 24, 0, 0, 8, 8, 7, 8, 7, 10, 12]
    charles = turtle.Turtle()
    screen = charles.screen
    charles.penup()
    charles.goto(-screen.window_width() / 2, -screen.window_height() / 2)
    charles.setheading(0)
    charles.pendown()
    charles.speed(1000)
    for h in template:
        draw_bar_u(screen, charles, 1, h)
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


def draw_bar_u(screen, drawer, width, height):
    for i in range(units.wu2px(screen, width)):
        draw_peak(drawer, units.vu2px(screen, height))


if __name__ == "__main__":
    main()
