import math

angle = float(input('Input a angle: '))

velocity = float(input('Input velocity: '))

height = float(input('Input height: '))

radians = math.radians(angle)

speed = velocity/3.6

cos = speed * math.cos(radians)

sin = speed * math.sin(radians)

t = (sin + math.sqrt(sin**2 + 2 * 9.81 * height)) / 9.81

r = cos * t

print(f'''
{radians:.2f} 
{speed:.2f}
{cos:.2f}
{sin:.2f}
{t:.2f}
{r:.2f}
''')