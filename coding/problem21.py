from datetime import datetime

def calculate_total_experience(candidate_exps):
    # Parse dates and sort the intervals by start date
    intervals = sorted([
        (datetime.strptime(exp['start_date'], '%d-%m-%Y'), datetime.strptime(exp['end_date'], '%d-%m-%Y'))
        for exp in candidate_exps
    ])
    
    # Merge overlapping intervals
    merged_intervals = []
    current_start, current_end = intervals[0]
    
    for start, end in intervals[1:]:
        if start <= current_end:  # Overlapping intervals
            current_end = max(current_end, end)
        else:
            merged_intervals.append((current_start, current_end))
            current_start, current_end = start, end
    merged_intervals.append((current_start, current_end))
    
    # Calculate total experience in days
    total_days = sum((end - start).days for start, end in merged_intervals)
    
    # Convert days to years
    total_years = total_days / 365.25  # Considering leap years
    
    return total_years

candidate_exps =  [
    {"company": "D", "start_date": "01-12-2010", "end_date": "15-07-2012"},
    {"company": "B", "start_date": "25-12-2011", "end_date": "15-07-2014"},
    {"company": "C", "start_date": "20-05-2016", "end_date": "19-07-2018"},
    {"company": "A", "start_date": "20-07-2019", "end_date": "19-07-2020"},
]

total_experience = calculate_total_experience(candidate_exps)
print(f"Total years of experience: {total_experience:.2f}")
