 

import os

dropbox = 0
local_path = 0

class TransferData():
    def __init__(self,acces_token):
        self.access_token = acces_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from)

        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))


def main():
    access_token = 'sl.BCAnDBS_BtehCgk5LgWmiaP1NLx13R4YF-oNwNkfNvAayB4I10AT8VVk5t54X4nVeoxGhtkYUM4yUQe7Ca7DM9-ZycMQBQg6MSKu5Aw05YoDEmb60SrwSp4c8kBjENDgQk-CPHL32RM8'
    transfer_Data = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload the dropbox: ")

    transfer_Data.upload_file(file_from, file_to)
    print("file has been moved")


main()  

    
   