function getGrade(marks) {
    if (marks >= 90 && marks <= 100) {
        return "A+";
    } else if (marks >= 80) {
        return "A";
    } else if (marks >= 70) {
        return "B";
    } else if (marks >= 60) {
        return "C";
    } else if (marks >= 50) {
        return "D";
    } else if (marks >= 0) {
        return "F";
    } else {
        return "Invalid marks";
    }
}

console.log(getGrade(95)); 
console.log(getGrade(82)); 
console.log(getGrade(67)); 
console.log(getGrade(45)); 
