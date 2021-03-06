import matplotlib.pyplot as plt
import numpy as np

rok = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
pensja = np.array([1923.81, 2061.85, 2133.21, 2201.47, 2289.57, 2380.29, 2477.23, 2691.03, 2943.88, 3102.96, 3224.98, 3399.52, 3521.67, 3650.06, 3783.46, 3899.78, 4047.21, 4271.51, 4585.03, 4918.17, 5167.47, 5536.80])

plt.plot(rok,pensja, marker = 'D')
plt.xlabel("Rok")
plt.ylabel("Średnie zarobki")
plt.grid()
plt.show()
