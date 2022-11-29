from statistics import stdev as Sp
from statistics import mean
from scipy.special import erfc
from math import fabs

l = [8.02, 8.16, 3.97, 8.64, 0.84, 4.46, 0.81, 7.74, 8.78, 9.26, 20.46, 29.87, 10.38, 25.71]

sp = Sp(l)
avg = mean(l)

print("%.2f" % sp, "%.2f" % avg, [erfc(fabs(i-avg)/sp) < 1/(2 * len(l)) and i  for i in l])