from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.problem import (
    ProblemViewFactory)
from src.interface.routes.problem import (
   problem_router)

class ProblemRouter(SimpleRouter):
    routes = [
        Route(
            url=problem_router.get_url('solve_chess_problem'),
            mapping=problem_router.map('solve_chess_problem'),
            initkwargs={'viewset_factory':ProblemViewFactory},
            name='chess_{basename}',
            detail=False
        ),
            Route(
            url=problem_router.get_url('solve_string_problem'),
            mapping=problem_router.map('solve_string_problem'),
            initkwargs={'viewset_factory':ProblemViewFactory},
            name='string_{basename}',
            detail=False
        )
    ]