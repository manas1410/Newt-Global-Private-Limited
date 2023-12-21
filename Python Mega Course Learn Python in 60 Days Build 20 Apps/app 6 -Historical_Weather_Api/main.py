from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)




stations = pd.read_csv(
    r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 6 -Historical_Weather_Api\data_small\stations.txt", sep=",",
    skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]
@app.route("/home")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/<station>/<date>/")
def about(station, date):
    filename = r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 6 -Historical_Weather_Api\data_small\TG_STAID" + str(
        station).zfill(6) + ".txt"
    df = pd.read_csv(filename, sep=",", skiprows=20, parse_dates=["    DATE"])

    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station, "date": date, "temp": temperature}


@app.route("/api/<station>")
def print_station(station):
    df=pd.read_csv(r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 6 -Historical_Weather_Api\data_small\TG_STAID" + str(station).zfill(6) + ".txt",sep=",",skiprows=20,parse_dates=["    DATE"])
    return df.to_dict(orient="records")


@app.route("/api/year/<station>/<year>")
def print_year_data(station,year):

    df=pd.read_csv(r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 6 -Historical_Weather_Api\data_small\TG_STAID" + str(station).zfill(6) + ".txt",sep=",",skiprows=20)
    df["    DATE"]=df["    DATE"].astype(str)
    result= df[df["    DATE"].str.startswith(str(year))]
    return  result.to_dict(orient="records")


if __name__ == "__main__":
    app.run(debug=True)
