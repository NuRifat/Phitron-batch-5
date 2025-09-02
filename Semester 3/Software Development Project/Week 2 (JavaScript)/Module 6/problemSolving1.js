//Create odd even array
const oddEven = (array) => {
    let evenNumbers = [];
    let oddNumbers = [];
    for (let i = 0; i < array.length; i++) {
        const element = array[i];
        if (element % 2 == 0) {
            evenNumbers.push(element);
        } else {
            oddNumbers.push(element);
        }
    }
    return evenNumbers;
}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
const result = oddEven(numbers);
console.log(result);
