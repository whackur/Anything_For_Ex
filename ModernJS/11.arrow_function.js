// arrow function
setTimeout(function() {
    console.log("settimeout1")
}, 500
);

setTimeout(() => {
    console.log("settimeout arrow")
}, 500
);

let newArr = [1,2,3,4,5].map(function(value, index, object) {
    return value * 2;
});
console.log(newArr);

let newArr2 = [1,2,3,4,5].map( (v) => {
    return v * 3;
});
console.log(newArr2)

let newArr3 = [1,2,3,4,5].map( (v) => (v * 4) ); // return 생략가능
console.log(newArr3)