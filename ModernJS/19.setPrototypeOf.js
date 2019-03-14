// setPrototypeOf

const healthObj = {
    showHealth : function() {
        console.log("오늘 운동시간 : " + this.healthTime);
    },
    setHealth : function(newTime) {
        this.setHealth.healthTime = newTime;
    }
}

const newobj = Object.setPrototypeOf({
    name : "jay",
    lastTime : "11:00"
}, healthObj);

console.log(newobj); 