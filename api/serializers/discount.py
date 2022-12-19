from discount.models import DiscountTabe
from rest_framework.serializers import ModelSerializer


class DiscountSerilizer(ModelSerializer):
    class Meta:
        model = DiscountTabe
        fields = "__all__"
