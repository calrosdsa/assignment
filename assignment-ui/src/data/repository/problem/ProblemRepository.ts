class ProblemRepository {
  dataSource: ProblemDataSource;
  constructor(datasource: ProblemDataSource) {
    this.dataSource = datasource;
  }
  SolveChessProblem = async (
    d: ChessProblemRequestData
  ): Promise<ChessProblemResponseData> => {
    const res = await this.dataSource.SolveChessProblem(d);
    if (!res.ok) {
      const data = await res.json();
      window.alert(JSON.stringify(data));
      throw new Error("Fail to fetch data");
    }
    return res.json();
  };
  SolveStringProblem = async (
    d: StringProblemRequestData
  ): Promise<StringProblemResponseData> => {
    const res = await this.dataSource.SolveStringProblem(d);
    if (!res.ok) {
      const data = await res.json();
      window.alert(JSON.stringify(data));
      throw new Error("Fail to fetch data");
    }
    return res.json();
  };
}

export default ProblemRepository;
