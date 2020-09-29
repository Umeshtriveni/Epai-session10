from collections import namedtuple
from faker import Faker
import datetime
from time import perf_counter
from functools import wraps
import re
import random
import string

fake = Faker()

def generate_profiles_using_namedtuple(no_profiles: int): 
    """
    To create a fake profiles of given number of people using namedtuples

    """
    profiles = []
    Profile = namedtuple('Profile', fake.profile().keys())
    for _ in range(no_profiles):
        profiles.append(Profile(**fake.profile()))
    return profiles

def generate_profiles_using_dictionary(no_profiles: int):
    """
    To create a fake profiles of given number of people using dictornary
    """
    profiles = []
    for _ in range(no_profiles):
        profiles.append(fake.profile())
    return profiles

def timed(fn: "Function"):
    """
    Decorator to calculate run time of a function.
    """
    @wraps(fn)
    def inner(*args, **kwargs) -> "Function Output":
        """
        Inner function to calculate the time.
        """
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        time_elapsed = (end - start)
        print('Run time: {0:.6f}s'.format(time_elapsed))
        return result
    return inner

@timed
def calc_data_using_namedtuple() -> "namedtuple":
    """
    calculate the largest blood type, mean-current_location, 
    oldest_person_age and average age of a generated 1000 profiles using namedtuple
    """
    no_profiles = 10000
    profiles = generate_profiles_using_namedtuple(no_profiles)
    date_today = datetime.date.today()
    blood_gp = dict()
    max_age = {'age': 0, 'profile': None}
    cur_loc_coord_sum = [0, 0]
    sum_ages = 0
    for profile in profiles:
        blood_gp[profile.blood_group] = blood_gp.get(profile.blood_group,0) + 1
        age = (date_today - profile.birthdate).days
        if  age > max_age['age']:
            max_age['age'] = age
            max_age['profile'] = profile
        cur_loc_coord_sum[0] += profile.current_location[0]
        cur_loc_coord_sum[1] += profile.current_location[1]
        sum_ages += int(age/365)

    data = namedtuple('data', 'largest_blood_type mean_current_location oldest_person average_age')
    bg_l = max(blood_gp, key=blood_gp.get)
    mean_current_location = (cur_loc_coord_sum[0]/no_profiles, cur_loc_coord_sum[1]/no_profiles)
    return data((bg_l, blood_gp[bg_l]), mean_current_location, (max_age['profile'], int(max_age['age']/365)), int(sum_ages/no_profiles))

@timed
def calc_data_using_dictionary() -> "Dictionary":
    """
    calculate the largest blood type, mean-current_location, 
    oldest_person_age and average age of a generated 1000 profiles using dictionary
    """
    no_profiles = 10000
    profiles = generate_profiles_using_dictionary(no_profiles)
    date_today = datetime.date.today()
    blood_gp = dict()
    max_age = {'age': 0, 'proflie': None}
    cur_loc_coord_sum = [0, 0]
    sum_ages = 0
    for profile in profiles:

        blood_gp[profile['blood_group']] = blood_gp.get(profile['blood_group'],0) + 1
        age = (date_today - profile['birthdate']).days
        if  age > max_age['age']:
            max_age['age'] = age
            max_age['profile'] = profile
        cur_loc_coord_sum[0] += profile['current_location'][0]
        cur_loc_coord_sum[1] += profile['current_location'][1]
        sum_ages += int(age/365)
    bg_l = max(blood_gp, key=blood_gp.get)
    mean_current_location = (cur_loc_coord_sum[0]/no_profiles, cur_loc_coord_sum[1]/no_profiles)
    return {'largest_blood_type': (bg_l, blood_gp[bg_l]), 'mean_current_location': mean_current_location, 'oldest_person': (max_age['profile'], int(max_age['age']/365)), 'average_age': int(sum_ages/no_profiles)}
