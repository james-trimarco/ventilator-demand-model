import pandas as pd

us_population = 325_000_000
peak_sick_coef = 0.1
symptomatic_coef = 0.5
need_hospital_coef = 0.8
need_ventilation_coef = 0.3

print(
    f"Number of ventilators needed: {us_population * peak_sick_coef * symptomatic_coef * need_hospital_coef * need_ventilation_coef}")
