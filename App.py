import requests
import json

# def make_json_file(json_data):
#     data = json.dumps(json_data)
#     with open("sample.json", "w") as outfile:
#         outfile.write(data)


def call_hrd_api(parameter):
    API_URL = 'https://www.hrd.go.kr/hrdp/api/apipo/APIPO0101T.do'
    try:
        response = requests.get(url=API_URL, params=parameter)
        # tree = etree.parse(response.content)
        # print(tree)
        data = response.json()
        dict = json.loads(data['returnJSON'])
        srch_list = dict['srchList']
        # make_json_file(srch_list)

        # count = 0
        # for i in srch_list:
        #     print(i)
        #     count +=1
        # print(count)
    except Exception as e:
        print(e)




parameters = {
    'returnType': 'JSON',
    'pageSize': '100',
    'srchTraArea1': '00',
    'authKey': '',
    'sort': 'ASC',
    'outType': '1',
    'srchTraStDt': '20220101',
    'pageNum': '1',
    'sortCol': 'TRNG_BGDE',
    'srchTraEndDt': '20230630',
    'srchTraPattern': 'N1',
    'srchPart': '-99',
    'apiRequstPageUrlAdres': '/jsp/HRDP/HRDPO00/HRDPOA60/HRDPOA60_1.jsp',
    'apiRequstIp': '125.129.231.37'
}

call_hrd_api(parameters)