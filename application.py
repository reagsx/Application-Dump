import gspread
import discord
from oauth2client.service_account import ServiceAccountCredentials
import pickle
import os

# Settings
path_to_pickle = r"/home/scripts/pickle.pickle"
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


# Create Pickle if does not exist or Load last number of rows
if not os.path.exists(path_to_pickle):
    old_num_rows = row_count
    with open(path_to_pickle, "wb") as output_file:
        pickle.dump(row_count, output_file)
else:
    with open(path_to_pickle, "rb") as input_file:
        old_num_rows = pickle.load(input_file)
        print('Loading old rows...')


# if new row, update rows and output info, assumes 1 submits or less between runs
if old_num_rows < row_count:

    with open(path_to_pickle, "wb") as output_file:
        pickle.dump(row_count, output_file)

    client = discord.Client()

    for i in range(row_count - old_num_rows, 0, -1):
        print('Counting Row:' + str(i-1))

    @client.event
    async def on_ready():
        print('client ready')

        for i in range(row_count - old_num_rows, 0, -1):
            current_row = row_count - (i-1)
            print('Printing Row: ' + str(current_row))
            last_row_values = sheet.row_values(current_row)
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

        print('Complete. Exiting')
        exit(0)


    client.run("*******")
