function doIt(){
    let title = document.getElementById("title").value;
    let pic = document.getElementById("pic").files;
    if( pic.length === 0 ){
        alert("No file");
        return;
    }
    let fdata = new FormData();
    fdata.append("title",title);
    fdata.append("pic",pic[0]);

    fetch( "/dopost", {
        method:"POST",
        body: fdata
    }).then( (resp) => {
        resp.json().then( (J) => {
            console.log("server said:",J);
            if( J.ok )
                document.location="/";
            else
                alert("Problem: "+J.reason);
        });
    });
}
