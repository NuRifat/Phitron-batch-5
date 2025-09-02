//distructuring object
const person = {
    name: "Rifat",
    age: 10,
    friends: ["Sabbir", "Abir", "Joshim", "Razzak"]
};
const {age,name} = person;
console.log(age,name);

//distructuring array
const names = ["Karim", 30, "CSE"];
const [a,b,c] = names;
console.log(a,b,c);