from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from discount.models import DiscountTabe
from api.serializers.discount import DiscountSerilizer
from rest_framework import status


class DiscountApiView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = DiscountTabe.objects.all()

    def get(self, request):
        discount = self.queryset
        serilizer = DiscountSerilizer(discount, many=True)

        return Response(serilizer.data, status=status.HTTP_200_OKs)
    
DiscountApiView=DiscountApiView.as_view()
