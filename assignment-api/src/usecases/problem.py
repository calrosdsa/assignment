from src.domain.chess_problem import ChessProblemEntity
from src.domain.string_problem import StringProblemEntity

class ProblemInteractor:
    def __init__(self,problem_repo:object):
        self.problem_repo = problem_repo

    def solve_chess_problem(self,**kwargs) -> int:
        chess_problem:ChessProblemEntity =  self.problem_repo.get_chess_problem(**kwargs)
        possible_targets = chess_problem.queensAttack()
        return possible_targets
    
    def solve_string_problem(self,**kwargs)-> int:
        string_problem:StringProblemEntity = self.problem_repo.get_string_problem(**kwargs)
        maximum_value = string_problem.maxValue()
        return maximum_value
        