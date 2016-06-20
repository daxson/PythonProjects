import xml.etree.ElementTree as ET

tree = ET.parse("getprojectxml.xml")

root = tree.getroot()

for Level_1 in root.findall("Folder"):
    for Level_2 in Level_1.findall("Document"):
        docID = Level_2.findall("docID")[0].text #This findall should only return one ID
        docName = Level_2.findall("documentName")[0].text #This findall should only return one ID
        for Level_3 in Level_2.findall("Annotations"):
            layerName = Level_3.findall("layerName")[0].text
            owner = Level_3.findall("setOwner")[0].text
            for Level_4 in Level_3.findall("ElementAndPhotos"):
                for element in Level_4.findall("Element"):
                    annoGUID = element.findall("annoGUID")[0].text
                    dateCreated_list = element.findall("dateCreated")[0].text.split(' ', 1)[0].split('-', 2)
                    dateCreated = dateCreated_list[1] + '-' + dateCreated_list[2] + '-' + dateCreated_list[0]
                    try:
                        unit = element.findall("userField1")[0].text
                    except:
                        unit = ''
                for elementPhoto_data in Level_4.findall("elementPhotos-data"):
                    for photo in elementPhoto_data:
                        photoID = photo.find("id").text
                        annoPID = photo.find("fk").text
                        photoURL = photo.find("photoURL")
                        print(docID, docName, layerName, owner, unit, dateCreated, annoGUID, annoPID, photoID, photoURL.text, photoURL.attrib['name'], sep=", ")
