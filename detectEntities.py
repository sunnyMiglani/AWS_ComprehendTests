import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')
textFile = open("much_ado_about_nothing.txt", "r", encoding="utf8");
text = textFile.read();



print('Calling DetectEntities')
stringResponse = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4) # type string
dictResponse = json.loads(stringResponse);
listOfEntities = [];
listOfDefines = [];
for entity in dictResponse['Entities']:
    listOfEntities.append(entity['Text']);
    listOfDefines.append(entity['Type']);
    print("Entity : {0}, Type : {1}".format(entity['Text'], entity['Type']));

print('End of DetectEntities\n')

