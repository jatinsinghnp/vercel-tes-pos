from .user import urlpatterns as user_urlpatterns
from .product import urlpatterns as product_urlpatterns
from .bill import urlpatterns as bill_urlpatterns
from .organization import urlpatterns as org_urlpatterns
from .discount_urls import urlpatterns as discount_urlspatterns
urlpatterns = (
    [] + user_urlpatterns + product_urlpatterns + bill_urlpatterns + org_urlpatterns+discount_urlspatterns
)
