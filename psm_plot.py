from math import *
import numpy as np
import matplotlib.pyplot as plt

"""
UCO PSM Plotting Library

Form of functions are:

xxyyzzPlot###

xxyyzz = Plot type (Line, Scatter, etc...)

Multiple types are meant to be series on a single plot... arguments are in this same order

### =

first digit = # of rows
second digit = # of cols
third digit = # of series per plot

Arguments are in row, then column order

"""
#

def LinePlot111(x,y,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    plt.ylim(min(y), max(y))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(x,y)
    plt.savefig(filename)
    plt.show()

def ScatterPlot111(x,y,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    plt.ylim(min(y), max(y))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.scatter(x,y)
    plt.savefig(filename)
    plt.show()

def TwoLineColorsPlot111(x,y1,y1label,y2,y2label,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    plt.ylim(ymin, ymax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.plot(x,y1,c='r',label=y1label)
    plt.plot(x, y2, c='b', label=y2label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def ThreeLineColorsPlot111(x,y1,y1label,y2,y2label,y3,y3label, xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.plot(x,y1,c='r',linestyle="-",label=y1label)
    plt.plot(x, y2, c='b', linestyle="--", label=y2label)
    plt.plot(x, y3, c='g', linestyle=":", label=y3label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def FourLineColorsPlot111(x,y1,y1label,y2,y2label,y3,y3label, y4, y4_label, xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.plot(x,y1,c='r',linestyle="-",label=y1label)
    plt.plot(x, y2, c='b', linestyle="--", label=y2label)
    plt.plot(x, y3, c='g', linestyle=":", label=y3label)
    plt.plot(x, y4, c='k', linestyle="-", label=y3label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def FiveLineColorsPlot111(x,y1,y1label,y2,y2label,y3,y3label, y4, y4label, y5,y5label, xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.plot(x,y1,c='r',linestyle="-",label=y1label)
    plt.plot(x, y2, c='b', linestyle="--", label=y2label)
    plt.plot(x, y3, c='g', linestyle=":", label=y3label)
    plt.plot(x, y4, c='k', linestyle="-", label=y4label)
    plt.plot(x, y5, c='m', linestyle="--", label=y5label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()



def TwoDictLinePlot111(x,y1,y2,datakeys1,datakeys2,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    line_colors = ['b', 'g', 'r','c','m','y','k']
    line_styles = ['-',':','-.','--']
    linestyle_counter=0
    color_counter = 0
    for i, list_item in enumerate(datakeys1):
        list_item2=datakeys2[i]
        plt.plot(x[list_item],y1[list_item],c=line_colors[color_counter],linestyle='-',label=list_item)
        linestyle_counter += 1
        plt.plot(x[list_item], y2[list_item2], c=line_colors[color_counter], linestyle='--',label=list_item2)
        color_counter += 1
        if color_counter >= len(line_colors):
            color_counter = 0

    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()



def DictLinePlot111(x,y,datakeys,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    line_colors = ['b', 'g', 'r','c','m','y','k']
    line_styles = ['-',':','-.','--']
    linestyle_counter=0
    color_counter = 0
    loop_counter = 0
    for list_item in datakeys:
        plt.plot(x[list_item],y[list_item],c=line_colors[color_counter],linestyle=line_styles[linestyle_counter],label=list_item)
        if color_counter >= len(line_colors):
            linestyle_counter += 1
            color_counter = 0
        else:
            color_counter += 1
        loop_counter+=1

    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()



def LineScatterPlot111(x,y1,y2,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    plt.ylim(ymin, ymax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(x,y1)
    plt.scatter(x,y2)
    plt.savefig(filename)
    plt.show()


def LinePlot211(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(211)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(212,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    plt.savefig(filename)
    plt.show()

def LinePlot121(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(121)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(122,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    plt.savefig(filename)
    plt.show()



def LinePlot311(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(311)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(312,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.ylabel(y2label)
    plt.plot(x, y2)

    ax3 = plt.subplot(313,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.plot(x, y3)

    plt.savefig(filename)
    plt.show()

def LinePlot131(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(131)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(132,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    ax3 = plt.subplot(133,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.plot(x, y3)
    plt.savefig(filename)
    plt.show()





def ScatterPlot211(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(211)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(212,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    plt.savefig(filename)
    plt.show()

def ScatterPlot121(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(121)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(122,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    plt.savefig(filename)
    plt.show()



def ScatterPlot311(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(311)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(312,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    ax3 = plt.subplot(313,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.scatter(x, y3)

    plt.savefig(filename)
    plt.show()

def ScatterPlot131(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(131)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(132,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    ax3 = plt.subplot(133,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.scatter(x, y3)
    plt.savefig(filename)
    plt.show()




"""
    plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    plt.ylim(ymin, ymax)
    """