from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
	# Examples:
	url(r'^$', 'genre.views.home', name='home'),


    url(r'^admin/', admin.site.urls),
] 
	
	if settings.DEBUG:
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)