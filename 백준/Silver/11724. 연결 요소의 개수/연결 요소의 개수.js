let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(' ').map(Number); // 정점의 개수 N과 간선의 개수 M

// 1. dfs 함수
const dfs = (graph, node, visited) => {
  visited[node] = true; // 해당 노드 방문으로 처리
  for (let k = 0; k < graph[node].length; k++) {
    const next = graph[node][k]; // 연결된 다음 노드
    if (!visited[next]) {
      dfs(graph, next, visited);
    }
  }
};

// 2. 간선의 관계를 인접 그래프로 표현
// let graph = Array(n).fill([]); -> 이렇게 할 경우, graph[1], graph[2],... 모든 요소가 같은 주소값의 배열[]을 가리키므로 에러가 남
let graph = Array.from({ length: n + 1 }, () => []);

for (let i = 1; i < m + 1; i++) {
  const [u, v] = input[i].split(' ').map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

// 3. 최종 결과값(연결 요소 개수), 방문 확인 배열 선언
let cnt = 0;
let visited = Array.from({length: n + 1}, () => false);

// 4. 노드를 순회하면서 방문을 했으면 pass하고 방문을 안했다면 dfs 진행 후, 결과값 1 증가시키기
for (let j = 1; j <= n; j++) {
  if (!visited[j]) {
    dfs(graph, j, visited);
    cnt++;
  }
}

// 5. 결과값 출력
console.log(cnt);