# Bangalore-House-Price-Prediction

## Table of Content
  * [Demo](#demo)
  * [Objective](#objective)
  * [Inspiration](#inspiration)
  * [Approach](#approach)
  * [Data](#data)
  * [Packages/Libraries](#packageslibraries)
  * [Installation](#installation)
  * [To Do](#to-do)
  * [Contact](#contact)

## Demo
This Webapp is deployed on Streamlit-sharing
Link: [https://share.streamlit.io/rahul1758/bangalore-house-price-prediction/app.py](https://share.streamlit.io/rahul1758/bangalore-house-price-prediction/app.py)
### Working
![]()

## Objective
The Objective of this Project was to predict the price of Houses in Bangalore given its features.

## Inspiration
All ML beginners are aware of Boston House Price dataset, which is a stepping stone for regression tasks. I thought, why not implement the same task for an Indian city (by now you know which one 😁). So here is this project, a product of the above thought.

## Data 
I am using a Kaggle dataset which you can download from here: [Bangalore House Price data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data). This House price data from 2017 and has various features of House like: 
* Area_type
* Location
* Size (BHK)
* Bathrooms
* Balcony
* Availability
* Prices
* Society name

## Approach
This process involved many steps such as:
1. Data Exploration: Understanding the data, types of variables (Numericall & Categorical) & gaining some insights from the data.
2. Feature Engineering & Data cleaning: Handling outliers & missing values, encoding categorical variables, Feature Selection
3. Model Building: Training various ML algorithms on the Transformed dataset. I used following ML algorithms
    * Linear regression
    * Lasso & Ridge regression
    * SVR
    * Decision Tree
    * Random Forest
    * Gradient Boost
    * XGBoost
    * Stacking model: A combination pf Linear, Ridge, SVR, Random Forest, Gradient Boost & XGBoost regressors.
Stacked model performed the best (**87.11% r2 score**) which I've used for prediction in the Webapp.

## Packages/Libraries
* Sklearn
* Pandas
* Xgboost
* Streamlit

## Installation
The Code is written in Python 3.8. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
Then run the following command which runs the Webapp locally:
```
streamlit run app.py
```
That's it!!

## To Do
* This is 2017 dataset which is quite old for today's market. Maybe I can collect data for 2022 and build an updated webapp for the same.

## Contact
If you have suggestions for improvement or any other query, you can reach me at following platform:
  * [Linkedin](https://www.linkedin.com/in/rahul-menon-515702a7/)
