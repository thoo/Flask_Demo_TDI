import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.io import show,output_file
from bokeh.palettes import Category10_4 as C4
from bokeh.models import HoverTool
import os
from boto.s3.connection import S3Connection

import quandl as ql

#stock_dict={"AAPL":"APPLE Inc.","MSFT":"Microsoft Corp.","NKE":"Nike Inc.","INTC":"Intel Corp."}
api_key = os.environ['API_KEY']
def get_ql(stock='AAPL',api_key=api_key):
	
	mykey=api_key.rstrip()

	ql.ApiConfig.api_key = mykey
	data=ql.get('WIKI/'+stock,rows=30)
	data.reset_index(inplace=True)
	return data

def hover(col_name,line):
	Hov=HoverTool(
	tooltips=[
		( 'Date',   '@Date{%F}'            ),
		( col_name,  '@'+col_name+'{%0.2f}' ), # use @{ } for field names with spaces
		# 'volume', '@volume{0.00 a}'      ),
	],

	formatters={
		'Date'      : 'datetime', # use 'datetime' formatter for 'date' field
		col_name : 'printf',   # use 'printf' formatter for 'adj close' field
								  # use default 'numeral' formatter for other fields
	},

	# display a tooltip whenever the cursor is vertically in line with a glyph
	mode='vline',renderers=[line]
	)
	return Hov



def stock_plot(stock_ticker='AAPL',col_names=['Open','Close']):
	

	data=get_ql(stock_ticker)
	data.rename(columns={'Adj. Open': 'Adj_Open', 'Adj. Close': 'Adj_Close'}, inplace=True)
	column_dict={'Adj. Open': 'Adj_Open', 'Adj. Close': 'Adj_Close','Open':'Open','Close':'Close'}
	#print(data.head())
	p=figure(plot_width = 800,\
			 plot_height = 600,\
			 x_axis_type = "datetime")

	#p.background_fill_color = "black"

	color={'Open':C4[0],\
			'Close':C4[1],\
			'Adj_Open':C4[2],\
			'Adj_Close':C4[3]}


	p.title.text= "{} : End-Of-Day Stock Price for Last 30-Business-Day".format(stock_ticker)

	#legend
	p.xaxis.axis_label = 'Time [Month/Day]'
	p.yaxis.axis_label = 'Stock Price in $'


   


	for i in col_names:
		i=column_dict[i]
		line=p.line('Date',i, source = data, legend=":"+i,alpha = 0.9 , line_width = 3, line_color = color[i])
		hov=hover(i,line)
		p.add_tools(hov)
	p.legend.location= "top_left"
	p.legend.click_policy="hide"
	return p



if __name__ == "__main__":
	stock_plot()

