import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['Interest.Rate'][0:5]

loansData['Loan.Length'][0:5]

loansData['FICO.Range'][0:5]

def f(x):
    '''This function takes x as a parameter and returns x squared'''
    print x**2

f(2)

g = lambda x: x**2

g(2)

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

InterestRate = b + a1(FICOScore) + a2(LoanAmount)

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()

