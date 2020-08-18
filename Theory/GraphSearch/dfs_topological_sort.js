const adj = new Map();
adj.set("6", ["7", "8", "9"]);
adj.set("7", ["1"]);
adj.set("8", ["2"]);
adj.set("9", ["4"]);
adj.set("1", ["2"]);
adj.set("2", ["3"]);
adj.set("10", ["3"]);
adj.set("3", ["4"]);
adj.set("4", ["5"]);
adj.set("5", []);

const visited = new Map();
adj.forEach((_, vertex) => {
  visited.set(vertex, false);
});

const records = [];

const dfs = (here) => {
  // 1. 체크인
  visited.set(here, true);
  // 2. 도착
  console.log(`dfs visits ${here}`);
  // 3. 인접한 정점 순회
  adj.get(here).forEach((there) => {
    // 4. 갈 수 있는 지 검사
    if (visited.get(there) === false) {
      // 5. 간다
      dfs(there);
      //   records.push(there);
    }
  });
  records.push(here);
};

const dfsAll = () => {
  for (let vertex of adj.keys()) {
    if (visited.get(vertex) === false) {
      dfs(vertex);
    }
  }
};

dfsAll();
console.log(records);

const adj2 = new Map([
  [1, [2, 3, 4]],
  [2, [5]],
  [3, [4]],
  [4, [2, 5]],
  [5, []],
]);

const inDegree = [-1, 0, 2, 1, 2, 2];
const queue = [];

const topologicalSort = () => {
  inDegree.forEach((degree, idx) => {
    if (degree === 0) {
      queue.push(idx);
    }
  });

  // console.log(queue);

  while (queue.length !== 0) {
    let here = queue.shift();
    console.log(here);
    adj2.get(here).forEach((there) => {
      inDegree[there]--;
      if (inDegree[there] === 0) {
        queue.push(there);
      }
    });
  }
};

topologicalSort();
