from api.models import *
from rest_framework import serializers


class CourseModelSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    level = serializers.CharField(source='get_level_display')

    class Meta:
        model = Course
        fields = ['id', 'name', 'status', 'course_img', 'level', 'brief']


class CourseDetailModelSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name')
    recommends = serializers.SerializerMethodField()
    price_policy = serializers.SerializerMethodField()
    course_chapter = serializers.SerializerMethodField()
    asked_question = serializers.SerializerMethodField()

    class Meta:
        model = CourseDetail
        fields = ['course', 'video_brief_link', 'why_study', 'what_to_study_brief', 'career_improvement',
                  'prerequisite', 'recommends', 'price_policy', 'course_chapter', 'asked_question']

    def get_recommends(self, obj):
        queryset = obj.recommend_courses.all()
        return [{'id': row.id, 'title': row.name} for row in queryset]

    def get_price_policy(self, obj):
        queryset = obj.course.price_policy.all()
        return [{'period': row.valid_period, 'price': row.price} for row in queryset]

    def get_course_chapter(self, obj):
        queryset = obj.course.coursechapters.all()
        return [{'chapter': row.chapter, 'summary': row.summary} for row in queryset]

    def get_asked_question(self, obj):
        queryset = obj.course.asked_question.all()
        return [{'question': row.question, 'answer': row.answer} for row in queryset]


class tacherModelSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='get_role_display')

    class Meta:
        model = Teacher
        fields = ['role', 'title', 'image', 'brief', 'name']


class DegreeCourseModelSerializer(serializers.ModelSerializer):
    asked_question = serializers.SerializerMethodField()

    class Meta:
        model = DegreeCourse
        fields = ['id','prerequisite', 'name', 'course_img', 'brief', 'asked_question']

    def get_asked_question(self, obj):
        queryset = obj.asked_question.all()
        return [{'question': row.question, 'answer': row.answer} for row in queryset]


class ArticleSourceSerializer(serializers.ModelSerializer):
    article = serializers.SerializerMethodField()

    class Meta:
        model = ArticleSource
        fields = ['id','article']

    def get_article(self, obj):
        queryset = obj.article_set.all()
        return [{'title': row.title, 'brief': row.brief, 'head_img': row.head_img, 'comment_num': row.comment_num,
                 'agree_num': row.agree_num} for row in queryset]


class ArticleModelSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source='source.name')

    class Meta:
        model = Article
        fields = ['id','title', 'source', 'content', 'comment_num', 'agree_num']
