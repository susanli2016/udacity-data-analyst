#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

poi_array =[]
for i in enron_data.values():
    if i['poi']==True:
        poi_array.append(i)
        
poi_array_nopayment = []
for p in poi_array:
    if p['total_payments']=='NaN':
        poi_array_nopayment.append(p['total_payments'])

print 'The number of people in the data set is: ', len(enron_data)
print 'The number of feature is: ', len(enron_data.values()[0])
print 'The number of person of interest is: ', sum([1 for i in enron_data.values() if i['poi']==True])
print 'The total value of staock belongs to James Prentice is: ', enron_data['PRENTICE JAMES']['total_stock_value']
print 'The number of email message from Wesley Colwell to persons of interest is: ', enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print 'The value of stock options exercised by Jeffrey Skilling is: ', enron_data['SKILLING JEFFREY K']['exercised_stock_options']

for i in enron_data.keys():
    if i.startswith('S') or i.startswith('J'):
        print i
for i in enron_data.keys():
    if i.startswith('A') or i.startswith('F'):
        print i
for i in enron_data.keys():
    if i.startswith('K') or i.startswith('L'):
        print i
print 'The total payments to Lay is: ', enron_data['LAY KENNETH L']['total_payments']
print 'The total payments to Fastow is:', enron_data['FASTOW ANDREW S']['total_payments']
print 'The total payments to Skilling is:', enron_data['SKILLING JEFFREY K']['total_payments']
print 'The number of folks have a quantified salary: ', sum([1 for i in enron_data.values() if i['salary']!='NaN'])
print 'The number of folks have a known email address: ', sum([1 for i in enron_data.values() if i['email_address']!='NaN'])
print "The number of people in E+F dataset have 'NaN' for their total payments: ", sum([1 for i in enron_data.values() if i['total_payments']=='NaN'])
print "The percentage of people in E+F dataset have 'NaN' for their total payments: ", 100*21.0/146
print "The number of POIs in the E+F dataset have 'NaN' for their total payments is: ", sum([1 for i in enron_data.values() if i['total_payments']=='NaN' and i['poi']==True]) 
