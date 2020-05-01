import gspread 
from google.colab import auth
from oauth2client.client import GoogleCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import pandas as pd

def getSpreadsheetAuth(): 
  auth.authenticate_user()
  spreadsheetAuth=gspread.authorize(GoogleCredentials.get_application_default())
  return spreadsheetAuth

def getSpreadsheet(spreadsheetUrl,sheetName):
    spreadsheetAuth=getSpreadsheetAuth()
    sheet=spreadsheetAuth.open_by_url(spreadsheetUrl)
    frame=get_as_dataframe(sheet.worksheet(sheetName))
    frame=frame.dropna(how='all')
    frame=frame.dropna(axis='columns',how='all')
    return frame

