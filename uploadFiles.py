import os
import dropbox




class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)                   
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                  
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BI6Z9VE32y15TlqyUxm_-F0pXFrDs5Hh8079ECX-qHTrjokXsxGsKBRDfxUN6Q1pyHOD5SlIAy0TJNvSjCSR7EGzKLn7-11-9F2lWU7X--nEGhDgfK_W1Gw9eRn8iUTIFeLfELFW'
    transferData = TransferData(access_token)

    file_from = 'pro2.py'
    file_to = '/python/pro2.py'  

 
    transferData.uploadFile(file_from,file_to)
    print("moved")

if __name__ == '__main__':
    main()
