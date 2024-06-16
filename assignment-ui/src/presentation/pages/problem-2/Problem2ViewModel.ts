import { problemRepository } from "@/data/repository";
import { useState } from "react";

const Problem2ViewModel = () => {
  const repo = problemRepository;
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState<StringProblemResponseData | null>(null);

  function validateJsonString(str:string) {
    try {
        JSON.parse(str);
    } catch (e) {  
      window.alert(`
        Invalid JSON input. Please ensure your input data is in the correct JSON format.
        Expected Format Example:
        {
          "t": "aaaaaa"
        }
        `);    
    }
}

  const solveStringProblem = async (d: string) => {
    try {
      validateJsonString(d)
      setLoading(true);
      const body: StringProblemRequestData = JSON.parse(d);
      const res = await repo.SolveStringProblem(body);
      console.log(res)
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
      data
    },
    solveStringProblem: solveStringProblem,
  };
};

export default Problem2ViewModel;
