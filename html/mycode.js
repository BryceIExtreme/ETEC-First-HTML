"use strict";

function dobcheck(){
    let theinput = document.getElementById("dob");
    let dob = theinput.valueAsNumber;
    let current_date = Date.now();
    let thirteen_years = 13 * 365.25 * 24 * 60 * 60 * 1000;
    let max_allowed_date = current_date - thirteen_years
    if (dob < max_allowed_date)
    {
        alert("This is an invalid date.")
    }
}
