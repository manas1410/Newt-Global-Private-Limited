import pandas as pd



# filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
# df = pd.read_csv(filename, sep=",", skiprows=20, parse_dates=["    DATE"])
# print(df.head(5))
# print(filename)

df=pd.read_csv(r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 6 -Historical_Weather_Api\data_small\stations.txt", sep=",",skiprows=17)
print(df.head(5))