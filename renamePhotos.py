# File Cataloge
# This script will grab all file names, types, and locations and create a csv file in the parent directory
# of the files being grabbed
#
# By: Daniel Axson
#


import os

rootdir = os.path.join(os.getcwd(), 'shore')

ownerdict = {'DPA': 'daxson', 'MPC': 'mcarlton', 'EJM': 'emurray', 'ADG': 'agelsone', 'BSB': 'bboaz', 'JTR': 'jrussell'}

for photodir in os.listdir(rootdir):
    #print(photodir)
    try:
        if photodir.find("2016") != -1 or photodir.find("2015") != -1:
            #print(photodir)
            for Level_2 in os.listdir(os.path.join(rootdir, photodir)):
                #print(Level_2)
                try:
                    Level_2_path = os.path.join(rootdir,photodir,Level_2)
                    #print(Level_2_path)
                    for Level_3 in os.listdir(Level_2_path):
                        #print(Level_3[-3:])
                        Level_3_path = os.path.join(rootdir, photodir, Level_2, Level_3)
                        if Level_3[0:6] == '(null)' and Level_3[-3:] != '.jpg':
                            print(Level_3_path)
                            #os.rename(Level_3_path, Level_3_path + ".jpg")
                except:
                    #print(Level_2)
                    pass
    except:
        pass
