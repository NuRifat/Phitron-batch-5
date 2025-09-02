let numbers = [];

for(let a=1;a<=50;a++){
    if(a%3==0 && a%5==0){
        numbers.push(a);
    }
}

console.log(numbers);