def get(): return (
"""<!DOCTYPE html>
<html>
<head>
<title>Test Page</title>
<style>
    .titlebar {
        background: blue;
        border: 1px solid black;
    }   
    .menubutton {
    position: relative;
    left: 0px;
    top: 0px;
    }
    .textbox {
    position: relative;
    left:90%;
    top: 0px;
    font-weight:bold;
    color: solid black
    }
</style>
</head>
<body>
<div>
    <div class="titlebar">
    <span class="textbox">
    "Hello, NAME"

    </span>
    
</div>
</body>
</html>
""")