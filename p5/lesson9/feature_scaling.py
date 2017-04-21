import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)
salary = []
stock = []
for i in data_dict:
    if data_dict[i]['salary']=='NaN':
        continue
    salary.append(float(data_dict[i]['salary']))
    if data_dict[i]['exercised_stock_options']=='NaN':
        continue
    stock.append(float(data_dict[i]['exercised_stock_options']))

salary = [min(salary), 200000., max(salary)]
stock = [min(stock), 1000000., max(stock)]

salary_array = np.array([[e] for e in salary])
stock_array = np.array([[e] for e in stock])

salary_scaler = MinMaxScaler()
stock_scaler = MinMaxScaler()

rescaled_salary = salary_scaler.fit_transform(salary_array)
rescaled_stock = stock_scaler.fit_transform(stock_array)

print rescaled_salary
print rescaled_stock
                 
    


                 

