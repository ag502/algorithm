function solution(n) {
  const primeList = new Array(n);
  for (let i = 0; i <= n; i++) {
    primeList[i] = i;
  }

  for (let i = 2; i <= parseInt(n ** 0.5); i++) {
    for (let j = i ** 2; j <= n; j += i) {
      if (primeList[j] != 0) {
        primeList[j] = 0;
      }
    }
  }
  primeList[1] = 0;

  const answer = primeList.filter((number) => number !== 0).length;
  return answer;
}
