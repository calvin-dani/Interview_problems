function matrixTraversal(costs, travelCost) {
  let row = 0;
  let col = 0;

  travelCost += Number(costs[row][col]);
  let rightArr;
  let downArr;

  if (costs.length == 1 && costs[row].length == 1) {
    return travelCost;
  } else if (costs.length == 1 && costs[row].length > 1) {
    rightArr = traverseMatrix(costs, row, col + 1);
    return matrixTraversal(rightArr, travelCost);
  } else if (costs.length > 1 && costs[row].length == 1) {
    downArr = traverseMatrix(costs, row + 1, col);
    return matrixTraversal(downArr, travelCost);
  } else {
    rightArr = traverseMatrix(costs, row, col + 1);
    downArr = traverseMatrix(costs, row + 1, col);
    return Math.min(
      matrixTraversal(rightArr, travelCost),
      matrixTraversal(downArr, travelCost)
    );
  }
}

function traverseMatrix(paramArr, row, col) {
  let newArr = [];
  for (let rowIdx = row; rowIdx < paramArr.length; rowIdx++) {
    newArr.push(paramArr[rowIdx].slice(col));
  }
  return newArr;
}

let costs = [
  [1, 6, 2],
  [4, 2, 9],
  [8, 14, 6],
  [9, 0, 1],
];

console.log(matrixTraversal(costs, 0));
