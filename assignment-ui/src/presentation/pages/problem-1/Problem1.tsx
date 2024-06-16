"use client";
import { LoadingButton } from "@mui/lab";
import { Button, Typography } from "@mui/material";
import Problem1ViewModel from "./Problem1ViewModel";
import { ChangeEvent, FormEvent, useState } from "react";

const Problem1 = () => {
  const vm = Problem1ViewModel();
  const state = vm.state;
  const [inputData, setInputData] = useState(``);

  const onSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    vm.solveChessProblem(inputData);
  };

  return (
    <div className="p-4 max-w-lg mx-auto grid gap-y-4">
      <Typography variant="h4">Problem 1: Chess</Typography>
      <Typography variant="body1">
        You have a square chess board with one queen and a number of obstacles
        placed on it. Determine how many squares the queen can attack.
      </Typography>
      <div className="mb-4">
        <form onSubmit={onSubmit} className="mb-4 w-full grid gap-y-4">
          <div>
            <label className="block text-lg font-medium mb-2">Input data</label>
            <textarea
              value={inputData}
              onChange={(e) => setInputData(e.target.value)}
              name="chess_problem"
              id="input-1"
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
        <pre id="output-1" className="p-4 bg-gray-100 text-lg rounded-lg h-12 flex justify-center items-center">
          {state.data != null && state.data.possible_targets}
        </pre>
      </div>
    </div>
  );
};

export default Problem1;
