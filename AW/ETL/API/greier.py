# %% [markdown]
# # Exercises
# 
# ## Public holidays
# For these exercises, we will use the API at `https://date.nager.at/Api`. The API can be used like this: `https://date.nager.at/api/v3/PublicHolidays/2022/NO`, which returns all holidays for 2022 for Norway. The API does not require authentication.
# 
# 1. Send a request to the API to get all public holidays for Norway in 2022. If the request is OK (status code 2xx) , print the response json.
# 

# %%
import requests
URL = 'https://date.nager.at/api/v3/PublicHolidays/'
response = requests.get(URL+'2022/NO')
if response.ok:
    print(response.json())

# %% [markdown]
# 2. Create a function `get_public_holidays(year, country_code)` that returns all the public holidays for the given `year` and `country_code` by requesting the API. If the request towards the API fails, you should return "Could not fetch holidays for {country} in {year}"
# ```
# get_public_holidays(2022, "NO")
# ``` 
# should return the json you get when you visit https://date.nager.at/api/v3/PublicHolidays/2022/NO
# ```
# get_public_holidays(2005, "NASFASD") 
# ```
# should return "Could not fetch holidays for NASDFASD in 2005.
# 
# 
# (Hint: Re-use some of the code you used in task 1, and base the error message on whether the response is OK or not)
# 

# %%
def get_public_holidays(year, country_code):
    response = requests.get(f'{URL}{year}/{country_code}')
    if not response.ok:
        return(f'Could not fetch holidays for {country_code} in {year}')
    else:
        return response.json()

print(get_public_holidays('2022', 'NO'))

# %% [markdown]
# 3. Write a function `get_norwegian_holiday_dates(holiday_name, years_back)` that returns all the dates of the given holiday for a number of years back.
# For instance
# ```
# get_norwegian_holiday_dates("Langfredag", 3) should return 
# ["2022-04-15", "2021-04-02", "2020-04-10"] since these are the three last years dates of when "Langfredag" was. (2022, 2021, 2020) 
# ```
# Hint: Re-use the `get_public_holidays` function you created in task 2.
# Also, 
# ```
# for i in range(5,1,-1)
# ```
#  counts backwards from 5 to 1. 
# 
# 

# %%
def get_norwegian_holiday_dates(holiday_name, years_back):
    ls = [str(2023 - x) for x in range(years_back, 0, -1)]
    dict_years = []
    list_of_dates = []
    for year in ls:
        dict_years.append(get_public_holidays(year, 'NO'))
    for dic in dict_years:
        for holidays in dic:
            if holidays['localName'] == holiday_name:
                list_of_dates.append(holidays['date'])
    return list_of_dates

print(get_norwegian_holiday_dates('Langfredag', 3))


# %% [markdown]
# 
# 4.
# If you have got this far- congrats! Try adding another API! 
# This api: http://numbersapi.com can get cool facts about a given date. For instance, `http://numbersapi.com/8/9/date` gives gives fun facts about August 9th. 
# Can you somehow combine it with some of the functions we have already got? 

# %%
URL_FACTS = 'http://numbersapi.com/'

def get_facts(list_of_dates):   
    fact_ls = []
    for date in list_of_dates:
        date_ls = []
        date_ls.append(date[5:7])
        date_ls.append(date[8:10])
        fact_ls.append(date_ls)
    
    for c,date_list in enumerate(fact_ls):
        for x,date in enumerate(date_list):
            if date[0] == '0':
                fact_ls[c][x] = date[1]
    
    f_ls = []
    for i in fact_ls:
        response_facts = requests.get(f'{URL_FACTS}{i[0]}/{i[1]}')
        if not response_facts.ok:
            return 'This didnt work'
        else:
            f_ls.append(response_facts.text)
    return f_ls,list_of_dates

print(get_facts(get_norwegian_holiday_dates('Skjærtorsdag', 3)))

# %%



