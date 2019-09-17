import pandas as pd 

data = pd.read_csv("input_wages_hours.csv", sep ="\t")

data2 = data.sort(["AGE", "RATE"]) 

# print(data2.sorted(["AGE"])) # opravit funkcia sort 
