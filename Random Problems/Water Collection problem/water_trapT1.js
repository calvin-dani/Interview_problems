function waterTrap(paramArr) {
  let maxH = Math.max(...paramArr);
  let waterQ = 0;
  for (let waterLevel = 1; waterLevel <= maxH; waterLevel++) {
    let temp = waterTrapFilter(waterLevel, paramArr);
    waterQ += temp;
  }
  console.log(waterQ);
  return waterQ;
}

function waterTrapFilter(waterLevel, paramArr) {
  let boolArr = paramArr.map((curr) => (curr >= waterLevel ? false : true));
  let leftIdx = boolArr.findIndex((value) => value == false);
  boolArr.reverse();
  let rightIdx = boolArr.findIndex((value) => value == false);
  rightIdx = boolArr.length - rightIdx;
  boolArr.reverse();
  let filteredBoolArr = boolArr.slice(leftIdx, rightIdx);
  let waterCollected = filteredBoolArr.reduce((acc, curr) => {
    if (curr) {
      acc++;
    }
    return acc;
  }, 0);

  return waterCollected;
}

waterTrap([1, 3, 2, 0, 5, 1, 1, 3, 4]);
