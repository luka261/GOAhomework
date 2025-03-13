// New keywordის გამოყენებით 
// შექმენით ლისთი რომელშიც შეინახავთ 5 სხვადასხვა ელემენტს, შემდეგ ინდექსინგის გამოყენებით გამოიტანეთ კონსოლში ყველა ეს ელემენტი
// შექმენით ლისთი New Keywordოს გამოყენებით რომელსაც არგუმენტად მისცემთ 4ს, კომენტარების დახმარებით ახსენით რას ნიშნავს ეს 4
// შექმენით ლისთი New keywordის გამოყენების გარეშე და შეინახეთ 3 ელემენტი

const list = ['apple', 'banana', 'kiwi', 'orange', 'grape'];
console.log(list[0]);
console.log(list[1]);
console.log(list[2]);
console.log(list[3]);
console.log(list[4]);

const list2 = new Array('apple', 'banana', 'kiwi', 'orange');

const list3 = new Array('apple', 'banana', 'kiwi');
console.log(list2);
console.log(list3);


// დაამსგავსეთ ის Associative Arrayს, შემდეგ კი ახსენით, რატომ აჩვენებს Array ზომა 0ს

const arr = [];
arr['name'] = 'Giorgi';
arr['lastname'] = 'Kalandadze';
arr['age'] = 25;
console.log(arr);
console.log(arr.length); 


// შექმენით ცარიელი Array, რომელსაც დაამატებთ თქვენს სახელს, გვარს და ასაკს.

const arr2 = [];
arr2.push('Giorgi');
arr2.push('Kalandadze');
arr2.push(25);
console.log(arr2);
console.log(arr2.length); 



