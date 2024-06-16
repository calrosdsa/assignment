# coding: utf-8

from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.problem.routers import (
    ProblemRouter)
from src.infrastructure.api.views.problem import (
    ProblemViewSet)

chess_problem_router = ProblemRouter()
chess_problem_router.register('', viewset=ProblemViewSet, basename='problem')

urlpatterns = [
    path('', include(chess_problem_router.urls))
]