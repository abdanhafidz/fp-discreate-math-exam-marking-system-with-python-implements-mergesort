import os

def showFile():
    directory = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(directory)
    files_data = []
    for x in files:
        if(x != '__pycache__' and x!='__init__.py' and  x!='readerfiles_repository.py' and x!='kunci_jawaban.py'):
            files_data.append(x)
    return files_data
            
