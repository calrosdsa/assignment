interface ProblemDataSource {
  SolveChessProblem: (d: ChessProblemRequestData) => Promise<Response>;
  SolveStringProblem: (d: StringProblemRequestData) => Promise<Response>;
}
