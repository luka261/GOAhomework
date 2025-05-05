// შექმენით .forEach მეთდის კლონი

function myForEach(array, callback) {
    for (let i = 0; i < array.length; i++) {
        callback(array[i], i, array);
    }
}

myForEach(names, (curValue, index) => {
    if(index % 2 === 0) {
        console.log(`${curValue} is on even index`);
    } else {
        console.log(`${curValue} is on odd index`);
    }
});

// არ გამოიყენოთ .forEach

for (let i = 0; i < names.length; i++) {
    if(i % 2 === 0) {
        console.log(`${names[i]} is on even index`);
    } else {
        console.log(`${names[i]} is on odd index`);
    }
}

