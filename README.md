# **Session 10 - Tuples & Named Tuples and Modules**

## **Assignment**
1. Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings)
2. Do the same thing above using a dictionary. Prove that namedtuple is faster.
3. Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. 

## **Functions**

### 1. timed
Decorator to calculate run time of a function.

```python
def timed(fn: "Function"):
    
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
```

### 2. generate_profiles_using_namedtuple
To create a fake profiles of given number of people using namedtuples

```python
profiles = []
    Profile = namedtuple('Profile', fake.profile().keys())
    for profile in range(no_profiles):
        profiles.append(Profile(**fake.profile()))
    return profiles
```
### 3.calc_data_using_namedtuple
    calculate the largest blood type, mean-current_location, 
    oldest_person_age and average age of a generated 1000 profiles using namedtuple
```python
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
```
### 4.calc_data_using_dictionary
    calculate the largest blood type, mean-current_location, 
    oldest_person_age and average age of a generated 1000 profiles using dictionary
```python
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
```


