import json
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
text = 'I love this new technology.'
# text = "This is fun."
# text = 'I love working with Python'  # “SENT_POSITIVE”
# text = 'I hate working with Pyhton'  # “SENT_NEGATIVE”
# text = 'I am neutral on Python' #“SENT_NEUTRAL”

response = sentiment_analyzer(text)


# for not formated response
# formatted_response = json.loads(response)
# label = formatted_response['sentiment']['document']['label']
# score = formatted_response['sentiment']['document']['score']
# language = formatted_response['language']
# print(formatted_response['sentiment'])
# print(f'Document language: {language}')
# print(f'Document sentiment label: {label}')
# print(f'Document sentiment score: {score}')

# for formated response
label = response['label']
score = response['score']
print(f'Analysed text: \"{text}\"')
print(f'Response: {response}')
print(f'Document sentiment label: {label}')
print(f'Document sentiment score: {score}')
