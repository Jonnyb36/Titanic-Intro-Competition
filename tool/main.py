
from pandas import read_csv
import toml
from os import path, makedirs

def run_tool(configFN, testing=False):
    
    dictConfig = toml.load(configFN)
    dictGlobal = dictConfig['global']

    dfGender = read_csv(path.join(dictGlobal['inputFP'],dictGlobal['genderFN']))
    dfGender.info()
    print(dfGender.head())
    dfTest = read_csv(path.join(dictGlobal['inputFP'],dictGlobal['testFN']))
    dfTest.info()
    print(dfTest.head())
    dfTrain = read_csv(path.join(dictGlobal['inputFP'],dictGlobal['trainFN']))
    dfTrain.info()
    print(dfTrain.head())
    outputFP = dictConfig['testing']['outputFP'] if testing else dictGlobal['outputFP']

if __name__ == '__main__':
    configFN = r'C:\Users\Brow54J\Kaggle\Titanic-Intro-Competition\config.toml'
    run_tool(configFN, True)