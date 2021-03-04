function sockMerchant(sockArr) {
  let sockObj = {};
  frequencyColor(sockObj, sockArr);
  sockFreqArr = Object.entries(sockObj);
  let pair = sockFreqArr.reduce(
    (acc, curr) => (acc += Math.floor(curr[1] / 2)),
    0
  );
  console.log(pair);
  return pair;
}

function frequencyColor(sockObj, sockArr) {
  for (let sockColor of sockArr) {
    if (!sockObj.hasOwnProperty(sockColor)) {
      sockObj[sockColor] = 1;
      continue;
    }
    sockObj[sockColor] += 1;
  }
}

sockMerchant([10, 20, 20, 10, 10, 30, 50, 10, 20]);

sockMerchant([50, 20, 30, 90, 30, 20, 50, 20, 90]);

sockMerchant([]);
