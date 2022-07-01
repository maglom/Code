import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats


def throw_distance(velocity, angle, init_height=1.8):

    cos_sin = velocity_decomposition(velocity, angle)    

    t = airtime(cos_sin[1], init_height)

    r = cos_sin[0] * t

    return r

def kmh_to_ms(velocity):
    return velocity * 1000/3600

def velocity_decomposition(velocity, angle):
    
    radians = math.radians(angle)
    speed = kmh_to_ms(velocity) 
    cos = speed * math.cos(radians)
    sin = speed * math.sin(radians)

    return cos, sin

def airtime(velocity_y, init_height, g=9.81):
    
    t = (velocity_y + math.sqrt(velocity_y**2 + 2 * g * init_height)) / g

    return t

#def throw_position(velocity, angle, init_height=1.8, time):
    
    cos_sin = velocity_decomposition(velocity, angle)    

    t = airtime(cos_sin[1], init_height)

    r = cos_sin[0] * t

    return r, t


def thorkildsen_throw():

    thorkildsen_velocity = stats.weibull_max.rvs(2,loc=107,scale=4,size=1)[0]
    thorkildsen_angle = stats.norm.rvs(48,7,1)[0]

    return throw_distance(thorkildsen_velocity, thorkildsen_angle, 2)


def pitkamaki_throw():

    pitkamaki_velocity = stats.weibull_max.rvs(2,loc=106.5,scale=3,size=1)[0]

    pitkamaki_angle = stats.norm.rvs(45.5,4,1)[0]

    return throw_distance(pitkamaki_velocity, pitkamaki_angle, 2)

def thorkildsen_best_throw(numb_throw=6):
    ls = []
    for i in range(numb_throw):
        ls.append(thorkildsen_throw())
    return ls


def pitkamaki_best_throw(numb_throw=6):
    ls = []
    for i in range(numb_throw):
        ls.append(pitkamaki_throw())
    return ls

y = thorkildsen_best_throw(10000)

x = pitkamaki_best_throw(10000)

numb_bins = 1000

plt.hist(y, numb_bins, facecolor='blue', alpha=0.5)
plt.show()

t_win = 0
p_win = 0

for t, k in zip(y,x):
    if t > k:
        t_win += 1
    else:
        p_win += 1
t_win
p_win

t_win / (t_win+p_win)

