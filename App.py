import requests
import json
import pandas as pd
from TrainingType import TrainingType



# def make_json_file(json_data):
#     data = json.dumps(json_data)
#     with open("sample.json", "w") as outfile:
#         outfile.write(data)

type =  TrainingType.KCardGeneralNormal.code

print(type)


# 파라미터 만들기
def makeParameter(traingType, startDate = '20220101', endDate = '20230630', page = 1):
    crseTracseSe = TrainingType.KCardGeneralNormal.code if traingType == None else traingType.code

    return {
        'authKey': '',  # 인증키
        'returnType': 'JSON',  # 리턴타입 JSON / XML
        'outType': '1',  # 구분자 : 출력형태('1':리스트 '2':상세)
        'pageNum': page,  # 시작페이지. 기본값 1, 최대 1000 검색 시작위치를 지정할 수 있습니다. 최대 1000 까지 가능.
        'pageSize': '100',  # 페이지당 출력건수, 기본값 10, 최대 100까지 가능.
        'srchTraStDt': startDate,  # 훈련시작일 From
        'srchTraEndDt': endDate,  # 훈련시작일 To
        'sort': 'ASC',  # 정렬방법 'ASC', 'DESC'
        'sortCol': 'TRNG_BGDE',  # 정렬컬럼  모집인원 : 'TOT_FXNUM', 훈련시작일: 'TRNG_BGDE', 훈련과정명: 'TRNG_CRSN'
        'crseTracseSe': crseTracseSe  # 훈련유형
    }


def call_hrd_api(parameter):
    API_URL = 'https://www.hrd.go.kr/hrdp/api/apipo/APIPO0101T.do'
    try:
        response = requests.get(url=API_URL, params=parameter)
        data = json.loads(response.json()['returnJSON'])
        srch_list = data['srchList']
        print(srch_list)
        # make_json_file(srch_list)
    except Exception as e:
        print(e)



parameter = makeParameter(TrainingType.KCardGeneralNormal)
call_hrd_api(parameter)