import os
from flask import Flask, render_template, redirect, url_for, request,Markup,make_response,render_template_string
import pandas as pd
from nsedata import *

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def app1():
    symbols=nseindia.symbol()
    dates=nseindia.data()
    #print(dates)
    return render_template('web.html',symbols=symbols)

@app.route('/client_change', methods=[ 'GET','POST'])
def client_change():
    print("route working")
    print(request.method)
    if request.method.lower() == 'post':
        print("in data")
        symbol=request.get_data('client')
        symbol=str(symbol, "utf-8")
        print(symbol)
        symbol=symbol.split('=')[1]
        print(symbol)
        symbols=nseindia.symbol()
        index=symbols.index(symbol)
        
        values=nseindia.find_symbol(nseindia,symbol)
        values=values.to_html()
        #print("values")
        


    return values





if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print ("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')