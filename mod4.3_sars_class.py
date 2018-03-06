from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *


#Mod4.3 SEIR Modeling
s_0 = 999
e_0 = 0
i_0 = 1
r_0 = 0
n_0 = s_0+e_0+i_0+r_0
s = [s_0]
e = [e_0]
r = [r_0]
n = [n_0]
i = [i_0]

alpha = 0.05
beta = 10
gamma = 0.17
mu = 0.005

#new_s_rate = 50 #per day
#q_rate = 0.25 #per day

#t_0 = start time
t_0=0   #days
t = [t_0]
delta_t=0.1    #days
t_max = 100     #days

counter=0

while t[counter] < t_max:
    counter+=1                              #increment counter (0->1 on first trip through
    t_curr=t[counter-1]+delta_t             #get the current time by adding delta_t
    t.append(t_curr)                        #add this time to the time list

    s_births = mu*n[counter-1]
    s_dies = mu*s[counter-1]
    e_new = beta*i[counter-1]/n[counter-1]*s[counter-1]
    e_dies = mu*e[counter-1]
    i_new = alpha*e[counter-1]
    i_dies = mu*i[counter-1]
    r_new = gamma*i[counter-1]
    r_dies = mu*r[counter-1]

    delta_s = (s_births-s_dies-e_new)*delta_t
    delta_e = (e_new-e_dies-i_new)*delta_t
    delta_i = (i_new-i_dies-r_new)*delta_t
    delta_r = (r_new-r_dies)*delta_t

    s.append(s[counter-1]+delta_s)
    e.append(e[counter-1]+delta_e)
    i.append(i[counter-1]+delta_i)
    r.append(r[counter-1]+delta_r)

    delta_n = delta_s+delta_i+delta_e+delta_r
    n.append(n[counter-1]+delta_n)

    #print t
    #print i
    #print r
    #print s

title_base = "SEIR Model"
title = title_base + " delta_t = " + str(delta_t)
filename = "seir_model_mod43_" + str(delta_t) + ".png"
xlabel = "t (days)"
ylabel = "Population"
s_label = "Susecptible"
i_label = "Infected"
r_label = "Recovered"
e_label = "Exposed"
n_label = "Total"

FiveLineColorsPlot111(t,s,s_label,e,e_label,i,i_label,r,r_label,n,n_label,xlabel,ylabel,title,filename)



