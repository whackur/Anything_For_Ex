// ES6 Class

class Health {
    constructor(name, lastTime) {
        this.name = name;
        this.lastTime = lastTime;
    }

    showHealth(){
        console.log("안녕하세요 " + this.name);
    }
}

const myHealth = new Health("Jay");
myHealth.showHealth();
console.log(myHealth);
console.log(toString.call(Health)); // Health는 실제로는 class가 아니라 function