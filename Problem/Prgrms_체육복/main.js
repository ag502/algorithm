function solution(n, lost, reserve) {
  const studentList = new Map();

  for (let i = 1; i <= n; i++) {
    studentList.set(i, 1);
  }

  lost.forEach((stdNum) =>
    studentList.set(stdNum, studentList.get(stdNum) - 1)
  );

  reserve.forEach((stdNum) =>
    studentList.set(stdNum, studentList.get(stdNum) + 1)
  );

  studentList.forEach((clothNum, stdNum) => {
    if (clothNum === 0 && studentList.get(stdNum - 1) === 2) {
      studentList.set(stdNum - 1, 1);
      studentList.set(stdNum, 1);
    } else if (clothNum === 0 && studentList.get(stdNum + 1) === 2) {
      studentList.set(stdNum + 1, 1);
      studentList.set(stdNum, 1);
    }
  });

  let answer = 0;
  studentList.forEach((clothNum, stdNum) => {
    if (clothNum >= 1) {
      answer += 1;
    }
  });
  return answer;
}
