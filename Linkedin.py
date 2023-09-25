from selenium import webdriver
from functions import LoginSite,Search,Connect,ChangeTab


class LinkedIn:

    def __init__(self,site,Adjective):
        self.UserInfo = Adjective().GetLogin()
        self.user = self.UserInfo[0]
        self.password = self.UserInfo[1]
        self.site = site
        self.adjective = Adjective().GetProfession()
        self.driver = webdriver.Chrome()
    

    def Login(self):
        self.driver.get(self.site)
        self.driver.maximize_window()
        LoginSite(self.driver,self.user,self.password)
        Search(self.driver,self.adjective)
        for counter in range(0,101):
            Connect(self.driver,App)
            ChangeTab(self.driver,counter)


import tkinter as tk


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("LinkedIn Profile Search")
        self.value = ''
        self.User = ""
        self.Password = ''

    def GetLogin(self):
        # Create an Label field
        self.window.geometry('300x200')
        self.label = tk.Label(self.window, text="Enter you E-mail")
        self.label.pack()

        # Create an Entry field
        self.UserEntry = tk.Entry(self.window)
        self.UserEntry.pack()

        self.label = tk.Label(self.window, text="Enter you Password")
        self.label.pack()

        # Create an Entry field
        self.passwordEntry = tk.Entry(self.window)
        self.passwordEntry.pack()

        # Create a button
        button = tk.Button(self.window, text="Submit", command=self.UserInfo)
        button.pack()

        self.window.mainloop()
        return self.User,self.Password


    def GetProfession(self):
        self.label = tk.Label(self.window, text="Write the name of profession of the People you are looking for")
        self.label.pack()

        # Create an Entry field
        self.profession = tk.Entry(self.window)
        self.profession.pack()

        # Create a button
        button = tk.Button(self.window, text="Submit", command=self.Profession)
        button.pack()

        self.window.mainloop()
        return self.value


    def Profession(self):
        self.value = self.profession.get()
        self.window.destroy()


    def UserInfo(self):
        self.User = self.UserEntry.get()
        self.Password = self.passwordEntry.get()
        self.window.destroy()
    

    
    def ConnectionLimit(self):
        self.label = tk.Label(self.window, text='We will finish the process, because of the alert "limit Week Connection"')
        self.label.pack()

        # Create a button
        button = tk.Button(self.window, text="OK", command=self.window.destroy)
        button.pack()

        self.window.mainloop()



Run = LinkedIn("https://www.linkedin.com/",App)
Run.Login()
