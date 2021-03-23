from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Cheff API backend exam WORKALOVE",
      
      default_version='beta backend',
      description="Esta interface é a conexão entre você e dois dos melhores cheff's do mundo, um é especialista em FastFood, seu nome é (Cheff_ID) Sanji, o outro, é especialista em receitas demoradas, ele se chama (Cheff_ID) Zeff, você comprou esse contato direto com eles por 5 milhões de dolares, poisjuntos eles tem 18239012 michelins. Essa API fornece também a possibilidade de integração com Qualquer sistema de frontend.Caso tenha algum problema, acesse o dominio http://127.0.0.1:8000/admin/, as credenciais devem ser criadass",
      terms_of_service="https://github.com/mendesbayout",
      contact=openapi.Contact(email="mendesbayout@gmail.com"),
      license=openapi.License(name="Pesquise primeiro as IDS, cheque o curriculum de cada um, depois busque por receitas usando o nome deles, lembrando, Sanji é especialista em comida rapida pois trabalha em um barco pirata, Zeff tem seu príprio restaurante e muitos funcionários"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    #path('api', include('api.urls')),
    #path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
