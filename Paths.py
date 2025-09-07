import os, shutil, json, sys
isCompile = hasattr(sys, "frozen")
def getDirName(path):
    return os.path.dirname(os.path.normpath(path))

def join(path1, path2):
    return os.path.join(os.path.normpath(path1), os.path.normpath(path2))
def getFromRoot(path):
    if isCompile:
        return join(sys._MEIPASS, path)
    return join(os.path.dirname(os.path.abspath("main.py")), path)
def getAssetPath(path):
    return join(getFromRoot("assets"), path)
def getTempPath(path):
    return join(getFromRoot("temp"), path)
def getFileName(path) -> str:
    return os.path.basename(path)
def exists(path):
    if path is None:
        return False
    return os.path.exists(os.path.normpath(path))

def createFolder(path):
    if not os.path.isdir(os.path.normpath(path)):
        os.mkdir(path)
def deleteFolder(path):
    shutil.rmtree(os.path.normpath(path))
def rename(ogPath, path):
    os.rename(os.path.normpath(ogPath), os.path.normpath(path))
def createFile(path, content):
    with open(path, "w") as file:
        file.write(content)

def getJsonData(path) -> dict:
    data = {}
    with open(path) as file:
        data = json.load(file)
    return data
def saveJson(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
def copyFile(filePath, copyfilePath):
    filePath = os.path.normpath(filePath)
    copyfilePath = os.path.normpath(copyfilePath)
    if filePath == copyfilePath:
        return
    shutil.copyfile(filePath, copyfilePath)

def listFolder(path) -> list[str]:
    path = os.path.normpath(path)
    if not os.path.isdir(path):
        return []
    return os.listdir(path)

def isDir(path) -> bool:
    return os.path.isdir(os.path.normpath(path))