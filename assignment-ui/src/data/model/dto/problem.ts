interface ChessProblemRequestData {
    n:number
    k:number
    rq:number
    cq:number
    obstacles:number[][]
}

interface ChessProblemResponseData {
    possible_targets:number
}

interface StringProblemRequestData {
    t:string
}

interface StringProblemResponseData {
    maximum_value:number
}