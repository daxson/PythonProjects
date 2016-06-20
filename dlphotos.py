
import requests
import csv
import os

rootdir = os.getcwd()

print(rootdir)

photodir = os.path.join(rootdir,"shore")

print(photodir)

pplmap = {'emurra': 'EJM', 'bboaz': 'BSB', 'daxson': 'DPA', 'jrusse': 'JTR'}

i = 0

with open('Parsed_Photo_Info.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[9].strip() != row[10].strip():
            photoName1 = row[10].strip()
            if photoName1[0:6] == '(null)' and photoName1[-3:] != '.jpg':
                photoName1 = photoName1 + '.jpg'
            pid = row[3].strip()
            unit = row[4].strip()
            if pid in pplmap.keys():
                if unit in ['None', 'Maintenance', '8th floor line', 'observed from 2202', '']:
                    path1 = os.path.join(photodir, row[5].strip() + ' ' + pplmap[pid])
                else:
                    path1 = os.path.join(photodir, row[5].strip() + ' ' + pplmap[pid], unit)

                url = "https://plannotate.me/photoalbum/index/%s" % (row[9].strip())
                print('Getting:', url)
                photo_path = os.path.join(path1, photoName1)
                if not os.path.exists(photo_path):
                    print('For:', photo_path)
                    r = requests.get(url)
                    if r.status_code == 200:
                        #create directory if return code is good
                        try:
                            os.stat(path1)
                        except:
                            print('mkdir')
                            os.makedirs(path1)

                        with open(photo_path, 'wb') as fd:
                            for chunk in r.iter_content(4096): # 4K chunks
                                fd.write(chunk)
                        print('done')
                    else:
                        print('Error getting photo:', r.status_code)
                else:
                    print('For:', photo_path)
                    print('File Exists:', photo_path)
