from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *


#Mod3.1 Exercise 1
#W = white-tip shark (WTS) pop. (# if item)
#B = black-tip shark (BTS) pop. (# if item)
#W_0 initial population at time t_0
#B_0 initial population at time t_0
W_0=20
B_0=15
W = [W_0]
B=[B_0]
#t_0 = start time
t_0=0   #months
t = [t_0]
delta_t=0.001    #months
t_max = 5      #months
#above t_max was tweaked until graph showed p going to zero... so answer is 0.84 hours

W_birth_rate = 1
B_birth_rate = 1
#b competition death rate (per WTS and per BTS) of BTS due to WTS
b = 0.20
#w competition death rate (per WTS and per BTS) of WTS due to BTS
w = 0.27

W_curr = 0.0
B_curr = 0.0
t_curr = 0.0
delta_W = 0.0
delta_B = 0.0
counter=0

while t[counter] < t_max:
    counter+=1                              #increment counter (0->1 on first trip through
    t_curr=t[counter-1]+delta_t             #get the current time by adding delta_t
    t.append(t_curr)                        #add this time to the time list
    W_birth = W_birth_rate*W[counter-1]
    W_death = w*B[counter-1]*W[counter-1]
    W_curr = W[counter-1]+(W_birth-W_death)*delta_t
    W.append(W_curr)

    B_birth = B_birth_rate*B[counter-1]
    B_death = b*W[counter]*B[counter-1]
    B_curr = B[counter-1]+(B_birth-B_death)*delta_t
    B.append(B_curr)
    #print t
    #print W
    #print B

title_base = "WTS and BTS Pop."
title = title_base + " delta_t = " + str(delta_t)
filename = "wts_bts_mod41_pop_" + str(delta_t) + ".png"
xlabel = "t (months)"
ylabel = "Number of of sharks"
W_label = "WTS"
B_label = "BTS"

TwoLineColorsPlot111(t,W,W_label,B,B_label,xlabel,ylabel,title,filename)


