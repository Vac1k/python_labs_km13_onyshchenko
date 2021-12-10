import json

with open('image_info_test-dev2017.json') as f:
    data = json.load(f)


for i,v in data.items():
    if i == 'images':
        print("Quantity of images: ",len(v))
        c = -1
        for j in v:
            if j["file_name"] == "000000000001.jpg":
                print('Filename :', j["file_name"],'height:' , j['height'],'width:' , j['width'],'id:' , j['id'] )

            if int((j["file_name"].split('.'))[0])>c:
                c = int((j["file_name"].split('.'))[0])
        print("Max number:",c)
    if i == 'categories':
        print("Quantity of categories: ",len(v))


#person_dict = json.loads(data)
#print(person_dict[0])

