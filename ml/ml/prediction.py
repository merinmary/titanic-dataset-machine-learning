def pre(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x=[[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest=pickle.load(open(r"C:\Users\MERIN MARY\Desktop\project\ml\ml\titanic_model.sav","rb"))
    predictions=randomforest.predict(x)
    if(predictions==1):
        return "survived"
    else:
        return " Not survived"
   