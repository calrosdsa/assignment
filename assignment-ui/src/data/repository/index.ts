import ProblemDataSourceImpl from "./problem/ProblemDataSourceImpl";
import ProblemRepository from "./problem/ProblemRepository";

const problemDataSource = new ProblemDataSourceImpl()
const problemRepository  = new ProblemRepository(problemDataSource)


export {
    problemRepository
}