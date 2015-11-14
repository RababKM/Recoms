from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'main.views.home'),
    url(r'^category/(?P<pk>\d+)/$', 'main.views.category_detail'),
    url(r'^recommendation/(?P<pk>\d+)/$', 'main.views.recommendation_detail'),
    url(r'^categories/$', 'main.views.category_list'),
    url(r'^cat_recommendations/(?P<pk>\d+)/$', 'main.views.cat_recommendations'),
    url(r'^location/(?P<pk>\d+)/$', 'main.views.location'),
    url(r'^search/(?P<search>\w+)/$', 'main.views.search'),
    url(r'^submit/$', 'main.views.submit_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
