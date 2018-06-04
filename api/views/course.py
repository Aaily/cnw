from rest_framework import viewsets
from rest_framework.response import Response
from api.myserialisers.utils import *
from rest_framework.views import APIView


class CourseModelViews(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer

    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Course.objects.all()
            rec = CourseModelSerializer(instance=queryset, many=True)
            ret['data'] = rec.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取班级数据失败'
        return Response(ret)


class CourseDetailModelViews(viewsets.ModelViewSet):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailModelSerializer

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = CourseDetail.objects.filter(course_id=pk).first()
            rec = CourseDetailModelSerializer(instance=obj, many=False)
            ret['data'] = rec.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取班级详细信息失败'
        return Response(ret)


class DegreeCourselModelViews(viewsets.ModelViewSet):
    queryset = DegreeCourse.objects.all()
    serializer_class = DegreeCourseModelSerializer

    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = DegreeCourse.objects.all()
            rec = DegreeCourseModelSerializer(instance=queryset, many=True)
            ret['data'] = rec.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取学位数据失败'
        return Response(ret)


class TeacherModelViews(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = tacherModelSerializer

    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Teacher.objects.all()
            rec = tacherModelSerializer(instance=queryset, many=True)
            ret['data'] = rec.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取班级数据失败'
        return Response(ret)


class MicroView(viewsets.ModelViewSet):
    queryset = ArticleSource.objects.all()
    serializer_class = ArticleSourceSerializer

    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = ArticleSource.objects.all()
            rec = ArticleSourceSerializer(instance=queryset, many=True)
            ret['data'] = rec.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取文章失败'
        return Response(ret)


class NewDetailView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = Article.objects.filter(id=pk).first()
            rec = ArticleModelSerializer(instance=obj, many=False)
            ret['data'] = rec.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取文章详细信息失败'
        return Response(ret)

    def create(self, request, *args, **kwargs):
        pass