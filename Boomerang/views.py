from django.shortcuts import render

 # Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

sentiment = 0
text = 0
entity = 0

def Boomerang_entertext(request):
    if request.method == 'POST':
        if request.POST.get('submittext'):
            global text
            text = request.POST.get('text')
            entity_api(text)
            sentiment_api(text)
    return render(request, 'enterText.html')

def sentiment_api(text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    global sentiment
    sentiment = client.analyze_sentiment(document=document)


def Boomerang_analysis(request):
    while sentiment == 0:
        pass

    neu, pos, neg = 0, 0, 0
    sentimentTypeCount = [neu, pos, neg]

    for sentence in sentiment.sentences:
        if -0.2 > sentence.sentiment.score:
            sentimentTypeCount[2] += 1
        elif 0.2 < sentence.sentiment.score:
            sentimentTypeCount[1] += 1
        else:
            sentimentTypeCount[0] += 1

    arr = [sentiment, text, sentimentTypeCount, entity]
    return render(request, 'Analysis.html', {"arr": arr})

def entity_api(text):
    document = {"content": text, "type": enums.Document.Type.PLAIN_TEXT}
    client = language.LanguageServiceClient()
    # Available values: NONE, UTF8, UTF16, UTF32
    response = client.analyze_entities(document, encoding_type=enums.EncodingType.UTF8)

    global entity 
    ten = 0
    entity = {'name':[], 'salience':[]}
    # Loop through entitites returned from the API
    for en in response.entities:
        ten += 1
        entity['name'].append(en.name)
        entity['salience'].append(en.salience)
        if ten == 10:
            break
