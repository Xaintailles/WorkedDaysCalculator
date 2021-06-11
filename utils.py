# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:05:20 2021

@author: Gebruiker
"""
# %% Import Modules

from dateutil import easter
from datetime import datetime
from datetime import timedelta

# %% Functions

def get_easter_for_range(start: int, end: int) -> list:
    l_easter_days = [easter.easter(y) for y in range(start,end+1)]
    return l_easter_days

def get_easter_monday_for_list(list_of_easter: list) -> list:
    l_easter_monday = [d + timedelta(days=39) for d in list_of_easter]
    return l_easter_monday

def get_ascencion_for_list(list_of_easter: list) -> list:
    l_ascension_days = [d + timedelta(days=39) for d in list_of_easter]
    return l_ascension_days

def get_whit_monday_for_list(list_of_easter: list) -> list:
    l_whit_mondays = [d + timedelta(days=50) for d in list_of_easter]
    return l_whit_mondays

def get_good_friday_for_list(list_of_easter: list) -> list:
    l_good_fridays = [d - timedelta(days=2) for d in list_of_easter]
    return l_good_fridays

def get_static_holidays_from_range(start: int, end: int) -> list:
    l_static_holidays = list()
    for y in range(start,end+1):
        l_static_holidays.append(datetime(y,1,1).date()) #1st January
        l_static_holidays.append(datetime(y,4,27).date()) #King's Day
        l_static_holidays.append(datetime(y,5,5).date()) #Liberation Day
        l_static_holidays.append(datetime(y,12,25).date()) #XMas Day
        l_static_holidays.append(datetime(y,12,26).date()) #Boxing Day
    return l_static_holidays

def get_all_holidays(start: int, end: int) -> list:
    
    l_easters = get_easter_for_range(start, end)
    l_good_fridays = get_good_friday_for_list(l_easters)
    l_easter_mondays = get_easter_monday_for_list(l_easters)
    l_ascension_days = get_ascencion_for_list(l_easters)
    l_whit_mondays = get_whit_monday_for_list(l_easters)
    l_static_holidays = get_static_holidays_from_range(start, end)
    
    l_final = list()
    
    l_final.extend(l_good_fridays)
    l_final.extend(l_easter_mondays)
    l_final.extend(l_ascension_days)
    l_final.extend(l_whit_mondays)
    l_final.extend(l_static_holidays)
                          
    return l_final

def exclude_week_ends(list_of_days: list, excluded = (6,7)) -> list:
    
    new_days = list()
    
    for d in list_of_days:
        if d.isoweekday() not in excluded:
            new_days.append(d)
            
    return new_days

def isleapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return 
    else:
        return False

