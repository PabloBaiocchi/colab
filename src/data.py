import gspread 
from google.colab import auth
from oauth2client.client import GoogleCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import pandas as pd

def getSpreadsheetAuth(): 
  auth.authenticate_user()
  spreadsheetAuth=gspread.authorize(GoogleCredentials.get_application_default())
  return spreadsheetAuth

def getSpreadsheetFrame(sheet_url,sheet_name):
  spreadsheetAuth=getSpreadsheetAuth()
  sheet=spreadsheetAuth.open_by_url(sheet_url)
  frame=get_as_dataframe(sheet.worksheet(sheet_name),{float_precision='high'}) #changes here
  frame=frame.dropna(how='all')
  frame=frame.dropna(axis='columns',how='all')
  return frame

def importGoogleDriveFile(directoryCode,fileName):
  auth.authenticate_user()
  gauth = GoogleAuth()
  gauth.credentials = GoogleCredentials.get_application_default()
  drive = GoogleDrive(gauth)
  file_list = drive.ListFile({'q': f"'{directoryCode}' in parents and trashed=false"}).GetList()
  for file in file_list:
    if file['title']==fileName:
      file.GetContentFile(fileName)

def getGoogleDriveFrame(directoryCode,fileName):
  importGoogleDriveFile(directoryCode,fileName)
  return pd.read_csv(fileName)

