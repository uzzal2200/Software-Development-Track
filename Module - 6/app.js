
console.log("he");
console.log(document.getElementById("title").style.color="red");
console.log(document.getElementsByClassName("uzzal"));
// to get attibute

var img = document.getElementById("img");
//console.log(img.getAttribute("src"));

// to set attribute
img.setAttribute("alt"," profile picture");

//console.log(img.getAttribute("alt"));
img.classList.add("testclass");
console.log(img);

var hero=document.getElementById("hero");
console.log(hero.innerText);

var input=document.getElementById("input").value;
console.log(typeof value);
var parent = document.getElementById("parent").innerHTML;
console.log(parent);

// var testdiv = document.getElementsByClassName("test");
// console.log(testdiv[0].childNodes[1].parentNode.parentNode.parentNode.childNodes[5]);
var appended = document.getElementById("appended");
// var p=document.createElement("p");
// p.innerText = "I am so alone ";
// appended.appendChild(p);

// function
function createEl()
{
    var p = document.createElement("p");
    p.innerText = "I am alone ";
    appended.appendChild(p);
}

createEl();
// add event listener
// document.getElementById("submit-btn").addEventListener("click",function(e){
//     //console.log("yes boss");
//     // createEl();

//     var inputValue = document.getElementById("input").value;
//     console.log(inputValue);
// });

// // on change event
// document.getElementById("input").addEventListener("blur",function(e){
//     console.log(e.target.value);
// });

function inputChange(e){
    console.log("hello");
}

function clickHandler(e){
  
    var inputValue = document.getElementById("input").value;
    console.log(inputValue);
};