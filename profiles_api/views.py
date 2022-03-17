from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView (APIView):
    """Test Api View"""
    def get (self,request,formate=None):
        """Returns a list of APIView features"""
        an_apiview =[
            'Uses HTTP methods as function (get,post,put,patch,delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response ({'message':'Hello!', 'an_apiview': an_apiview})