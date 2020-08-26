const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  // 1. input parsing
  const [N, M] = input[0].split(" ").map((number) => parseInt(number));
  const inputArray = input[1]
    .split(" ")
    .map((number) => parseInt(number))
    .sort((a, b) => a - b);
  //   const visited = Array(N).fill(False);

  for (let idx = 0; idx < N; idx++) {
    mPermutation(idx, N, M, 0, inputArray, []);
  }
  process.exit();
});

const mPermutation = (curIdx, n, m, selectedNum, array, answer) => {
  // 1. 체크인
  selectedNum++;
  // 2. 목적지
  answer.push(array[curIdx]);
  // 3. 인접 노드 순회
  for (let nextIdx = 0; nextIdx < n; nextIdx++) {
    // 4. 갈수 있는지 검사
    if (selectedNum != m) {
      mPermutation(nextIdx, n, m, selectedNum, array, answer);
    }
  }
  // 5. 체크아웃
  if (answer.length === m) {
    console.log(answer.join(" "));
  }
  selectedNum--;
  answer.pop();
};
