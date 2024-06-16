# coding: utf-8

from src.domain.core.routing import Route, Router
from src.interface.routes.constants import (
    CHESS_PROBLEM_PREFIX,STRING_PROBLEM_PREFIX)
from src.interface.controllers.problem import ProblemController
from src.domain.core.constants import HTTP_VERB_POST,HTTP_VERB_GET


problem_router = Router()
problem_router.register([
   Route(
        http_verb=HTTP_VERB_POST,
        path=fr'^{CHESS_PROBLEM_PREFIX}/',
        controller=ProblemController,
        method='solve_chess_problem',
        name='solve_chess_problem',
    ),
    Route(
        http_verb=HTTP_VERB_POST,
        path=fr'^{STRING_PROBLEM_PREFIX}/',
        controller=ProblemController,
        method='solve_string_problem',
        name='solve_string_problem',
    ),
])