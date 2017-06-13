from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "c:/Users/Chris/Documents/secrets/GoogleAPI.json"
SPREADSHEET = "Application (Responses)"

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = ServiceAccountCredentials(json_key['client_email'],
                                        json_key['private_key'], SCOPE)
