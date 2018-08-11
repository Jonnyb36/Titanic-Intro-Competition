
import pandas as pd
import toml
from os import path, makedirs
import seaborn as sns
import matplotlib.pyplot as plt

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

    dfTrain = pd.read_csv(path.join(dictGlobal['inputFP'],dictGlobal['trainFN']))
    dfTrain.info()
    print(dfTrain.head())
    #891 rows.  Age only 714 rows.  Cabin only 204 rows.

    dfClean = dfCombined[['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']]

    sns.pairplot(dfClean, hue='Survived', kind='reg')
    plt.show()

    sns.lmplot(x='Pclass', y='Survived', data=dfCombined)
    sns.lmplot(x='Pclass', y='Survived', data=dfCombined, col='Sex')
    sns.lmplot(x='Pclass', y='Survived', data=dfCombined, row='Sex')
    plt.show()

    sns.jointplot(x='Pclass',y='Survived',data=dfCombined)
    plt.show()


    
    outputFP = dictConfig['testing']['outputFP'] if testing else dictGlobal['outputFP']

if __name__ == '__main__':
    configFN = r'C:\Users\Brow54J\Kaggle\Titanic-Intro-Competition\config.toml'
    run_tool(configFN, True)