We look at the concept of Model Tuning & Calibration using a UCI Credit Card prediction dataset

Data: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients

Model Tuning & Calibration:

    • Use of stratified sampling
    • Finding the best probability cut off for the class using a metric e.g. Based on F1 Score
    • Calibration -> Reliability curve, Platt Scaling   & Isotonic Regression (usually used of larger dataset)
    • Hyper-parameter tuning -> Using Randomised SearchCV which is then used as to narrow down the best parameters using GridSearchCV
    
We perform the below steps
    • Load the data
    • Basic data processing
    • Build a Random Forest model 
    • Inspect the probability using a reliability curve
    • Use of Hyper parameter tuning

Why Calibration?

Probability calibration is necessary if the required output is the true probability returned from a classifier and is critical to the problem at hand. This is not the case if the required output from a classifier is the ranking or say the user is only interested in a binary class form. 

The overall model can further be improved by feature engineering, use of various machine learning algorithms & other hyper parameter tuning approaches amongst other things.
