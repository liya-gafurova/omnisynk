from typing import List
from monkeylearn import MonkeyLearn
import json
from zeep import Client
import  requests

def get_keywords_from_description(description : str, number_keywords = 5) -> List[str]:
    ml = MonkeyLearn('c3e523c989d56faa8e968f6881a0269fe6f5dc09')
    model_id_for_key_word_distraction = 'ex_YCya9nrn'

    response_body_str = ml.extractors.extract(model_id= model_id_for_key_word_distraction,
                                              data=[description]).body

    keywords = []
    for res in response_body_str:
        keywords.extend([kw['parsed_value'] for kw in res['extractions']])
    return keywords[:number_keywords]



def get_grants_from_WSDL_api():

    wsdl = "https://ws07.grants.gov:443/grantsws-applicant/services/v2/ApplicantWebServicesSoapPort?wsdl"
    client = Client(wsdl)
    params = {
        'OpportunityFilter' : {
            'FundingOpportunityNumber' : 'ED-GRANTS-012720-001',
        },
    }

    res = client.service.GetOpportunityList(**params)
    print(res)


def format_params_str(keywords):
    return '%20'.join(keywords)


def send_request(keywords: dict):
    url = "https://www.grants.gov/grantsws/rest/opportunities/search/"


    params = {"startRecordNum": 0, "keyword": "", "oppNum": "", "cfda": "", # ED-GRANTS-012720-001
                          "oppStatuses": "forecasted|posted"}

    params['keyword'] = format_params_str(keywords)
    payload = json.dumps(params)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response

