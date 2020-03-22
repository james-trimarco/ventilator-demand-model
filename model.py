import pandas as pd
import requests

us_population = 325_000_000
peak_sick_coef = 0.1
symptomatic_coef = 0.5
need_hospital_coef = 0.8
need_ventilation_coef = 0.3

print(
    f"Number of ventilators needed in baseline model: \
    {us_population * peak_sick_coef * symptomatic_coef * need_hospital_coef * need_ventilation_coef}")

HOST = "https://api.census.gov"
year = "2010"
dataset = "dec/sf1"
key = 'd650c820313785ca8ffd7bc7b0f7d5de0fd4dbce'
base_url = "/".join([HOST, year, dataset])


predicates = {}
get_vars = ["NAME", "AREALAND", "P001001"]
predicates["get"] = ",".join(get_vars)
predicates["for"] = "state:*"
#predicates["key"] = key

r = requests.Request('GET', base_url, params=predicates)
prep = r.prepare()
print(prep.url)
#print(predicates)
#print(r.text)