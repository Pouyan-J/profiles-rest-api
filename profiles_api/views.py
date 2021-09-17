from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            "I. Voluptate deserunt voluptate tempor sit ut irure ullamco enim irure aute id eiusmod laborum.",
            "II. Velit pariatur do dolore elit enim quis minim minim incididunt quis aliqua non.",
            "III. Deserunt proident minim sint laborum esse ea."
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})