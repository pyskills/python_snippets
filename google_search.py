import pprint
from googleapiclient.discovery import build

my_api_key = "APIKEY"
my_cse_id = "CUSTOM SEARCH ID"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
