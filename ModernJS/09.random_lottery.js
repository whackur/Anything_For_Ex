const SETTING = {
  name: "LUCKY LOTTO",
  count: 6,
  maxNumber: 45
};

let { count, maxNumber } = SETTING;
console.log(getLottoNumberSet(count, maxNumber));

function getRandomNumber(maxNumber) {
  return Math.floor(Math.random() * maxNumber + 1)
}

function getLottoNumberSet(count, maxNumber) {
  const numberSet = new Set();

  while (numberSet.size !== count) {
    numberSet.add(getRandomNumber(maxNumber))
  }

  return numberSet;
}