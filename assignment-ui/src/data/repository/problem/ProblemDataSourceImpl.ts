class ProblemDataSourceImpl implements ProblemDataSource {
  SolveChessProblem = (d: ChessProblemRequestData): Promise<Response> => {
    const res = fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/chess-problem/`,{
        method:"post",
        body:JSON.stringify(d),
        headers:{
            "Content-Type":"application/json"
        }
    });
    return res;
  };
  SolveStringProblem = (d: StringProblemRequestData): Promise<Response> => {
    const res = fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/string-problem/`,{
        method:"post",
        body:JSON.stringify(d),
        headers:{
            "Content-Type":"application/json"
        }
    });
    return res;
  };
}

export default ProblemDataSourceImpl;