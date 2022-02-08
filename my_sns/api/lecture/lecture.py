from rest_framework.views import APIView
from rest_framework.response import Response

from my_sns.models import Lectures
from my_sns.serializer import LectureSerializer

class Lecture(APIView):
    
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