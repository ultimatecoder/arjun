from django.conf.urls import url, include

from team import urls

urlpatterns = [
    url(r'^team/', include(urls.router.urls))
]
