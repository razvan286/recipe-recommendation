import csv
import pandas as pd

df_healthy_nutrients = pd.read_csv('./exports/nutrients_for_health.csv')

def healthy_recipe():
    with open('./exports/nutrients_for_health.csv', 'r') as file:
        reader = csv.reader(file)
        #total_fat -> 10-20
        #calories -> 250-500
        #proteins -> 10-20
        #carbo -> 30-100
        #sodium -> 150-500
