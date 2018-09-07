from flask import Flask, render_template, request, redirect, url_for
from Calculator import Calculator


#creates the application
app = Flask(__name__)

calc_total = False
calc_time = False

@app.route("/", methods = ['POST', 'GET'])
def mainWebsite():
    calc_total = True
    if request.method == 'POST':
        print(request.form)
        calculator = Calculator(initial = int(request.form["initial"]), rate = int(request.form["rate"])) #i removed the apostrophe and somehow it worked
        interest = calculator.total_interest(int(request.form['time']))
        print(calculator.total_interest(int(request.form['time']))) #this is broken
        if int(request.form['time'])< 0:
            return render_template("interestCalculator.html", message="invalid input try again", calc_total = calc_total)
        return render_template("interestCalculator.html", total=interest, message="success", calc_total = calc_total)
    return render_template("interestCalculator.html", calc_total = calc_total) #change this back to main website


@app.route("/calculatetime", methods = ['POST', 'GET'])
def timeCalculator():
    calc_time = True
    if request.method == 'POST':
        print(request.form)
        calculator = Calculator(initial = int(request.form["initial"]), rate = int(request.form["rate"]))
        calcedtime = calculator.time_required(int(request.form["gain"]))
        print(calcedtime)
        return render_template("interestCalculator.html", totaltime = calcedtime, message="success", calc_time = calc_time )
    return render_template("interestCalculator.html", calc_time = calc_time) #change this back to timeCalculator.html



@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/antiage")
def anti_age():
    return render_template("anti_age.html")


    #fornow all the calculators will be the same but once i get it working i have to change each individual html file


    #Put calc total and calc time as a variable in the main function and have it disable and change colour depending on what function starts it

