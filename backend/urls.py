
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', include('principal.urls.indexUrls')),
    path('principal/', include('principal.urls.aboutUrls')),
    path('principal/', include('principal.urls.contactUrls')),
    path('principal/', include('principal.urls.faqUrls')),
    path('principal/', include('principal.urls.bloghomeUrls')),
    path('principal/', include('principal.urls.blogpostUrls')),
    path('pacotes/', include('pacotes.urls.pricingUrls')),
    path('login_user/', include('login_user.urls.loginUrls')),
    path('login_user/', include('login_user.urls.registroUrls')),
    path('login_user/', include('login_user.urls.redefinirUrls')),
    path('dashboard/', include('dashboard.urls.perfilFotografoUrls')),
    path('dashboard/', include('dashboard.urls.portfolioItemUrls')),
    path('dashboard/', include('dashboard.urls.portfolioOverviewUrls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
