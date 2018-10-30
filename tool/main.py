
import pandas as pd
import numpy as np
import toml
from os import path, makedirs
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model

def run_tool(configFN, testing=False):
    
    dictConfig = toml.load(configFN)
    dictGlobal = dictConfig['global']

    #get passenger survived - PassengerID, Survived
    dfGender = pd.read_csv(path.join(dictGlobal['inputFP'],dictGlobal['genderFN']))
    dfGender.info()
    print(dfGender.head())
    #get passenger detailed info - 'PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
    dfTest = pd.read_csv(path.join(dictGlobal['inputFP'],dictGlobal['testFN']))
    dfTest.info()
    print(dfTest.head())
    #join whether survived to passenger detailed info
    dfCombined = pd.merge(dfGender, dfTest, how='inner', on='PassengerId')
    print(dfCombined.head())
    #418 rows.  Age 332 rows, Fare 417 rows, Cabin 91 rows

    dfTrain = pd.read_csv(path.join(dictGlobal['inputFP'],dictGlobal['trainFN'])).dropna()
    dfTrain.info()
    print(dfTrain.head())
    #891 rows.  Age only 714 rows.  Cabin only 204 rows.

    dfCleanTest = dfCombined[['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked', 'Age']].dropna()

    '''
    sns.pairplot(dfClean, hue='Survived', kind='reg')
    plt.show()

    sns.lmplot(x='Pclass', y='Survived', data=dfCombined)
    sns.lmplot(x='Pclass', y='Survived', data=dfCombined, col='Sex')
    sns.lmplot(x='Pclass', y='Survived', data=dfCombined, row='Sex')
    plt.show()

    sns.jointplot(x='Pclass',y='Survived',data=dfCombined)
    plt.show()
    '''

    #Linear Regression
    reg = linear_model.LinearRegression()

    Y_train = dfTrain.Survived
    PredResults = dfCleanTest['Survived']

    #Age classification
    feature_X_train = dfTrain.Age.as_matrix().reshape(-1,1) #convert to numpy array
    feature_X_test = dfCleanTest.Age.as_matrix().reshape(-1,1)

    reg.fit(feature_X_train, Y_train)

    survived_predict = reg.predict(feature_X_test)
    print(survived_predict)
    print(reg.coef_)
    
    #round everyone above 0.5 as survived
    dfCleanTest['rawPrediction'] = survived_predict
    dfCleanTest['prediction'] = [1 if x >= 0.5 else 0 for x in survived_predict]
    dfCleanTest['predCorrect'] = (dfCleanTest['Survived']==dfCleanTest['prediction']).astype(int)
    percCorrect = sum(dfCleanTest['predCorrect'])/len(dfCleanTest['predCorrect'])

    outputFP = dictConfig['testing']['outputFP'] if testing else dictGlobal['outputFP']

if __name__ == '__main__':
    configFN = r'/Users/jonbrown/Documents/GitHub/Titanic-Intro-Competition/config.toml'
    run_tool(configFN, True)