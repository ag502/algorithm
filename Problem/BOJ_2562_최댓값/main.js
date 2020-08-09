const readline = require("readline");
const stdin = require("process");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(parseInt(line));
}).on("close", () => {
  const [maxValue, index] = input.reduce(
    (prev, current, idx) => {
      if (prev[0] < current) {
        return [current, idx];
      }
      return prev;
    },
    [-1, -1]
  );
  console.log(maxValue);
  console.log(index + 1);
  process.exit();
});
