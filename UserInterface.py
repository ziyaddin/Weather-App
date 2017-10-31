import tkinter as tk
from tkinter import ttk
import json
import urllib.request

class UserInterface():

	
    win=tk.Tk()
    win.title(" Awesome Weather App")

   

    urltillcity="http://api.openweathermap.org/data/2.5/weather?q="
    print("Enter name of city")
    city=input()
    apikey="&units=metric&appid=00e8850255d526bfa5f02705e8c0ea07"
    wholeurl=urltillcity+city+apikey


    data=json.load(urllib.request.urlopen(wholeurl))

    tempish=data['main']['temp']




    cityLabel=ttk.Label(win,text="Enter name of the city").grid(row=1,column=2)
    userCityInput=ttk.Entry(win).grid(row=2,column=2)
    submitButton=ttk.Button(win,text="Submit",width=10).grid(row=3,column=2)
    temperatur=ttk.Label(win, text="Curernt Temperture in  "+city+ " is:  "+str(tempish)+" C").grid(row=4,column=1)
    win.mainloop()



