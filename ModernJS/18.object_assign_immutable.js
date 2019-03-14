// Object assign 메서드
// new 대신에 object를 만드는 방법

const previousObj = {
    name : "jay",
    lastTime : "11:20"
}

const myHealth = Object.assign({}, previousObj, { // 새로운 항목을 넣을때는 덧붙여 적용
    "lastTime":"11:00",
    "age" : 30
});

console.log(myHealth);
console.log(myHealth===previousObj);