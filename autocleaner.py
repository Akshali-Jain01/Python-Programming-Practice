import os
def createIfNotExist(parameters):
    if not os.path.exists(parameters):
        os.makedirs(parameters)
if __name__ =="__main__":
    files = os.listdir()
# print(files) --defined complete files of the folder of the content
    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')
    imgExts =[".png",".jpg",".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts =[".txt",".docx","doc",]
