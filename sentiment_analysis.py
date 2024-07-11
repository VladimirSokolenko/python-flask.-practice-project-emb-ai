import requests
from requests.auth import HTTPBasicAuth

def sentiment_analyzer(text_to_analyse):
    # url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    url = 'https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/539dad39-1942-4c5b-b421-9e2b845e4450'
    # myobj = { "raw_document": { "text": text_to_analyse } }
    myobj = {"text": text_to_analyse,"features":{"sentiment": {"document":"true"}}}
    auth = HTTPBasicAuth('apikey', 'Hr1P2YsklytsPAUuCSwxBpr6JWNRd3r41lxvFOIc2Ktu')
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url + '/v1/analyze?version=2019-07-12', json = myobj, headers=header, auth=auth)
    return response.text