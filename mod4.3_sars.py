from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *


#Mod4.3 SEIR Modeling
s_0 = 950
e_0 = 0
i_0 = 50
r_0 = 0
n_0 = s_0+e_0+i_0+r_0
s = [s_0]
e = [e_0]
i = [i_0]
r = [r_0]
n = [n_0]
beta = 0.1
gamma = 0.1
mu = 0.001
alpha = 0.20

#new_s_rate = 50 #per day
#q_rate = 0.25 #per day

#t_0 = start time
t_0=0   #days
t = [t_0]
delta_t=0.1    #days
t_max = 500     #days

counter=0

while t[counter] < t_max:
    counter+=1                              #increment counter (0->1 on first trip through
    t_curr=t[counter-1]+delta_t             #get the current time by adding delta_t
    t.append(t_curr)                        #add this time to the time list

    s_born = mu*n[counter-1]
    s_died = mu*s[counter-1]
    s_exposed = beta*i[counter-1]/n[counter-1]*s[counter-1]

    e_died = mu*e[counter-1]
    e_infected = alpha*e[counter-1]

    i_died = mu*i[counter-1]
    i_recovered = gamma*i[counter-1]

    r_died = mu*r[counter-1]

    delta_s = (s_born-s_died-s_exposed)*delta_t
    delta_e = (s_exposed - e_died - e_infected)*delta_t
    delta_i = (e_infected-i_died-i_recovered)*delta_t
    delta_r = (i_recovered-r_died)*delta_t

    s.append(s[counter-1]+delta_s)
    e.append(e[counter-1]+delta_e)
    i.append(i[counter-1]+delta_i)
    r.append(r[counter-1]+delta_r)

    n.append(s[counter]+e[counter]+i[counter]+r[counter])


title_base = "SEIR Model"
title = title_base + " delta_t = " + str(delta_t)
filename = "seir_model_mod43_" + str(delta_t) + ".png"
xlabel = "t (days)"
ylabel = "Number of species"
s_label = "Susceptible"
e_label = "Exposed"
i_label = "Infected"
r_label = "Recovered"
n_label = "Population Size"

FiveLineColorsPlot111(t,s,s_label,e,e_label,i, i_label,r,r_label,n,n_label,xlabel,ylabel,title,filename)



