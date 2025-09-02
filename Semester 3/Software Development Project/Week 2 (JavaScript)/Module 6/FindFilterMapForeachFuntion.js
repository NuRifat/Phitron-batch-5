const products = [
    {id:1,name:"Iphone",Color:"Blue",Price:15000},
    {id:2,name:"Samsung",Color:"Black",Price:9000},
    {id:3,name:"Oppo",Color:"Black",Price:6000},
    {id:4,name:"Samsung",Color:"Red",Price:6000},
    {id:5,name:"Iphone",Color:"Black",Price:8000},
    {id:6,name:"Iphone",Color:"Blue",Price:5000},
];

//finding id-3 using for-loop
for(let i=0;i<products.length;i++){
    const element = products[i];
    if(element.id == 3){
        console.log(element);
    }
}

//finding id-3 using find()
const result = products.find(pd=>pd.id==3);
console.log(result);

//filtering all iphone using filter()
const result2 = products.filter(pd=>pd.name=="Iphone");
console.log(result2);

//using map()
const sum = products.map(pd => pd.id*2);
console.log(sum);

//using forEach()
products.forEach(product => {
    console.log(product.id, product.name);
})