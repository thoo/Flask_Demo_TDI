from flask import Flask, render_template, request, redirect
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.io import show,output_file
from bokeh.palettes import Category10_4 as C4
import os
from bokeh.models import HoverTool
from boto.s3.connection import S3Connection
import quandl as ql

from functions import *




app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/myplot',methods=['POST'])

def myplot():
	web_input=request.form.getlist('price')
	ticker=request.form['ticker']
	print(web_input,ticker)
	
	plot=stock_plot(ticker,web_input)

	script,div=components(plot)

	return render_template('myplot.html',script=script,div=div)

if __name__ == '__main__':
  app.run(port=33507,debug=True)
