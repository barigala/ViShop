import inspect
import logging
import os

import allure


def customLogger():
    # 1.) This is used to get the  class / method name from where this customLogger method is called
    logName = inspect.stack()[1][3]

    # 2.) Create the logging object and pass the logName in it
    logger = logging.getLogger(logName)

    # 3.) Set the Log level
    logger.setLevel(logging.DEBUG)

    # 4.) Create the fileHandler to save the logs in the file, 'w' is given so that the logs will reset for every run, input 'a' to store all logs without resetting
    #fileHandler = logging.FileHandler("../reports/testreport.log", mode='w')

    log_directory = "../reports"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    fileHandler = logging.FileHandler(os.path.join(log_directory, "testreport.log"), mode='w')

    # 5.) Set the logLevel for fileHandler
    fileHandler.setLevel(logging.DEBUG)

    # 6.) Create the formatter in which format do you like to save the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # 7.) Set the formatter to fileHandler
    fileHandler.setFormatter(formatter)

    # 8.) Add file handler to logging
    logger.addHandler(fileHandler)

    #  9.) Finally return the logging object

    return logger


def allureLogs(text):
    with allure.step(text):
        pass
