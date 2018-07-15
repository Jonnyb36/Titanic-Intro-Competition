from os import path, makedirs
#import sys
import logging #https://docs.python.org/3/library/logging.html 

def logInfo(logFP, logFN, msg):        
    ''' use logging package to log info to output file '''
    print(msg)
    if not path.exists(logFP): makedirs(logFP) #check that log folder path exists
    #check if log file exists and writeable, if false then create it
    fullLogFP = path.join(logFP, logFN)
    try:
        open(fullLogFP, 'x')    
    except FileExistsError:
        pass
    #append the log info to the file
    logging.basicConfig(level=logging.DEBUG, filename=fullLogFP, filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s") 
    logging.info(msg)
    
def logError(logFP, logFN, msg):        
    ''' use logging package to log info to output file '''
    print(msg)
    if not path.exists(logFP): makedirs(logFP) #check that log folder path exists
    #check if log file exists and writeable, if false then create it
    fullLogFP = path.join(logFP, logFN)
    try:
        open(fullLogFP, 'x')    
    except FileExistsError:
        pass
    #append the log info to the file
    logging.basicConfig(level=logging.DEBUG, filename=fullLogFP, filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s") 
    logging.error(msg)  