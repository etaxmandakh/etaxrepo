from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

# from PYTHON-GETTING-STARTED123.etax import views
import etax.views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', etax.views.UserViewSet)
router.register(r'groups', etax.views.GroupViewSet)

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [

    path('register', etax.views.RegisterView.as_view()),
    path('login', etax.views.LoginView.as_view()),
    # path('user', etax.views.UserView.as_view()),
    # path('logout', etax.views.LogoutView.as_view()),


    path('init', etax.views.init),
    path('snip', etax.views.snippet_list),
    path('det/<pk>', etax.views.snippet_detail),
    path('userssnip/', etax.views.UserList.as_view()),
    path('userssnip/<int:pk>/', etax.views.UserDetail.as_view()),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("test", etax.views.test, name="index"),
    path("", etax.views.index, name="index"),
    path("db/", etax.views.db, name="db"),
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
