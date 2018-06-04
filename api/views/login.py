from api.models import *
from rest_framework.views import APIView
import uuid
from rest_framework.response import Response

class Authview(APIView):
    def post(self,request,*args,**kwargs):
        ret={'code':1000}
        user=request.data.get('user')
        pwd=request.data.get('pwd')
        user_obj=UserInfo.objects.filter(username=user,password=pwd).first()
        print(user)
        if not user_obj:
            ret['code']=1001
            ret['error']='用户名或密码错误'
        else:
            token=str(uuid.uuid4())
            UserToken.objects.update_or_create(username=user_obj,defaults={'token':token})
            ret['token']=token

        return Response(ret)