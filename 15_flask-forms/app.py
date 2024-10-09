'''
SAD - Sascha, Aditya, Danny
SoftDev
K15 - Flask-Form - Using Flask and request
2024 - 10 - 09
Time Spent: 1 hour 
'''

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    if request.method == "POST":
        username = request.form["username"]
    else:
        username = request.args["username"]
    explanation = "The GET method retrieves data by appending parameters to the URL, making it suitable for search queries. On the other hand, POST  puts data into the request body. For this reason, we prefer to use POST."
    return render_template('response.html', username=username, explanation=explanation, request=request.method) #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()