from src.interface.repositories.problem import ProblemRepository
from src.usecases.problem import ProblemInteractor

from src.interface.controllers.problem import ProblemController

class ProblemFactory:
    @staticmethod
    def get() -> ProblemRepository:
        return ProblemRepository()
    
class ProblemInteractorFactory:
    @staticmethod
    def get()->ProblemInteractor:
        problem_repo = ProblemFactory.get()
        return ProblemInteractor(problem_repo=problem_repo)
    
class ProblemViewFactory:
    @staticmethod
    def create() -> ProblemController:
        problem_interactor = ProblemInteractorFactory.get()
        return ProblemController(problem_interactor)