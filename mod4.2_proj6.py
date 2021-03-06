from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *


#Mod4.2 Equation Set 4.2.1
#prey= # of squirrels
#pred = # of hawks
#prey_0 initial population at time t_0
#pred_0 initial population at time t_0
prey_0=3.0e8
pred_0=5000
M = 4.0e8
prey = [prey_0]
pred = [pred_0]
#t_0 = start time
t_0=0   #months
t = [t_0]
delta_t=0.01    #years
t_max = 10      #years

pred_curr = 0.0
pred_birth_frac = 0.1
pred_death_const = 0

prey_birth_fraction=0.05
prey_death_constant = 0.01

prey_curr = 0.0
t_curr = 0.0
counter=0

while t[counter] < t_max:
    counter+=1                              #increment counter (0->1 on first trip through
    t_curr=t[counter-1]+delta_t             #get the current time by adding delta_t
    t.append(t_curr)                        #add this time to the time list
    pred_births = pred_birth_frac*pred[counter-1]*delta_t
    pred_deaths = pred_death_const*pred[counter-1]*delta_t
    pred_curr = pred[counter-1]+pred_births-pred_deaths

    prey_births = prey_birth_fraction*prey[counter-1]*prey[counter-1]/M*delta_t
    prey_deaths = prey_death_constant*prey[counter-1]*delta_t

    prey_curr = prey[counter-1]+prey_births - prey_deaths

    pred.append(pred_curr)

    prey.append(prey_curr)
    #print t
    #print pred_curr
    #print prey_curr

title_base = "Pred. / Prey Whales and Krill"
title = title_base + " delta_t = " + str(delta_t)
filename = "pred_prey_mod43_proj6_" + str(delta_t) + ".png"
xlabel = "t (years)"
ylabel = "Number of whales or tons of krill"
pred_label = "Predator (Blue Whales)"
prey_label = "Prey (Tons of Krill)"

TwoLineColorsPlot111(t,pred,pred_label,prey,prey_label,xlabel,ylabel,title,filename)

title = title_base + " delta_t = " + str(delta_t)
filename = "pred_prey_mod42b_pop_" + str(delta_t) + ".png"
xlabel = "Prey"
ylabel = "Predators"
LinePlot111(prey,pred,xlabel,ylabel,title,filename)



