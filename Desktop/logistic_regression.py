import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.to_csv('loansData_clean.csv', header=True, index=False)

df[df['Interest.Rate'] == 10].head()
df[df['Interest.Rate'] == 13].head()

interest_rate = b + a1(FICOScore) + a2(LoanAmount)

logit = sm.Logit(df['IR_TF'], df[ind_vars])

result = logit.fit()

coeff = result.params
print coeff
 
interest_rate = −60.125 + 0.087423(FicoScore) − 0.000174(LoanAmount)

p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))

 
