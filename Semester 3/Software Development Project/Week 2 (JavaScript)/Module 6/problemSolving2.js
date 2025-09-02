// find the big name
const FindBigName = (array) => {
    let bigName = array[0];
    for (let i = 0; i < array.length; i++) {
        if (array[i].length > bigName.length) {
            bigName = array[i];
        }
    }
    return bigName;
}

const friends = ["Rahim", "Mosharof", "Safi", "Debashish", "Rifat"];
const friend = FindBigName(friends);
console.log(friend);