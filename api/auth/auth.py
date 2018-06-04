from rest_framework.authentication import BaseAuthentication
from api.models import *
from rest_framework.exceptions import AuthenticationFailed
class CnwAuth(BaseAuthentication):
    def authenticate(self, request):
        token=request.query_params.get('token')
        obj=UserToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({'code':1001,'error':'认证失败'})
        return (obj.username.username,obj)