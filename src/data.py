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

def getSpreadsheet(spreadsheetUrl,sheetName):
    spreadsheetAuth=getSpreadsheetAuth()
    sheet=spreadsheetAuth.open_by_url(spreadsheetUrl)
    frame=get_as_dataframe(sheet.worksheet(sheetName))
    frame=frame.dropna(how='all')
    frame=frame.dropna(axis='columns',how='all')
    return frame

def importGoogleDriveFile(directoryCode,fileName):
  auth.authenticate_user()
  gauth = GoogleAuth()
  gauth.credentials = GoogleCredentials.get_application_default()
  drive = GoogleDrive(gauth)
  file_list = drive.ListFile({'q': "'${directoryCode}' in parents and trashed=false"}).GetList()
  for file in file_list:
    if file['title']==fileName:
      file.GetContentFile(fileName)

