# this script is meant to help processing the data for the EDA process
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
    def norm_or_not(self):
        if np.abs(EDA.skew(self)) <= 1:
            print(f'Skewness in normality Range: {EDA.skew(self)}')
        else: print(f'Skewness NOT in normality Range: {EDA.skew(self)}')
        if np.abs(EDA.kurtosis(self)) <= 1:
            print(f'Kurtosis in normality Range: {EDA.kurtosis(self)}')
        else: print(f'Kurtosis NOT in normality Range: {EDA.kurtosis(self)}')


print(EDA.skew(test_set))
print(EDA.kurtosis(test_set))
print(EDA.data_desc(test_set))
print(EDA.correl(test_set))
print(EDA.norm_or_not(test_set[0]))

