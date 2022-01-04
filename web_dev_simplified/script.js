// const body = document.body;
// //

// const div = document.createElement("div");
// // div.innerText = "Hello World";
// // div.innerHTML = "<strong>Hello World</strong>";

// //another way to add innerHTML
// strong = document.createElement("strong");
// strong.innerText = "Hello Strong";
// div.append(strong);

// body.append(div);
// // body.appendChild(div);

const body = document.body;
const div = document.querySelector("div");
const spanHi = document.querySelector("#hi");

const spanBye = document.querySelector("#bye");

spanBye.remove();
div.append(spanBye);

//aso we have removeChild() like this:
div.removeChild(spanBye);

console.log(spanHi.getAttribute("id"));
//just like below:
console.log(spanHi.id);
//how to modify attributes
spanHi.setAttribute("id", "another");
//or like below
spanHi.id = "yetAnother";
//so works the removeAttribute
spanHi.removeAttribute("id");

//we can also manipulate data attributes which I dont know anything about ha!
console.log(spanHi.dataset);
console.log(spanHi.dataset.test);
spanHi.dataset.newName = "New Name";

//accessing classes

spanHi.classList.remove("hi1");
spanHi.classList.add("hi3");

//also we have toggle, and can be used with boolean
spanHi.classList.toggle("hi4");

// modifying the css or style of any element
spanHi.style.color = "yellow";
//camel case
spanHi.style.backgroundColor = "red";
