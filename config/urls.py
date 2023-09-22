from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ace_produtos.views import AutorViewSet, CategoriaViewSet, MarcaViewSet, ProdutoViewSet

from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"autores", AutorViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    # token
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
<<<<<<< HEAD
    path("api/", include(usuario_router.urls)),
]
=======
]
>>>>>>> 30dca4fdb5323b36b1889beb883fc6befaa2cd81
