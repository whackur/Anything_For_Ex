// ES6 Class
function Health(name){
    this.name = name;
}

Health.prototype.showHealth = function (){
    console.log(this.name+"님 안녕하세요");
}

const h = new Health("Jay");
h.showHealth();