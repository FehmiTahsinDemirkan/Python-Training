import pandas as pd
import numpy as np


numbers = [10,20,30,40]
letters = ['a','b','c','d']
scalar = 5
# random_numbers = np.random.randint(10,100,6)
# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(random_numbers)

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insigma"])
opel2019 = pd.Series([10,70,20,30],["astra","corsa","grandland","insigma"])
print(opel2018+opel2019)
