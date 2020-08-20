const adj = new Map([
  ["S", ["A", "I"]],
  ["A", ["S", "B", "C", "E", "G"]],
  ["B", ["A", "C", "D", "E"]],
  ["C", ["A", "B"]],
  ["D", ["B"]],
  ["E", ["A", "B", "F"]],
  ["F", ["E"]],
  ["G", ["A", "H", "I"]],
  ["I", ["S", "G"]],
  ["H", ["G"]],
]);

const visited = new Map();
adj.forEach((_, vertex) => visited.set(vertex, false));

const stack = [];

const dfsStack = (here) => {
  // 1. 처음 시작 노드 체크인
  stack.push(here);
  visited.set(here, true);
  console.log(here);

  while (stack.length !== 0) {
    let isAddToStack = false;
    let curVertex = stack[stack.length - 1];
    let adjVertex = adj.get(curVertex);

    // 2. 인접 노드 순회
    for (let vertex of adjVertex) {
      // 3. 갈 수 있는지 검사
      if (!visited.get(vertex)) {
        // 4. 간다
        stack.push(vertex);
        visited.set(vertex, true);
        isAddToStack = true;
        console.log(vertex);
        break;
      }
    }

    // 5. 못 갈 경우 방문이 완료 되었기 때문에 스택에서 제거
    if (!isAddToStack) {
      stack.pop();
    }
  }
};

const dfsAll = () => {
  adj.forEach((_, vertex) => {
    if (!visited.get(vertex)) {
      dfsStack(vertex);
    }
  });
};

dfsAll();
