import sys
sys.path.insert(0, r'C:\Users\Brow54J\GitHub\Repositories\Prompt-VaR-Indicator')
sys.path.insert(0, r'C:\Users\Brow54J\GitHub\Repositories\Prompt-VaR-Indicator\Prompt_NOP_Tool')
sys.path.insert(0, r'C:\Users\Brow54J\GitHub\Repositories\Prompt-VaR-Indicator\tests')
import toml

def load_config(strConfigFP):
    '''load parameters from a TOML config file'''
    configDict = toml.load(strConfigFP) #note toml.dumps(dict, filename) #returns the string to the TOML format 
    return configDict

def export_config(dictConfig, strConfigFP):
    toml.dumps(dictConfig, strConfigFP) #note toml.dumps(dict, filename) #returns the string to the TOML format 
    print('successfully updated the config file with new settings')