"""
Given a list of dictionaries where each represents a work experience of a candidate. 
Each work experience contains a start date, end date and the name of the company where the candidate has worked. 



Write a function that will calculate the total years of experience of the candidate.
Note: A candidate can be working for multiple companies at the same time, 
this should be accounted for while calculating the total years. I.e., 
If a candidate has worked for 1 year for both company A and company B during the same time period, 
the total years of experience will be 1 and not 2. Also there could be “gaps” during which a candidate has not worked for any company. 
This should also be accounted for while calculating the total years of experience.
"""

from typing import List, Dict

from datetime import timedelta, datetime


candidate_exps =  [
    {"company": "D", "start_date": "01-12-2010", "end_date": "15-07-2012"},
    {"company": "B", "start_date": "25-12-2011", "end_date": "15-07-2014"},
    {"company": "C", "start_date": "20-05-2016", "end_date": "19-07-2018"},
    {"company": "A", "start_date": "20-07-2019", "end_date": "19-07-2020"},
]



def calculate_total_experiance(candidate_exps: List[Dict]):
    previous_start_time = datetime.strptime(candidate_exps[0]["start_date"], r"%d-%m-%Y")
    previous_end_time = datetime.strptime(candidate_exps[0]["end_date"], r"%d-%m-%Y")
    exp, empty = previous_end_time - previous_start_time, timedelta(0)
    for i in range(1, len(candidate_exps)):
        current_start_time = datetime.strptime(candidate_exps[i]["start_date"], r"%d-%m-%Y")
        current_end_time = datetime.strptime(candidate_exps[i]["end_date"], r"%d-%m-%Y")
        if current_start_time - previous_end_time > empty:
            exp += current_end_time - current_start_time
        else:
            exp += (previous_end_time - current_start_time)+ (current_end_time - previous_end_time)
        previous_end_time = current_end_time
        previous_start_time = current_start_time

    return exp.days/365
        

print(calculate_total_experiance(candidate_exps=candidate_exps))