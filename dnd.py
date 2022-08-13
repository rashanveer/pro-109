import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")

List = df["math score"].tolist()

Mean = statistics.mean(List)
Median = statistics.median(List)
Mode = statistics.mode(List)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(Mean, Median, Mode))

Std = statistics.stdev(List)

FirstStdStart,heightFirstStdEnd = Mean-Std,Mean+Std
SecondStdStart,heightSecondStdEnd = Mean-(2*Std),Mean+(2*Std)
ThirdStdStart,heigthThirdStdEnd = Mean-(3*Std),Mean+(2*Std)

ListInFirstStd = [result for result in List if result > FirstStdStart and result < heightFirstStdEnd]
ListInSecondtStd = [result for result in List if result > SecondStdStart and result < heightSecondStdEnd]
ListInThirdStd = [result for result in List if result > ThirdStdStart and result < heigthThirdStdEnd]

print("{}% of data for data lies within 1 standard deviation".format(len(ListInFirstStd)*100.0/len(List))) 
print("{}% of data for data lies within 2 standard deviations".format(len(ListInSecondtStd)*100.0/len(List))) 
print("{}% of data for data lies within 3 standard deviations".format(len(ListInThirdStd)*100.0/len(List)))
