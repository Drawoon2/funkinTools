import os, shutil, json

def getDirName(path):
    return os.path.dirname(os.path.normpath(path))

def join(path1, path2):
    return os.path.join(os.path.normpath(path1), os.path.normpath(path2))

def getAssetPath(path):
    return join("assets", path)

def exists(path):
    return os.path.exists(os.path.normpath(path))

def createFolder(path):
    if not exists(path):
        os.mkdir(path)

def rename(ogPath, path):
    os.rename(os.path.normpath(ogPath), os.path.normpath(path))
def createFile(path, content):
    with open(path, "w") as file:
        file.write(content)

def getJsonData(path):
    data = {}
    with open(path) as file:
        data = json.load(file)
    return data
def saveJson(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
def copyFile(filePath, copyfilePath):
    shutil.copyfile(os.path.normpath(filePath), os.path.normpath(copyfilePath))

def listFolder(path):
    return os.listdir(path)