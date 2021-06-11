# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:05:06 2021

@author: Gebruiker
"""

# %% Variables

start_day = '2016-10-01'

end_day = '2021-06-11'

number_of_days_off_per_month = 2

# %% Import Modules

import utils as u
import pandas as pd
from datetime import datetime
import numpy as np

# %% main

# Fomatting dates

start_day = datetime.strptime(start_day,'%Y-%m-%d').date()
end_day = datetime.strptime(end_day,'%Y-%m-%d').date()

# Getting list of all dates
l_days = list(pd.date_range(start_day,end_day,freq='d'))

# We remove the week-ends
l_days = u.exclude_week_ends(l_days)

#convering from datetime to date
l_days = [d.date() for d in l_days]

#creating the list of holidays
l_holidays = u.get_all_holidays(start = min(l_days).year, end = max(l_days).year)

#getting anything in l_days that is not in l_holidays
l_days = list(np.setdiff1d(l_days,l_holidays))

#prepping for calculating accured holidays
num_months = (end_day.year - start_day.year) * 12 + (end_day.month - start_day.month)

num_days = num_months * number_of_days_off_per_month

number_of_days_worked = len(l_days) - num_days

print('You have worked for %s days, congratulations!' % number_of_days_worked)


