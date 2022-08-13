import math

def throw_distance(velocity, angle, init_height=1.8):

    cos_sin = velocity_decomposition(velocity, angle)    

    t = airtime(cos_sin[1], init_height)

    r = cos_sin[0] * t

    return r, t

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


velocity = float(input('Input a angle: '))

angle = float(input('Input velocity: '))

height = float(input('Input height: '))

print(throw_distance(velocity, angle, height))


