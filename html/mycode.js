"use strict";


function mega_func(){
    dobcheck();
    emailcheck();
}

function alert_message(error_no){
    let elem = document.getElementById("foo");
    if (elem == null){
        elem = document.createElement("div");
        elem.setAttribute("id", "foo");
        elem.classList.add("alert");
        document.body.appendChild(elem);
    }
    else {
        elem.innerHTML = "";
    }
    if (error_no == 1){
        elem.appendChild( document.createTextNode( "Your email can't start with an @." ) );
    }
    else if (error_no == 2){
        elem.appendChild( document.createTextNode( "Your email is too short." ) );
    }
    else if (error_no == 3){
        elem.appendChild( document.createTextNode( "Your email cannot end with an @ silly." ) );
    }
    else if (error_no == 4){
        elem.appendChild( document.createTextNode( "Your email has too many @s." ) );
    }
    else {
        elem.classList.add("banner");
        elem.appendChild( document.createTextNode( "Welcome to the same exact page" ) );
    }
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
        alert_message(1);
    }
    else if (amt < 1){
        alert_message(2);
    }
    else if (last_char == "@"){
        alert_message(3);
    }   
    else if (i != j){
        alert_message(4);
    }
    else {
        alert_message(0);
    }
}
