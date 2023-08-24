import logging
import inspect

class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        dad_name = inspect.stack()[2][3]

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", name, dad_name)
        logger = logging.getLogger(name)

        log_file = logging.FileHandler(".//Logs//drcatalyst_ehr.png")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s :%(message)s ")
        log_file.setFormatter(log_format)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger

