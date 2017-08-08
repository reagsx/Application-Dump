import gspread
import discord
from oauth2client.service_account import ServiceAccountCredentials
import pickle


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('GoogleAPI.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Application (Responses)").sheet1

# Extract all of the values
last_update = sheet.updated
row_count = sheet.row_count

# load old number of rows
with open(r"someobject.pickle", "rb") as input_file:
    old_num_rows = pickle.load(input_file)


# if new row, update rows and output info, assumes 1 submits or less between runs
if old_num_rows < row_count:
    last_row_values = sheet.row_values(row_count)
    print(last_row_values)
    with open(r"someobject.pickle", "wb") as output_file:
        pickle.dump(row_count, output_file)

    client = discord.Client()

    @client.event
    async def on_ready():
        await client.send_message(discord.Object(id='248968429678100480'), str
        ('**New Application:**'
         '\n **Date:** ' + last_row_values[0] +
         '\n **Name:** ' + last_row_values[1] +
         '\n **BattleTag:** ' + last_row_values[2] +
         '\n **Email:** ' + last_row_values[3] +
         '\n **Armory:** ' + last_row_values[4] +
         '\n **Can make Raid Times?:** ' + last_row_values[5] +
         '\n **Role:** ' + last_row_values[6] +
         '\n **Logs:** ' + last_row_values[7] +
         '\n **Artifact Level:** ' + last_row_values[8] +
         '\n **Spec:** ' + last_row_values[9] +
         '\n **Okay with Adult Language?:** ' + last_row_values[10] +
         '\n **Age:** ' + last_row_values[11]
         ))
        exit(0)

    client.run("*****")
