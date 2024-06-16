"use client";
import { LoadingButton } from "@mui/lab";
import { Button, Typography } from "@mui/material";
import ProblemViewModel from "./Problem2ViewModel";
import { ChangeEvent, FormEvent, useState } from "react";

const Problem2 = () => {
  const vm = ProblemViewModel();
  const state = vm.state;
  const [inputData, setInputData] = useState(``);

  const onSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    vm.solveStringProblem(inputData);
  };

  return (
    <div className="p-4 max-w-lg mx-auto grid gap-y-4">
      <Typography variant="h4">Problem 2: String value</Typography>
      <Typography variant="body1">
      Jane loves strings more than anything. She has a string t with her, and value of string s over function f can be calculated as given below:
      </Typography>
      <div className="mb-4">
        <form onSubmit={onSubmit} className="mb-4 w-full grid gap-y-4">
          <div>
            <label className="block text-lg font-medium mb-2">Input data</label>
            <textarea
              value={inputData}
              onChange={(e) => setInputData(e.target.value)}
              name="chess_problem"
              id="input-2"
              className="w-full p-2 border rounded-lg"
              rows={5}
            ></textarea>
          </div>
          <LoadingButton
            fullWidth
            type="submit"
            loading={state.loading}
            variant="contained"
          >
            Submit
          </LoadingButton>
        </form>
        <h6 className="text-lg font-semibold mb-2">Output</h6>
        <pre id="output-2" className="p-4 bg-gray-100 text-lg rounded-lg h-12 flex justify-center items-center">
          {state.data != null && state.data.maximum_value}
        </pre>
      </div>
    </div>
  );
};

export default Problem2;
