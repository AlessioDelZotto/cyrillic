import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

loansData = pd.read_csv('/home/alessio/Desktop/py/loansData_clean.csv')

loansData['Monthly.Income'][0:5]
loansData['Interest.Rate'][0:5]
loansData['Home.Ownership'][0:5]

annual_inc = loansData['Monthly.Income'] * 12
int_rate = loansData['Interest.Rate']
home_ownership = loansData['Home.Ownership']

X = loansData.copy()
y = X.pop('Interest.Rate')

loansData.head()

X = loansData[['Monthly.Income', 'Home.Ownership']]
y = loansData['Interest.Rate']

loansData.head()

X = sm.add_constant(X)
est = smf.ols(formula='Interest.Rate ~ Monthly.Income + Home.Ownership', data=loansData).fit()

est.summary()

