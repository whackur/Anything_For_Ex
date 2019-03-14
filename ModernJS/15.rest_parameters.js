// function checkNum() {
//     const argArray = Array.prototype.slice.call(arguments) // 배열로 변경해야함 옛날방식
//     console.log(toString.call(argArray));
//     const result = argArray.every((v) => typeof v === "number") // ES6
//     console.log(result);
// }

function checkNum(...argArray) { // argument 개수에 상관없도록 변경
    // const argArray = Array.prototype.slice.call(arguments) // 배열로 변경해야함 옛날방식
    // console.log(toString.call(argArray));
    const result = argArray.every((v) => typeof v === "number") // ES6
    console.log(result);
}


const result = checkNum(10,2,3,4,5,"123")
const result2 = checkNum(10,2,"123")
const result3 = checkNum(10,2,100)