from src.domain.chess_problem import ChessProblemEntity
from src.domain.string_problem import StringProblemEntity

class ProblemRepository:
    def __init__(self):
        pass

    def get_chess_problem(self,**kwargs)->ChessProblemEntity:
        chess_problem = ChessProblemEntity(**kwargs)
        return chess_problem

    def get_string_problem(self,**kwargs)-> StringProblemEntity:
        string_problem = StringProblemEntity(s=kwargs.get("t"))
        return string_problem