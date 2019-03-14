// Object assign 메서드
// new 대신에 object를 만드는 방법

const healthObj = {
    showHealth : function() {
        console.log("오늘 운동시간 : " + this.healthTime);
    }
}

// const myHealth = Object.create(healthObj); // 새로운 표준같은 방법
// myHealth.healthTime = "11:20";
// myHealth.name = "Jay";

const myHealth = Object.assign(Object.create(healthObj), {
    name : "jay",
    lastTime : "11:20"
});

console.log(myHealth); // myHealth object를 웹 디버거에서 확인하기