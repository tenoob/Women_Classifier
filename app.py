
from flask import Flask,render_template,request
import pickle

from sklearn.linear_model import OrthogonalMatchingPursuitCV

app = Flask(__name__)
model = pickle.load(open('logisticregression.pkl','rb'))

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def prediction():
    if (request.method=='POST'):
        rate = float(request.form['rate'])
        age =  int(request.form['age'])
        years  = int(request.form['yers']) 
        child = int(request.form['child'])
        relig = int(request.form['relig'])
        educ = int(request.form['edu'])
        occ = int(request.form['occ'])
        occ_husb =int(request.form['occhus'])

        occ_lst = [1 if i==occ else 0 for i in range(6) ]
        occ_lst_hus = [1 if i==occ_husb else 0 for i in range(6) ]

        occ_lst = occ_lst[1:]
        occ_lst_hus = occ_lst_hus[1:]
        
        predictors = occ_lst+occ_lst_hus
        predictors.extend([rate,age,years,child,relig,educ])
        print(occ_lst , occ_lst_hus)
        print(predictors)
        result = model.predict([predictors])

        if result[0]==1:
            ans = "Having Affair"
        else:
            ans='Not Having Affair'
        return render_template('index.html',result=ans)

if __name__=='__main__':
    app.run(debug=True)