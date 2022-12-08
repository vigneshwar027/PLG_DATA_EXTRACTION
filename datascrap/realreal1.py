import glob, os, sys
from os.path import join
import re
import time
from datetime import date, datetime
from time import strptime
from dateutil import parser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import shutil
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
import pandas as pd


fdname = os.path.dirname(__file__)+'/'

# fdname="E:/Raffy/datascrap/"
#fname="vest_Women_Accessories.xlsx"
fname="All_files/test_vest1.xlsx"
df = pd.read_excel('test_vest1.xlsx')
#print(df)


    
browser.close()
os.startfile('alarm.mp3')