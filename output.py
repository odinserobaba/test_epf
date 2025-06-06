import requests

# Общие параметры
AUTHORIZATION_TOKEN = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJmaXJzdE5hbWUiOiLQn9C-0LTRgNGP0LTRh9C40LoiLCJsYXN0TmFtZSI6ItCQ0J4gJ9Cm0JXQndCi0KDQmNCd0KTQntCg0JwnIiwicmVnaW9uQ29kZSI6Ijc3Iiwicm9sZSI6ImRldmVsb3BlciIsInJvbGVpZCI6IjEyIiwicGVybWlzc2lvbnMiOiJVc2VycyxSb2xlcyxOZXdzLFN0YXRpc3RpY2FsSW5mLFJldGFpbCxNYXJrZXRQYXJ0aWNpcGFudHMsUmVwb3J0cyxPcmdhbml6YXRpb25zLFJlcG9ydFRlbXBsYXRlcyxSZXRhaWwsUmV0YWlsLFJldGFpbCxSZXRhaWwsUmV0YWlsIiwibG9jYWxpdHkiOiLQnNC-0YHQutCy0LAiLCJsaXN0UmVnaW9uQ29kZXMiOiI3NyIsInJlZ2lvbiI6Ijc3IiwidXNlcmlkIjoiMTI1IiwibmJmIjoxNzQ4OTE2MjQ0LCJleHAiOjE3NDkwNDU4NDQsImlzcyI6IkNBRWdhaXMiLCJhdWQiOiJVc2VycyJ9.vW2S9KTSMeujzXyjWV0I4yMd_cf547uaTke1HJcjX_4"

COMMON_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'authorization': AUTHORIZATION_TOKEN,
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

def make_request(method, url, headers=None, cookies=None, json_data=None, params=None):
    if headers is None:
        headers = COMMON_HEADERS.copy()
    if cookies is None:
        cookies = {}

    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, cookies=cookies, params=params)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, cookies=cookies, json=json_data)
        elif method.upper() == 'PATCH':
            response = requests.patch(url, headers=headers, cookies=cookies, json=json_data)
        else:
            raise ValueError(f"Unsupported method: {method}")

        print(f"Request to {url} returned status code: {response.status_code}")
        return response
    except Exception as e:
        print(f"Failed to send request to {url}: {e}")
        return None

# Примеры использования
response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/233863/extended')

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/233863/info')

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request_new_information/233863/lic_info')

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/lic_types')

response = make_request('GET', 'https://lk-test.egais.ru/dashboard/catalog/cadastral')

response = make_request('GET', 'https://domestic-calendar.domestic.monitor-utm.ru/calendar/', params={'from': '2025-01-01', 'to': '2025-12-31'})

json_data = {
    'requestId': 233863,
    'ogrn': '310730882380772',
    'inn': '576853595470',
    'kpp': None,
    'orgActivityName': 'ИП',
    'orgNameBrief': 'ИП Попова Д. А.',
    'orgNameFull': 'Индивидуальный предприниматель Попова Дарья Алексеевна',
    'orgNameFullDative': 'Индивидуальному предпринимателю Поповой Дарья Алексеевной',
    'address': '430013, Респ. Мордовия, г. Саранск, ул. Воинова, д. 10, кв. 17',
    'region': {
        'code': '57',
        'name': 'ОРЛОВСКАЯ ОБЛ',
        'timeZone': 3,
        'active': True,
        'fiasUuid': '5e465691-de23-4c4e-9f46-f35a125b5970',
    },
    'email': 'popova-da@fsrar.ru',
    'comment': None,
    'rakrEntities': [],
    'rakrCerts': [],
    'phone': '+7(917)5710200',
    'ops': [],
    'final': True,
    'infoCadastralObjects': [],
    'cadastralObjectsIsEmpty': True,
    'notExFnsOp': False,
    'rakrEmpty': True,
    'execUser': {
        'id': 125,
        'firstName': 'Подрядчик',
        'lastName': "АО 'ЦЕНТРИНФОРМ'",
    },
    'minselhozData': [],
    'fromEpgu': True,
    'dataForRequests': {
        'mvdDataList': None,
        'minselhozDataList': None,
        'fnsDataList': None,
        'rosreestrDataList': None,
        'rosaccrDataList': [],
    },
    'transportEmpty': False,
    'transportObjects': [],
    'ogrnFilledFromEgrul': False,
    'innFilledFromEgrul': False,
    'kppFilledFromEgrul': False,
    'orgNameBriefFilledFromEgrul': False,
    'orgNameFullFilledFromEgrul': False,
    'addressFilledFromEgrul': False,
    'licenseType': {
        'code': 3,
        'description': 'производство, хранение и поставки произведенной сельскохозяйственными производителями винодельческой продукции',
        'shortName': 'ПХП_СХП',
        'region': False,
    },
    'addInfoFinishDt': None,
    'addInfoRestartFinishDt': None,
    'egrulData': False,
}

response = make_request('POST', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/233863/info', json_data=json_data)

json_data = {
    'checkId': 249507,
    'status': 2002,
}

response = make_request('PATCH', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/check/', json_data=json_data)

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/233863/extended')

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/233863/info')

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request_new_information/233863/lic_info')

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/classif/request_status/false')

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/page', params={'filter': '["status.finishedStatus","=","false"]', 'sort': '-dateInsert', 'page': 0, 'size': 20})

response = make_request('GET', 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/stats', params={'filter': '["status.finishedStatus","=","false"]'})
