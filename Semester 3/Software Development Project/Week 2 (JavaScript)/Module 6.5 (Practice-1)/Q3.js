let numbers = [12, 5, 19, 3, 7, 15, 1, 20, 8, 10, 14, 2, 6, 9, 18, 16, 13, 11, 17, 4];

//If just use numbers.sort(), it sorts alphabetically (so 10 would come before 2).
//That’s why we pass the compare function (a, b) => a - b to sort numerically.
numbers.sort((a,b) => a-b);

console.log(numbers);