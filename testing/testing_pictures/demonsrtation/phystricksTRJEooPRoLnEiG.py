# -*- coding: utf8 -*-
from phystricks import *
def TRJEooPRoLnEiG():
    pspict,fig = SinglePicture("TRJEooPRoLnEiG")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    x=var('x')
    P=Point(0,0)

    pspict.DrawGraphs(P)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

----------------
    pspicts,fig = MultiplePictures("TRJEooPRoLnEiG",3)
    pspicts[0].mother.caption="<+caption1+>"
    pspicts[1].mother.caption="<+caption2+>"
    pspicts[2].mother.caption="<+caption3+>"

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    <+Définition des objets+>

    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

------------------------------

    pspicts,figs = IndependentPictures("TRJEooPRoLnEiG",3)

    for psp in pspicts:
        psp.dilatation(1)

    <+Définition des objets+>

    for psp in pspicts:
        psp.DrawDefaultAxes()

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
