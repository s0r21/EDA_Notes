# this script is meant to help processing the data for the EDA process
import pandas as pd
import scipy.stats

from packages import *
import random

test_set = []
for i in range(1,10000):
    n = random.randint(1,i)
    z = random.randint(1,i)
    test_set.append([n,z])
test_set = pd.DataFrame(test_set)

class EDA():
    def kurtosis(self):
        kurt = scipy.stats.kurtosis(self)
        return kurt
    def skew(self):
        skewness = scipy.stats.skew(self)
        return skewness
    def data_desc(self):
        summary = self.describe()
        return summary
    def correl(self):
        correlation = self.corr()
        return correlation
    def correl_with_p(df, y_in_df):
        # if this is statistically significant it means that the data is correlated
        corr_df = pd.DataFrame(columns = ['correl', 'pvalue'])
        for col in df:
            if pd.api.types.is_numeric_dtype(df[col]):
                corr, p_val = scipy.stats.pearsonr(y_in_df, df[col])
                corr_df.loc[col] = [round(corr,5), round(p_val, 5)]
        return corr_df
    def norm_or_not(self):
        if np.abs(EDA.skew(self)) <= 1:
            print(f'Skewness in normality Range: {EDA.skew(self)}')
        else: print(f'Skewness NOT in normality Range: {EDA.skew(self)}')
        if np.abs(EDA.kurtosis(self)) <= 1:
            print(f'Kurtosis in normality Range: {EDA.kurtosis(self)}')
        else: print(f'Kurtosis NOT in normality Range: {EDA.kurtosis(self)}')


print(f'Skewness: {EDA.skew(test_set)}')
print(f'Kurtosis: {EDA.kurtosis(test_set)}')
print(f'Data Summary: {EDA.data_desc(test_set)}')
print(f'Pearsons Correl: {EDA.correl(test_set)}')
print(EDA.norm_or_not(test_set[0]))

print(f'Pearsons Correl and Pvalue: {EDA.correl_with_p(y_in_df = test_set[0], df = test_set)}')

