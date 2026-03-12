let expenses = JSON.parse(localStorage.getItem("expenses")) || [];
let budget = localStorage.getItem("budget") || null;


function save(){
localStorage.setItem("expenses", JSON.stringify(expenses));
}


function saveBudget(){
localStorage.setItem("budget", budget);
}


function updateTotal(){

let total = 0;

expenses.forEach(e=>{
total += e.amount;
});

document.getElementById("totalAmount").innerText = "₱" + total;

checkBudget(total);

}


function render(){

let list = document.getElementById("expenseList");
list.innerHTML = "";

expenses.forEach((e,i)=>{

let li = document.createElement("li");

li.innerHTML =
`₱${e.amount} | ${e.date} | ${e.category} | ${e.note}
<button onclick="editExpense(${i})">Edit</button>
<button onclick="deleteExpense(${i})">Delete</button>`;

list.appendChild(li);

});

updateTotal();

}


function addExpense(){

let amount = document.getElementById("amount").value;
let date = document.getElementById("date").value;
let category = document.getElementById("category").value;
let note = document.getElementById("note").value;

if(!amount || !date){
alert("Please enter amount and date");
return;
}

let today = new Date().toISOString().split("T")[0];

if(date > today){
alert("Date cannot be in the future");
return;
}

expenses.push({
amount: parseFloat(amount),
date: date,
category: category,
note: note
});

save();
render();

document.getElementById("amount").value = "";
document.getElementById("note").value = "";

}


function editExpense(index){

let e = expenses[index];

let newAmount = prompt("Edit Amount:", e.amount);
let newDate = prompt("Edit Date (YYYY-MM-DD):", e.date);
let newCategory = prompt("Edit Category:", e.category);
let newNote = prompt("Edit Notes:", e.note);

if(!newAmount || !newDate){
alert("Amount and date are required");
return;
}

let today = new Date().toISOString().split("T")[0];

if(newDate > today){
alert("Date cannot be in the future");
return;
}

expenses[index] = {
amount: parseFloat(newAmount),
date: newDate,
category: newCategory,
note: newNote
};

save();
render();

}


function deleteExpense(index){

expenses.splice(index,1);

save();
render();

}


function monthlyReport(){

let month = prompt("Enter month (YYYY-MM)");

let total = 0;

expenses.forEach(e=>{
if(e.date.startsWith(month)){
total += e.amount;
}
});

document.getElementById("report").innerText =
"Total spending for " + month + ": ₱" + total;

}


function categorySummary(){

let summary = {};

expenses.forEach(e=>{
summary[e.category] = (summary[e.category] || 0) + e.amount;
});

let text = "";

for(let cat in summary){
text += cat + " : ₱" + summary[cat] + "\n";
}

document.getElementById("report").innerText = text;

}


function exportCSV(){

let csv = "Amount,Date,Category,Notes\n";

expenses.forEach(e=>{
csv += `${e.amount},${e.date},${e.category},${e.note}\n`;
});

let blob = new Blob([csv],{type:"text/csv"});

let a = document.createElement("a");
a.href = URL.createObjectURL(blob);
a.download = "expenses.csv";
a.click();

}


function setBudget(){

let value = prompt("Enter your monthly budget:");

if(!value){
return;
}

budget = parseFloat(value);

saveBudget();

alert("Budget set to ₱" + budget);

checkBudget();

}


function checkBudget(currentTotal){

if(!budget){
return;
}

let total = currentTotal || expenses.reduce((sum,e)=>sum+e.amount,0);

if(total > budget){
alert("WARNING: You have exceeded your budget!");
}

}


render();
