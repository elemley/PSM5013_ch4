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

#t_0 = start time

t_0=0   #months
delta_t=[0.05, 0.005, 0.001, 0.0005, 0.0001, .00005]    #months
t_max = 5      #months

t={}
W={}
B={}

t["label"]="t (months)"
W["label"]="WTS Pop."
B["label"]="BTS Pop."

list_names_W = []
for item in delta_t:
    series_label = str(item)+" WTS"
    list_names_W.append(series_label)

list_names_B = []
for item in delta_t:
    series_label = str(item)+" BTS"
    list_names_B.append(series_label)

for item in list_names_W:
    t[item]=[t_0]
    W[item]=[W_0]
for item in list_names_B:
    B[item]=[B_0]

W_birth_rate = 1
B_birth_rate = 1
#b competition death rate (per WTS and per BTS) of BTS due to WTS
b = 0.20
#w competition death rate (per WTS and per BTS) of WTS due to BTS
w = 0.27

outer_counter=0
for i,label in enumerate(list_names_W):
    #need special label for list_names_B
    label_B = list_names_B[i]
    W_curr = 0.0
    B_curr = 0.0
    t_curr = 0.0
    delta_W = 0.0
    delta_B = 0.0
    counter = 0
    t_curr = t[label][0]

    while t_curr < t_max:
        counter+=1                              #increment counter (0->1 on first trip through
        t_curr=t[label][counter-1]+delta_t[outer_counter]             #get the current time by adding delta_t
        t[label].append(t_curr)                        #add this time to the time list
        W_birth = W_birth_rate*W[label][counter-1]
        W_death = w*B[label_B][counter-1]*W[label][counter-1]
        W_curr = W[label][counter-1]+(W_birth-W_death)*delta_t[outer_counter]
        W[label].append(W_curr)

        B_birth = B_birth_rate*B[label_B][counter-1]
        B_death = b*W[label][counter]*B[label_B][counter-1]
        B_curr = B[label_B][counter-1]+(B_birth-B_death)*delta_t[outer_counter]
        B[label_B].append(B_curr)
    outer_counter+=1


title_base = "WTS and BTS Pop."
title = title_base
filename = "wts_bts_mod41_pop_" + str(delta_t) + ".png"
xlabel = "t (months)"
ylabel = "Number of of sharks"
W_label = "WTS"
B_label = "BTS"

TwoDictLinePlot111(t,W,B,list_names_W,list_names_B, xlabel,ylabel,title,filename)

#DictLinePlot111(t,W,list_names,xlabel,ylabel,title,filename)

#LineColorsPlot111(t,W,W_label,B,B_label,xlabel,ylabel,title,filename)


