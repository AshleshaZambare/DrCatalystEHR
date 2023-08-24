import configparser

config = configparser.RawConfigParser()
filepath = ".\\Configuration\\config.ini"
config.read(filepath)

class Readconfig:
    @staticmethod
    def Getclinic():
        clinic = config.get("login info", 'clinic')
        return clinic

    @staticmethod
    def GetUsername():
        username = config.get("login info", "username")
        return username

    @staticmethod
    def Getpassword():
        password = config.get("login info", "password")
        return password





