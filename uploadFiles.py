import dropbox
import os
class UploadFiles:
       def __init__(self, access_token,upload_file):
        self.access_token = access_token
        self.upload_file = upload_file
     

def uploadFiles(self, file_from, file_to,local_path,upload_file):
    for root, dirs, files in os.walk(file_from):
        relative_path = os.path.relpath(local_path , file_from)
        dropbox_path = os.path.join(file_to, relative_path)
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.BIzzYYXQNLCzdR8RA4nmfyfiXSZqFvafpsr5__7OrjrJPaxnJnO1FPH0SxY_c2iOAGGCUL6FN3yL2DGvxxi6iIEYa9tOQwg_CPu3mJxZ3IzPfkdOF__kl11UJli2uIXjjwQHVftQ'
    transferData = UploadFiles(access_token)

    file_from = 'C101.py'
    file_to = '/python/C105.py'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()






           
 

      
      
      
      
      


