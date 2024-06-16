from src.usecases.problem import ProblemInteractor
from typing import Tuple
from http import HTTPStatus
from src.interface.serializers.problem import ChessProblemResponse,ChessProblemRequest,StringProblemRequest,StringProblemResponse
import logging
from marshmallow import ValidationError

logger = logging.getLogger(__name__)
class ProblemController:
    def __init__(self,chess_problem_interactor:ProblemInteractor):
        self.chess_problem_interactor = chess_problem_interactor
    
    def solve_chess_problem(self,requestData:dict)-> Tuple[dict,int]:   
        try:
            data = ChessProblemRequest().load(requestData)
            possible_targets = self.chess_problem_interactor.solve_chess_problem(**data)
            res = dict(possible_targets=possible_targets)
            return ChessProblemResponse().dump(res),HTTPStatus.OK
        except ValidationError as err:
            return {'error': err.messages}, HTTPStatus.UNPROCESSABLE_ENTITY.value
    
    def solve_string_problem(self,requestData:dict)->Tuple[dict,int]:
        try:
            data = StringProblemRequest().load(requestData)
            maximum_value = self.chess_problem_interactor.solve_string_problem(**data)
            res = dict(maximum_value=maximum_value)

            return StringProblemResponse().dump(res),HTTPStatus.OK
        except ValidationError as err:
            return {'error': err.messages}, HTTPStatus.UNPROCESSABLE_ENTITY.value
        