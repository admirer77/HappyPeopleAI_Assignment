// 1. Single-line comment
/*
2. Multiline comment
This program demonstrates various JavaScript concepts.
*/

// 2. Array sorting (descending order)
const fruits = ["apple", "banana", "orange", "grape", "kiwi"];
const sortButton = document.getElementById("sortButton");

sortButton.addEventListener("click", function() {
    fruits.sort(); // Sorts in ascending order
    fruits.reverse(); // Reverses to descending order
    document.getElementById("output").innerHTML += "<p>Sorted Fruits (Descending): " + fruits.join(", ") + "</p>";
});

// 3. FOR...IN loop
const person = {
    firstname: "John",
    lastname: "Doe",
    age: 30
};

let text = "";
for (let x in person) {
    text += x + ": " + person[x] + "<br>";
}
document.getElementById("output").innerHTML += "<p>FOR...IN Loop: <br>" + text + "</p>";

// 4. Accessing object properties
document.getElementById("output").innerHTML += "<p>Firstname: " + person.firstname + "</p>"; // Using dot notation
document.getElementById("output").innerHTML += "<p>Lastname: " + person["lastname"] + "</p>"; // Using bracket notation

// 5. Variable hoisting
myVar = 5; // Initialization first
document.getElementById("output").innerHTML += "<p>Hoisted Variable: " + myVar + "</p>";
var myVar; // Declaration (hoisted to the top, but initialized later)

// 6. Strict mode
"use strict";
try {
    nonDeclaredVar = 10; // Causes an error in strict mode
    document.getElementById("output").innerHTML += "<p>Non-Declared Variable: " + nonDeclaredVar + "</p>"; // This line will not be reached
} catch (error) {
    document.getElementById("output").innerHTML += "<p>Error: " + error + "</p>"; //This gets printed
}
//The error message will be:  "Uncaught ReferenceError: nonDeclaredVar is not defined"