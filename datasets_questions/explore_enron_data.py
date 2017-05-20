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

print "Number of persons:", len(enron_data)

print "Features per person:", len(enron_data.itervalues().next())

poi = 0

for person in enron_data.itervalues():
    if person['poi'] == 1:
        poi = poi + 1

print "Persons of Interest:", poi

print "---"

# print "James Prentice Total Stock:", enron_data['PRENTICE JAMES']['total_stock_value']
#
# print "Wesley Colwell Emails to PICs:", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
#
# print "Jeffrey Skully Exercises Stock Options:", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

known_salary = 0

for person, data in enron_data.iteritems():
    if data['salary'] != 'NaN':
        known_salary = known_salary + 1

print "People with Known Salary:", known_salary

known_salary = 0

for person, data in enron_data.iteritems():
    if data['poi'] == 1 and data['salary'] != 'NaN':
        known_salary = known_salary + 1

print "POIs with Known Salary:", known_salary

print "---"

known_total_payments = 0

for person, data in enron_data.iteritems():
    if data['total_payments'] != 'NaN':
        known_total_payments = known_total_payments + 1

print "People with Known Total Payments:", known_total_payments

known_total_payments = 0

for person, data in enron_data.iteritems():
    if data['poi'] == 1 and data['total_payments'] != 'NaN':
        known_total_payments = known_total_payments + 1

print "POIs with Known Total Payments:", known_total_payments

print "---"

known_emails = 0

for person, data in enron_data.iteritems():
    if data['email_address'] != 'NaN':
        known_emails = known_emails + 1

print "People with Known Emails:", known_emails

known_emails = 0

for person, data in enron_data.iteritems():
    if data['poi'] == 1 and data['email_address'] != 'NaN':
        known_emails = known_emails + 1

print "POIs with Known Emails:", known_emails
