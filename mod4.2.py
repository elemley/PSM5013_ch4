from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *


#Mod4.2 Equation Set 4.2.1
#prey= # of squirrels
#pred = # of hawks
#prey_0 initial population at time t_0
#pred_0 initial population at time t_0
prey_0=50
pred_0=200
prey = [prey_0]
pred = [pred_0]
#t_0 = start time
t_0=0   #months
t = [t_0]
delta_t=0.0001    #months
t_max = 12      #months

pred_birth_frac = 0.01
pred_death_const = 1.06

prey_birth_fraction=2
prey_death_constant = 0.02

prey_curr = 0.0
pred_curr = 0.0
t_curr = 0.0
counter=0

while t[counter] < t_max:
    counter+=1                              #increment counter (0->1 on first trip through
    t_curr=t[counter-1]+delta_t             #get the current time by adding delta_t
    t.append(t_curr)                        #add this time to the time list
    pred_births = pred_birth_frac*prey[counter-1]*pred[counter-1]*delta_t
    pred_deaths = pred_death_const*pred[counter-1]*delta_t
    pred_curr = pred[counter-1]+pred_births-pred_deaths

    prey_births = prey_birth_fraction*prey[counter-1]*delta_t
    prey_deaths = prey_death_constant*pred[counter-1]*prey[counter-1]*delta_t

    prey_curr = prey[counter-1]+prey_births - prey_deaths

    pred.append(pred_curr)

    prey.append(prey_curr)
    #print t
    #print pred_curr
    #print prey_curr

title_base = "Pred. / Prey Squirrels and Hawks"
title = title_base + " delta_t = " + str(delta_t)
filename = "pred_prey_mod42_pop_" + str(delta_t) + ".png"
xlabel = "t (months)"
ylabel = "Number of species"
pred_label = "Predator (Hawks)"
prey_label = "Prey (Squirrels)"

TwoLineColorsPlot111(t,pred,pred_label,prey,prey_label,xlabel,ylabel,title,filename)

title = title_base + " delta_t = " + str(delta_t)
filename = "pred_prey_mod42b_pop_" + str(delta_t) + ".png"
xlabel = "Prey"
ylabel = "Predators"
LinePlot111(prey,pred,xlabel,ylabel,title,filename)



