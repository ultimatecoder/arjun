from rest_framework import routers

from team import views


router = routers.DefaultRouter()
router.register(r'members', views.MemberViewSet)
