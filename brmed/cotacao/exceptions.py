from rest_framework.exceptions import APIException

class DataNotFound(APIException):
    status_code = 404
    default_detail = {
        'code': 1422, 'msg': 'Não há dados no banco de dados'}
    default_code = 6003   