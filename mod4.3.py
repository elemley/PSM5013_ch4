from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *


#Mod4.3 SIR Modeling Equation Set 4.3.1
s_0 = 762
i_0 = 1
r_0 = 0
s = [s_0]
i = [i_0]
r = [r_0]

recov_rate = 0.5 #per day
trans_const =  0.00218 #per day

#t_0 = start time
t_0=0   #days
t = [t_0]
delta_t=0.1    #days
t_max = 14      #days

counter=0

while t[counter] < t_max:
    counter+=1                              #increment counter (0->1 on first trip through
    t_curr=t[counter-1]+delta_t             #get the current time by adding delta_t
    t.append(t_curr)                        #add this time to the time list
    new_infected = trans_const*s[counter-1]*i[counter-1]*delta_t
    new_recov = recov_rate * i[counter-1] * delta_t
    s.append(s[counter-1]-new_infected)
    i.append(i[counter-1]+new_infected-new_recov)
    r.append(r[counter-1]+new_recov)
    #print t
    #print i
    #print r
    #print s

title_base = "SIR Model"
title = title_base + " delta_t = " + str(delta_t)
filename = "sir_model_mod43_" + str(delta_t) + ".png"
xlabel = "t (days)"
ylabel = "Number of species"
s_label = "Susecptible"
i_label = "Infected"
r_label = "Recovered"

ThreeLineColorsPlot111(t,s,s_label,i,i_label,r,r_label,xlabel,ylabel,title,filename)



