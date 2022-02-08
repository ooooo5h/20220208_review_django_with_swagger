from rest_framework.views import APIView
from rest_framework.response import Response

from my_sns.models import Lectures
from my_sns.serializer import LectureSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class Lecture(APIView):
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'title',
                openapi.IN_QUERY,
                description='조회할 강의의 이름',
                required=True,
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request):
        
        from_db_lecture = Lectures.objects.filter(title=request.GET['title']).first()
        
        if from_db_lecture:
            
            serializer = LectureSerializer(from_db_lecture)
        
            return Response({
                'code' : 200,
                'message' : 'Lecture - GET 성공',
                'lecture' : serializer.data,
            })
        else :
            return Response({
                'code' : 400,
                'message' : '존재하지않는 강의명입니다.'
            }, status=400)