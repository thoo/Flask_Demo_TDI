# Flask on Heroku

This project is intended to help you tie together some important concepts and
technologies from the 12-day course, including Git, Flask, JSON, Pandas,
Requests, Heroku, and Bokeh for visualization.

The repository contains a basic template for a Flask configuration that will
work on Heroku.

A [finished example](https://stock30day.herokuapp.com/) that demonstrates some basic functionality.

## Step 1: Setup and deploy

- Git clone [the existing template repository](https://github.com/thedataincubator/flask-framework).
- `Procfile`, `requirements.txt`, `conda-requirements.txt`, and `runtime.txt`
  contain some default settings.
- There is some boilerplate HTML in `templates/`
- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.
- I put all requirements into `requirements.txt` .
- I use API Key  to access data from Quandl. To hide API key from Github push, I use Heroku CLI to set up the enviromental key:

  

  In command line:

  ```
  cd my_app_root_folder
  heroku config:set API_KEY = my_api_key_from_Quandl
  ```

  To call my api_key from my python app,

  ```
  import os
  api_key = os.environ['API_KEY']
  ```

  

  
- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://stock30day.herokuapp.com/`

  

## Step 2: Get data from API and put it in pandas

- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 3: Use Bokeh to plot pandas data

- Create a Bokeh plot from the dataframe.
- Consult the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Make the plot visible on your website through embedded HTML or other methods - this is where Flask comes in to manage the interactivity and display the desired content.
- Some good references for Flask: [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off", and [this tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
