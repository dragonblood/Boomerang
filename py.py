from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import argparse

text = 'first of all, I love noodles, Manchurians Chinese food in general. They are spicy and they have umami flavor. on the topic of flavor, I think bitter is the most underrated taste of them all. It is very rich and it makes you think, its a very human flavor. I dont think animals love bitter and even most of humans hate it. '
document = {"content": text, "type": enums.Document.Type.PLAIN_TEXT}
client = language.LanguageServiceClient()
response = client.analyze_entities(document, encoding_type=enums.EncodingType.UTF8)

entity = {'name':[], 'salience':[]}

for en in response.entities:
    entity['name'].append(en.name)
    entity['salience'].append(en.salience)

print(entity)