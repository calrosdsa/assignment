from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.interface.controllers.problem import ProblemController
class ProblemViewSet(ViewSet):
    viewset_factory=None

    @property
    def controller(self) -> ProblemController:
        return self.viewset_factory.create()
    
    def solve_chess_problem(self,request:Request)->Response:
        payload,status = self.controller.solve_chess_problem(request.data)
        return Response(data=payload,status=status)
    
    def solve_string_problem(self,request:Request) -> Response:
        payload,status = self.controller.solve_string_problem(request.data)
        return Response(data=payload,status=status)
    


