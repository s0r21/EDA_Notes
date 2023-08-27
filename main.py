# this script is meant to help processing the data for the EDA process
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats

from packages import *
import random

# Note: when rebuilding this code, use do a print on every function
# to actually give the results that they are looking for. Maybe?

test_set = []
for i in range(1,100):
    n = random.randint(1,i)
    z = random.randint(1,i)
    test_set.append([n,z])
test_set = pd.DataFrame(test_set)

test_set2 = [[1,2,3,4,5,6,7,8,9,10],[10,9,8,7,6,5,4,3,2,1]]

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

class EDA_Chart():
    def tips_for_charts(self):
        print('Just going to make this section a help guide:'
              ' 1.) To make a scatter plot you will need to get matplotlib.pyplot (plt.scatter)'
              ' 2.) After getting that integrating pyplot into your code, use it to generate a plot '
              '     and see how the distribution between x and y is.'
              ' 3.) Regression Model-> ')
    def regression(x,y):
        reg_info = scipy.stats.linregress(x,y)
        slope = print(f'Slope: {reg_info[0]}')
        intercept = print(f'Slope: {reg_info[1]}')
        correl = print(f'Correl: {reg_info[2]}')
        pval =  print(f'Correl: {reg_info[3]}')
        return slope, intercept, correl, pval

print(f'Skewness: {EDA.skew(test_set)}')
print(f'Kurtosis: {EDA.kurtosis(test_set)}')
print(f'Data Summary: {EDA.data_desc(test_set)}')
print(f'Pearsons Correl: {EDA.correl(test_set)}')
print(EDA.norm_or_not(test_set[0]))
print(f'Pearsons Correl and Pvalue: {EDA.correl_with_p(y_in_df = test_set[0], df = test_set[1])}')
EDA_Chart.regression(test_set[0], test_set[1])



# Building the chart:
#plt.plot(test_set2[0], test_set2[1])
#plt.title ('Test Set First vs Second Column')
#plt.xlabel('Test_zero_position')
#plt.ylabel('Test_first_position')
#plt.show()