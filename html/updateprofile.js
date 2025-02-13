"use strict";


function submit(){
    let picfiles = document.getElementById("profilepic").files;
    let postname = document.getElementById("postname").value;

    if( picfiles.length === 0 ){
        alert("Please be smarter.")
        return;
    }

    if (postname.length == 0){
        alert("Cmon man give the dang post a name")
        return;
    }


    let fdata = new FormData();
    fdata.append("data", picfiles[0])

    fetch( "/checkImage", {
        method: "POST",
        body: fdata
    }).then( (resp) => {
        resp.json().then( (J) => {
            console.log("Server said:",J);
            document.location.assign( 
                "http://localhost:8080/"); 
        }).catch( (err) => {
            console.log("JSON error:",err);
        })
    }).catch( (err) => {
        console.log("Error:",err);
    });
}

function updatethumb(){
    let picfiles = document.getElementById("profilepic").files;
    if(picfiles.length > 0 ){
        let u = URL.createObjectURL(picfiles[0]);
        let th = document.getElementById("thumbnail");
        th.onload = () => {
            URL.revokeObjectURL(u);
        };
        th.src = u;
    }
}

function recent_img(){
    fetch( "/mostrecent", {
        method: "POST",
        body: fdata
    }).then( (resp) => {
        resp.json().then( (J) => {
            console.log("Server said:",J);
        }).catch( (err) => {
            console.log("JSON error:",err);
        })
    }).catch( (err) => {
        console.log("Error:",err);
    });
    return 0;
}