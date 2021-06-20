import os

def ML():
        os.system("tput setaf 1")
        print("\n\t.....warning !!!! user should have sklearn and joblib pre-installed ,\n\
                if it is not then use \n\
                'pip3 install sklearn' & \n\
                'pip3 install joblib'(as a pre-requisite).... ")
        os.system("tput setaf 5")
        input("\nplz enter ur CSV File Name(with extension) as a dataset to use ML\n\
                (linear regression) to create model and predict the things : ")
        import joblib
        model=joblib.load("/pythonws/ML/salary.pkl")
        os.system("tput setaf 4")
        exp=input("\nEnter ur experience(in years) to predict salary : ")
        predicted_value=model.predict([[int(exp)]])
        os.system("tput setaf 6")
        print("\n\t\tPredicted Value : ",predicted_value)
        os.system("tput setaf 2")
        print("\n\n\tthis result is ur predicted salary in ml linear regression model")
        os.system("tput setaf 7")

