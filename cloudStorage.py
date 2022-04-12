from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token) 
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)


def main():
    access_token="sl.BFnQ7v4W-yQ1gq1ZCJeZWihReiBNhwvm0JFhUJ_YWMG7LC5A06mYq-qhJgLWA-o2d7U5kHlaGYHQhhKZPpowU6yRwgJY7atNTXYHve7v_dHzFty057o8KynblvUS5HmmKbqLjRGWGN3B"
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transfer:")
    file_to=input("enter the full path to upload to dropbox:")
    transferData.upload_file(file_from, file_to)
    print("file has been moved")



main()