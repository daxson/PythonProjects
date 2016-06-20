# File Cataloge
# This script will grab all file names, types, and locations and create a csv file in the parent directory
# of the files being grabbed
#
# By: Daniel Axson
#


import os

rootdir = os.cwd()

serverPath = "\\\\wjeaus\\projects"

def checkfiletype(mySTR):
    filetypelist = [".JPG", ".jpg", ".AVI", "s.db", ".mp4", ".ini"]
    if mySTR[-4:] in filetypelist:
        return False
    else:
        return True

ownerdict = {'DPA': 'daxson', 'MPC': 'mcarlton', 'EJM': 'emurray', 'ADG': 'agelsone', 'BSB': 'bboaz', 'JTR': 'jrussell'}

with open("directoryList.csv","w") as f:
    for photodir in os.listdir(rootdir):
        #print(photodir)
        try:
            if photodir.find("2016") != -1 or photodir.find("2015") != -1:
                if checkfiletype(photodir) == True:
                    print(os.path.join(serverPath,os.path.join(rootdir,photodir)[2:]), end=', ')
                    print(photodir[-3:], end=', ')
                    ownerini = photodir[-3:]
                    if photodir[-3:] in ownerdict:
                        ownerpid = ownerdict[photodir[-3:]]
                    else:
                        ownerpid = ''
                    print(ownerpid)
                    f.write(os.path.join(serverPath,os.path.join(rootdir,photodir)[2:] +
                                         ', ' + ownerini + ', ' + ownerpid + "\n"))
                for subdir in os.listdir(os.path.join(rootdir,photodir)):
                    try:
                        #if subdir.find(".JPG") == -1:
                        if checkfiletype(subdir) == True:
                            print(os.path.join(serverPath, os.path.join(rootdir, os.path.join(photodir, subdir))[2:]), end=', ')
                            print(subdir, end=', ')
                            print(ownerini, end=', ')
                            print(ownerpid)
                            f.write(os.path.join(serverPath,os.path.join(rootdir, os.path.join(photodir, subdir))[2:] +
                                                 ', ' + ownerini + ', ' + ownerpid + "\n"))
                    except:
                        pass
        except:
            pass

