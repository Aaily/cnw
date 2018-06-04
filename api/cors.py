from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # 允许你的域名来获取我数据
        response['Access-Control-Allow-Origin'] = '*'
        if request.method=='OPTIONS':
        # 允许你携带Content-Type请求头
            response['Access-Control-Allow-Headers'] = 'Content-Type'
        # 允许你发送DELETE,PUT
            response['Access-Control-Allow-Methods'] = 'DELETE,PUT'
            # print(request.data)
        return response
