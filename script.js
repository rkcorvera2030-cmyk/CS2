let expenses = JSON.parse(localStorage.getItem("expenses")) || [];


function save(){
localStorage.setItem("expenses", JSON.stringify(expenses));
}


function render(){

let list = document.getElementById("expenseList");
list.innerHTML="";

expenses.forEach((e,i)=>{

let li=document.createElement("li");

li.innerHTML=
`₱${e.amount} | ${e.date} | ${e.category} | ${e.note}
<button onclick="deleteExpense(${i})">Delete</button>`;

list.appendChild(li);

});

}


function addExpense(){

let amount=document.getElementById("amount").value;
let date=document.getElementById("date").value;
let category=document.getElementById("category").value;
let note=document.getElementById("note").value;

if(!amount || !date){
alert("Please enter amount and date.");
return;
}

expenses.push({
amount:parseFloat(amount),
date:date,
category:category,
note:note
});

save();
render();

document.getElementById("amount").value="";
document.getElementById("category").value="";
document.getElementById("note").value="";

}


function deleteExpense(index){

expenses.splice(index,1);

save();
render();

}


function monthlyReport(){

let month=prompt("Enter month (YYYY-MM)");

let total=0;

expenses.forEach(e=>{
if(e.date.startsWith(month)){
total+=e.amount;
}
});

document.getElementById("report").innerText=
"Total spending for "+month+": ₱"+total;

}


function categorySummary(){

let summary={};

expenses.forEach(e=>{

summary[e.category]=(summary[e.category]||0)+e.amount;

});

let text="";

for(let cat in summary){

text+=cat+" : ₱"+summary[cat]+"\n";

}

document.getElementById("report").innerText=text;

}


function exportCSV(){

let csv="Amount,Date,Category,Notes\n";

expenses.forEach(e=>{
csv+=`${e.amount},${e.date},${e.category},${e.note}\n`;
});

let blob=new Blob([csv],{type:"text/csv"});

let a=document.createElement("a");
a.href=URL.createObjectURL(blob);
a.download="expenses.csv";
a.click();

}


render();
