// 1) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A",
// თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)
// 2) მომხმარებელს შემოატანინეთ საკუთარი ასაკი, თუ იქნება 13 წელზე ნაკლების გამოუტანეთ You are kid, თუ იქნება 18 წელზე ნაკლების მაგრამ 13'ზე
//  მეტის გამოუტანეთ You are not adult yet და თუ იქნება 18 წელზე მეტის გამოუტანეთ You are adult
// 3) დაწერეთ მეორე დავალება პითონის კოდითაც და შემდეგ შეადარეთ js'ით დაწერილ კოდს, ამოწერეთ სინტაქსური განსხვავებები


let number = prompt("Enter your number: ");
if (number >= 90) {
    alert("Grade A");
}
else if (number >= 80) {
    alert("Grade B");
}
else if (number >= 70) {
    alert("Grade C");
}
else if (number >= 60) {
    alert("Grade D");
}
else {
    alert("Grade F");
}       

//py

// age = int(input("Enter your age: "))
// if age < 13:
//     print("You are a kid")
// elif age < 18:
//     print("You are a teenager")
// else:
//     print("You are a gorwn ass man")

//java

let age = prompt("Enter your age: ");
if (age < 13) {
    alert("You are a kid");
}
else if (age < 18) {
    alert("You are a teenager");
}
else {
    alert("You are a gorwn ass man");
}


// ამოწერეთ სინტაქსური განსხვავებები
// ჩემი აზრით py უფრო მარტივია და უფრო მარტივი წერის სტილი აქვს და js მასაც რაღაც დონეზე მსგავსია მარა სასწაულად რთულია "ჩემთვის და ისედაც არ მომწონს html, css, js," სხვა არაფერი 


// 4) შექმენით while loop'ი რომელიც გამოიტანს რიცხვებს 0'დან 100'ის ჩათვლით

let i = 0;
while (i <= 100) {
    console.log(i);
    i++;
}


// 5) შექმენით for loop'ი რომელიც გამოიტანს რიცხვებს 5'დან 10'ის ჩათვლით

for (let i = 5; i <= 10; i++) {
    console.log("i");
}
