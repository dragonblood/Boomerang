from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

 # Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

sentiment = 0
text = 0

def Boomerang_entertext(request):
    api_call(request)
    return render(request, 'enterText.html')

def api_call(request):
    if request.method == 'POST':
        if request.POST.get('submittext'):
            print('hihihih')
            global text
            text = request.POST.get('text')
            
            # Instantiates a client
            client = language.LanguageServiceClient()

            # The text to analyze
            document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

            # Detects the sentiment of the text
            global sentiment
            sentiment = client.analyze_sentiment(document=document)


# def printer(text, sentence):
#     print('Text: {}\n'.format(text))
#     print('Overall Sentiment\n')
#     print('Sentiment Score', sentiment.document_sentiment.score)
#     print('Sentiment Magnitude', sentiment.document_sentiment.magnitude)

#     for sentence in sentiment.sentences:
#         print(sentence.text)
#         print('Sentiment Score',sentence.sentiment.score)
#         print('Sentiment Magnitude',sentence.sentiment.magnitude)

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

    print(sentimentTypeCount)
    arr = [sentiment, text, sentimentTypeCount]
    return render(request, 'Analysis.html', {"arr": arr})
