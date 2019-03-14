// this context of Arrow function

const el = document.querySelector("div")

const myObj = {
    // register() {
    //     el.addEventListener("click", function(evt) {
    //         this.printData();
    //     }.bind(this));
    // },

    // printData(){
    //     alert("cliecked!")
    // }

    register() {
        el.addEventListener("click", (evt) => {
            this.printData(evt.target);
        });
    },

    printData(el){
        alert("cliecked!", el.innerText);
    }
}

myObj.register();