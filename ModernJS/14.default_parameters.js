// default parameters

function sum(value, size) { // function sum(value, size=1) {
    size = size || 1;
    return value * size;
}

console.log(sum(3, 10))
console.log(sum(3)) // 기본 2번째 인자값으로 위에서 || 1 을 parameter로 넣음
console.log()

function sum2(value, size = {value:1}) { // function sum(value, size=1) {
    return value * size.value;
}

console.log(sum2(3, {value:10}))
console.log(sum2(3)) // default param이 들어감