from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from graphql_api.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", GraphQLView.as_view(graphiql=True)),
]
