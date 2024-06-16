import { problemRepository } from "@/data/repository";
import { useState } from "react";

const Problem1ViewModel = () => {
  const repo = problemRepository;
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState<ChessProblemResponseData | null>(null);

  function validateJsonString(str: string) {
    try {
      JSON.parse(str);
    } catch (e) {
      window.alert(`
        Invalid JSON input. Please ensure your input data is in the correct JSON format.
        Expected Format Example:
        {
            "n":5,
            "k":3,
            "rq":4,
            "cq":3,
            "obstacles":[
                [5,5],
                [4,2],
                [2,3]
            ]
        }
          `);
    }
  }

  const solveChessProblem = async (d: string) => {
    try {
      validateJsonString(d);
      setLoading(true);
      const body: ChessProblemRequestData = JSON.parse(d);
      const res = await repo.SolveChessProblem(body);
      setData(res);
      setLoading(false);
    } catch (err) {
      setLoading(false);
      console.log(err);
    }
  };
  return {
    state: {
      loading,
      data,
    },
    solveChessProblem,
  };
};

export default Problem1ViewModel;
