_author__ = 'sin'
import easygui
from GdataEntry import *
class WebPage(object):

    def login(self):
        gde = GdataEntry()
        password = easygui.passwordbox("What is your password ?")
        if gde.checkEntry(password1=password)==True:
            easygui.msgbox("Welcome to the page")
        else:
            easygui.msgbox("Incorrent Password")

my_login = WebPage()
my_login.login()




