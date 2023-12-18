from tkinter import *
from joblib import *
import joblib as joblib
import sklearn

# Create tkinter GUI
# This GUI is for user to enter information
# into the GUI and the model will give user a predicted cost
# was able to use the same information from google colab on test
# user to compare results and make sure it was successful

# where ever JOBLIB file is located 'GBR_joblib_model' place path where comment say 'path here*'
def show_entry():
  p1 = float(e1.get())
  p2 = float(e2.get())
  p3 = float(e3.get())
  p4 = float(e4.get())
  p5 = float(e5.get())
  p6 = float(e6.get())

  model = joblib.load('Path Filename')#Path Here*
  result = model.predict([[p1,p2,p3,p4,p5,p6]])
  Label(master, text="Health Insurance Cost").grid(row=13)
  Label(master, text=result).grid(row=14)



master = Tk()
master.geometry("580x400")
master.title("Health Insurance Cost")
label = Label(master, text="Health Insurance Cost", bg ="black", fg="white").grid(row=0, columnspan=2)

Label(master, text="Enter Your Age").grid(row=1)
Label(master, text="Please Enter 0 for 'Male' Or 1 for 'Female' ").grid(row=3)
Label(master, text="Please Enter BMI").grid(row=5)
Label(master, text="Please Enter Number of Children").grid(row=7)
Label(master, text="Are You a Smoker: 1 for 'Yes' Or 0 for 'No' ").grid(row=9)
Label(master, text="Please Enter Your Region: 1 for 'Northeast', 2 for 'Northwest', 3 for 'Southeast', 2 for 'Southwest' ").grid(row=11)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)

e1.grid(row=2, column=0)
e2.grid(row=4, column=0)
e3.grid(row=6, column=0)
e4.grid(row=8, column=0)
e5.grid(row=10, column=0)
e6.grid(row=12, column=0)


Button(master, text = "Predict", command=show_entry).grid()

mainloop()