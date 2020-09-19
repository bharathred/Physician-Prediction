# Prediction of Physicians For Patient Diagnosis 

This project provides a predictive model for selecting the most appropriate health care practitioners nearby who can diagnose a patient. It’s a two-phase project.

## Phase 1 -
First, identification of the doctors who can diagnose a patient is done. Second, probabilities are used to provide a ranking of each physician. Then the top physicians with higher probability to diagnose the patient are
picked. 

## Phase 2 -
Integration with Practo is done. For each physician, the top five specialists in each field in the nearby location from Practo’s user are identified. These specialists are filtered through web scraping on Practo.
These specialists are ranked using sentimental analysis on the reviews from the patients who previously visited them. Then the construction of a basic user interface to suggest select Practo specialists based on the results is done.

*The base data set used can be found [here](https://health.data.ny.gov/api/views/rmwa-zns4/rows.csv?accessType=DOWNLOAD).*

## Project Folder Structure 
### Model/
The code in this folder consists of the creation and testing of predictive models used for the **first phase** of the project on the data: *dataset_with_values_v_3*. Both the **Logistic Regression** and **Random Forest** models are implemented in a *One vs Rest* manner. 

The python library *sklearn* is used for implementation - 

```from sklearn.linear_model import LogisticRegression```

 ```from sklearn.ensemble import RandomForestClassifier ```

These models output a list of type of doctors (pediatrician, psychiatrist, etc.) and their probabilities to diagnose a patient (test case). Both the models are stored in a pickle file for further usage.

### Scraping/ 
This folder contains logic for scraping Practo data, and saving it in a .csv file for further usage. 
 
### WebApp/ 
This folder contains code for the web user interface built using **Flask**, which gives users access to the final output of phase 2 of the project.

## Running the Project 
### Generating data for running the web interface -
For the code in *Model/*, execute *predictive_models.ipynb* in any python notebook and modify the google drive paths as needed.
 
Now, run *profile_scraper.py*, and it’ll save doctors’ profile in doctors.csv. You can change user’s location in *line 7* of code. Doctors’ data needed is compiled from [Practo](https://www.practo.com/) 

Classes in HTML pages of [Practo](https://www.practo.com/) may change. So, correct those after inspecting the elements in a profile.

*Example: name = soup_new.find(class_="c-profile__title u-bold u-d-inlineblock")*
>$ python profile_scraper.py

*comments_scraper.py* takes doctors.csv as input and output the comments extracted from particular doctor’s profile and saves it in comments/doctorname.txt format.
>$ python comments_scraper.py

### Running the web application -
**In Linux**

*Terminal:*
> $ export FLASK_APP=./app.py
 
> $ flask run
 
**In Windows**

*Command Prompt:*
> set FLASK_APP=app.py

*Power shell:*
> $env:FLASK_APP = "app.py"

Then, open http://127.0.0.1:5000/ in web browser, input details like, *age*, *symptoms*, etc. and check the results displayed.

## Project Team -

[Bharat Sharma](https://github.com/GENU05)

[Bharath Simha](https://github.com/bharathred)

[D. Praneetha](https://github.com/Shira98)

## Major Project Under the Guidance of -

[Ananthanarayana V. S.](http://infotech.nitk.ac.in/faculty/ananthanarayana-v-s) 