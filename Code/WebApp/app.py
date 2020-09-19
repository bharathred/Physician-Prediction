import flask
import pickle
import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler
logging.basicConfig(level=logging.INFO)
def scaling(x_set):
    scaler = StandardScaler()
    scaler.fit(x_set)
    x_set = scaler.transform(x_set)
    return x_set 
# Use pickle to load in the pre-trained model
def getAns(age,gender,s1,s2,s3,s4):
    logging.info('Age: '+str(age)+'Gender: '+str(gender))
    def model():
        models = []
        with open('lr_models.pckl','rb',) as f:
            while True:
                try: 
                    models.append(pickle.load(f))
                except:
                    break
        return models
    from sklearn.preprocessing import StandardScaler
    def scaling(x_set):
        scaler = StandardScaler()
        scaler.fit(x_set)
        x_set = scaler.transform(x_set)
        return x_set
    # array = [ ['1','1','35','41','11','1'] ]
    # array = [['2','1','33','35','1','41']]
    array = [[str(age),str(gender),str(s1),str(s2),str(s3),str(s4)]]
    X_test = array
    X_test = scaling(array)
    models = model()
    ans = 0
    idx = 0
    allprob = []
    cols = ['Allergist','Endocrinologist','General Physician','Cardiologist','Gastroenterologist','nephrologist','neurologist','Pediatrician','Psychiatrist','Pulmonologist','Rheumatologist']
    # cols = ['Allergist','Endocrinologist','General Physician','cardiologist','gastroenterologist','nephrologist','neurologist','rheumatologist','psychiatrist','pulmonologist']
    for i in range(len(models)):
        # ans.append(models[i].predict_proba(X_test)[0]),
        temp = models[i].predict_proba(X_test)[0][0]
        allprob.append(temp)
        if ans < temp:
            ans = temp 
            idx = i
    logging.info('IDX: '+str(idx))
    if idx==7 and (int(age)>1):
        search = sorted(allprob,reverse=True)[1]
        logging.info('Search Value '+ str(search))
        for i in range(len(allprob)):
            logging.info('AllProb '+str(allprob[i])+' ::' +str(i))
            if allprob[i] == search and i!=3:
                return cols[i]

    return cols[idx]
# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')


#Doctors CSV
Data = pd.read_csv('new.csv')
def getDocs(specs,loc):
    subData = Data[Data['Location']==loc]
    microData = subData[subData['Specialization']==specs]
    microData.sort_values(by=['Rating'],inplace=True,ascending=False)
    if len(microData.values.tolist()) > 5:
        return microData.head().values.tolist()
    return microData.values.tolist()
# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        age = flask.request.form['age']
        Gender = flask.request.form['Gender']
        S1 = flask.request.form['S1']
        S2 = flask.request.form['S2']
        S3 = flask.request.form['S3']
        S4 = flask.request.form['S4']
        location = flask.request.form['Location']
        # logging.info('Input'+age+ Gender+ S1+S2+S3+S4)
        prediction = getAns(age,Gender,S1,S2,S3,S4)
        logging.info('Pediction: '+prediction)
        Docs = getDocs(prediction,location)
        dict_age = {0:'Below 5 Years',1: '5 to 15 Years',2:'15 to 40 Years',3:'40 Years and above'}
        dict_gender = {0:'Male',1:'Female'}
        # logging.info(str(Docs[0][0]))
        dict_sym = {0: "hallucinations auditory" , 1: "sleeplessness" , 2: "feeling suicidal" , 3: "motor retardation" , 4: "feeling hopeless" , 5: "fever" , 6: "fall" , 7: "unresponsiveness" , 8: "lethargy" , 9: "cough" , 10: "sore throat" , 11: "wheezing" , 12: "shortness of breath" , 13: "orthopnea" , 14: "jugular venous distention" , 15: "rale" , 16: "hyperkalemia" , 17: "chest pain" , 18: "heme positive" , 19: "abdominal pain" , 20: "vomiting" , 21: "disequilibrium" , 22: "nightmare" , 23: "transsexual" , 24: "achalasia" , 25: "stiffness" , 26: "withdrawal" , 27: "asthenia" , 28: "numbness" , 29: "nausea" , 30: "awakening early" , 31: "oliguria" , 32: "chest tightness" , 33: "pain" , 34: "drool" , 35: "agitation" , 36: "rhonchus" , 37: "increased energy" , 38: "irritable mood" , 39: "seizure" , 40: "enuresis" , 41: "slurred speech" , 42: "breath-holding spell" , 43: "decreased body weight" , 44: "decreased translucency" , 45: "increased worry" , 46: "paraparesis" , 47: "slowing of urinary stream" , 48: "extreme exhaustion" , 49: "dyspnea" , 50: "hypokinesia" , 51: "hemodynamically stable" , 52: "hypersomnolence" , 53: "verbal auditory hallucinations" , 54: "hypotension" , 55: "hypocalcemia result" , 56: "hallucinations visual" , 57: "polyuria" , 58: "polydypsia" , 59: "catatonia" , 60: "snore" , 61: "diarrhea" , 62: "dysuria" , 63: "hematuria" , 64: "renal angle tenderness" , 65: "burning sensation" , 66: "hyponatremia" , 67: "fatigue" , 68: "uncoordination" , 69: "snuffle" , 70: "dizziness" } 
        return flask.render_template('main.html',
                                     original_input={'Age':dict_age[int(age)],
                                                     'Gender':dict_gender[int(Gender)],
                                                     'S1':dict_sym[int(S1)],'S2':dict_sym[int(S2)],'S3':dict_sym[int(S3)],'S4':dict_sym[int(S4)],'Location': location},
                                     result=Docs,
                                     )

if __name__ == '__main__':
    app.run()