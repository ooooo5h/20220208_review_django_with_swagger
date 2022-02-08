from rest_framework.views import APIView
from rest_framework.response import Response

from my_sns.models import User
from my_sns.serializer import UserSerializer

class User(APIView):
    
    def get(self, request):
        
        from_db_user = User.objects.filter(name=request.GET['name']).first()
        
        if from_db_user :
            
            serializer = UserSerializer(from_db_user)
            
            return Response({
                'code' : 200,
                'message' : 'GET 성공',
                'user' : serializer.data
            })
        
        else :
            return Response({
                'code' : 400,
                'message' : '입력한 이름은 존재하지 않습니다.',
            }, status=400)