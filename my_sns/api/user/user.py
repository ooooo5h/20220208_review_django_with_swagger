from rest_framework.views import APIView
from rest_framework.response import Response

from my_sns.models import Users
from my_sns.serializer import UserSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class User(APIView):
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'name',
                openapi.IN_QUERY,
                description='조회할 이름',
                required=True,
                type=openapi.TYPE_STRING,
            ),
        ]
    )    
    def get(self, request):
        
        from_db_user = Users.objects.filter(name=request.GET['name']).first()
        
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