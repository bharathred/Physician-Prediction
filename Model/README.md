# Models

This code consists of the creation and testing of predictive models used for the **first phase** of the project. Both the **Logistic Regression** and **Random Forest** models are implemented in a *One vs Rest* manner. 
Used the python library *sklearn* for implementation - 

```from sklearn.linear_model import LogisticRegression```

 ```from sklearn.ensemble import RandomForestClassifier ```

These models output a list of type of doctors (pediatrician, psychiatrist, etc.) and their probabilities to diagnose a patient (test case). Both the models are stored in a pickle file for further usage.
