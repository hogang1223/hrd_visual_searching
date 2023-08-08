from enum import Enum

class TrainingType(Enum):
    KCardGeneralNormal = (0, 'C0061') # 국민내일배움카드(일반)
    KCardGeneralJobSeeker = (1, 'C0061S') # 국민내일배움카드(주 훈련대상: 구직자)
    KCardGeneralIncumbent = (2, 'C0061I') # 국민내일배움카드(주 훈련대상: 재직자)
    NationalStrategicIndustries = (3, 'C0054') # 국가기간전략산업직종
    CourseEvaluationTraining = (4, 'C0055C') # 과정평가형훈련
    EnterpriseTraining = (5, 'C0054G') # 기업맞춤형훈련
    SmartMixedTraining = (6, 'C0054Y') # 스마트혼합훈련
    GeneralHighSpecializedTraining = (7, 'C0054S') # 일반고특화훈련
    FourthIndustrialHRDTraining = (8, 'C0054I') # 4차산업혁명인력양성훈련
    KDigitalTraining = (9, 'C0104') # K - 디지털트레이닝
    KDigitalBasicTraining = (10, 'C0105') # K - 디지털기초역량훈련
    PlatformWorkerTraining = (11, 'C0103') # 플랫폼종사자훈련
    ResponseToChangesIndustrialStructure = (10, 'C0105') # 산업구조변화대응
    SeniorCareerCounsling = (12, 'C0106') # 중장년경력설계카운슬링
    JobSeekerRemoteTraining = (13, 'C0055') # 실업자 원격훈련
    IncumbentRemoteTraining = (14, 'C0031') # 근로자 원격훈련
    IncumbentForeignLanguageTraining = (15, 'C0031F') # 근로자외국어훈련


    def __init__(self, number, code):
        self.number = number
        self.code = code


