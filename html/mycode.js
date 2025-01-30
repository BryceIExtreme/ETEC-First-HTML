"use strict";


function mega_func(){
    dobcheck();
    emailcheck();
}

function alert_message(){
    alert("Invalid Email");
}

function dobcheck(){
    let theinput = document.getElementById("dob");
    let dob = theinput.valueAsNumber;
    let current_date = Date.now();
    let thirteen_years = 13 * 365.25 * 24 * 60 * 60 * 1000;
    let max_allowed_date = current_date - thirteen_years;
    if (dob > max_allowed_date)
    {
        alert("This is an invalid date.");
    }
}

function emailcheck(){
    let theinput = document.getElementById("email");
    let email = theinput.value;
    let first = email[0];
    let amt = email.length;
    let last_char = email[email.length - 1];
    let i = email.indexOf("@");
    let j = email.lastIndexOf("@");

    if (first == "@"){
        alert_message();
    }
    if (amt < 2){
        alert("Email too short");
    }
    if (last_char == "@"){
        alert_message();
    }   
    if (i != j){
        alert_message();
    }
}
