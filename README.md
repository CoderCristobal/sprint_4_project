# sprint_4_project

### Web App: 
https://cristobal-liceas-sprint4-project.onrender.com/
### Git Hub: 
https://github.com/CoderCristobal/sprint_4_project

# Cristobal Licea's webapp for sprint 4


## Description
The goal of this project is to showcase the Data Science skills I've learned using Python, Pandas, Jupyter Notebook to make an functional Web App. This Web App allows the user to view Car Advertisement data and not only be able to filter it, but view some statistics like average price by model and year. In this project I was able to learn more about Streamlit, and how it works with Pandas to make Data Frames visible and usable in a Web App


## How to install
The simplest way to use the Web App is to click the link above

In the case that you are cloning this project repo, in the file terminal use:
pip install -r requirements.txt

This will install all required dependencies and will allow you to open the app using:
Streamlit run app.py
From terminal. In the case the app seems to not load, remove the file: config.toml
from the .streamlit folder.


## Instructions
Upon opening the app, you can view a listing of all cars and can sort based on the column. Below the full listing, you will see a graph displaying the amount of cars available by miles on odometer, or if you use the check box, display the amount of cars available by price. The 'condition' blocks in the legend can be clicked to filter in or out those car 'condition's. Below this section, you will 2 graphs displaying: 1. Prices of model in a given condition, and 2. The average price of a model in a given condition. You can use the selectbox above these 2 graphs to select what model and condition the graphs will display. Below the 2 graphs you also see a table displaying the average price of a given model and condition.

