function waterTrap(paramArr) {
  let leftIdx = 0;
  let rightIdx = paramArr.length - 1;
  let waterCollected = 0;
  let maxH = 0;
  while (leftIdx < rightIdx) {
    if (paramArr[leftIdx] <= paramArr[rightIdx]) {
      maxH = Math.max(paramArr[leftIdx], maxH);
      waterCollected += maxH - paramArr[leftIdx];
      leftIdx++;
    } else {
      maxH = Math.max(paramArr[rightIdx], maxH);
      waterCollected += maxH - paramArr[rightIdx];
      rightIdx--;
    }
  }
  console.log(waterCollected);
  return waterCollected;
}

waterTrap([1, 3, 2, 0, 5, 1, 1, 3, 4]);
