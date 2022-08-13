from scipy import stats
import numpy as np

angle = stats.norm.rvs(loc=48,scale=7,size=1000)

velocity = stats.weibull_max.rvs(2,loc=107,scale=4,size=1000)

height = 0

radians = np.radians(angle)

speed = velocity/3.6

cos = speed * np.cos(radians)

sin = speed * np.sin(radians)

t = (sin + np.sqrt(sin**2 + 2 * 9.81 * height)) / 9.81

r = cos * t

np.set_printoptions(precision=10)
print(f'''
{radians} 
{speed}
{cos}
{sin}
{t}
{r}
''')



values = r.tolist()

alpha = 0.05

values.sort()

output = ["%.2f" % elem for elem in values]

lower_idx = round(len(values) * alpha / 2)


upper_idx = round(len(values) * (1 - alpha / 2)) - 1

print(f'Lower values =  {output[:lower_idx]} \nUpper values =  {output[upper_idx:]}')

