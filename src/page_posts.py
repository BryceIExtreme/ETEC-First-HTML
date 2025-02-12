def get(): return (
"""<!DOCTYPE html>
<html>
<head>
<title>Post Page</title>
<style>

div.dialog {
        
        border: 2px double black;
        background: white;
        padding-top: 0em;
        padding-left: 1em;
        padding-right: 1em;
        padding-bottom: 1em;

        /* center the div vertically and horizontally
        ref: https://stackoverflow.com/a/13356401 */
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;

        /* set size of dialog */
        width: 20vw;
        height: 45vh;

        overflow: auto;

        z-index: 10;
    }

    table.chart td {
        border: 1px solid black;
    }

    table.chart {
        border-collapse: collapse;
    }
    table.chart tr:nth-child(odd) {
        background: tomato;
        border: 1px solid black;
    }
    table.chart tr:nth-child(even) {
        background: royalblue;
    }
    table.chart {
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }

   
</style>
</head>
<body>

    <span>Posts:</span>
    <div class="dialog">
    <table class="chart">
    <tbody>
    <tr>
        <td><img src="/html/sample10.jpg"></td>
        <td>Posted today.</td>
        <td>Views:321</td></tr>
    
    <tr>
        <td><img src="/html/sample1.jpg"></td>
        <td>Posted 2 days ago.</td>
        <td>Views: 349</td>
    </tr>
    <tr>
        <td><img src="/html/sample2.jpg"></td>
        <td>Posted 3 days ago.</td>
        <td>Views: 43</td>
    </tr>
    <tr>
        <td><img src="/html/sample3.jpg"></td>
        <td>Posted 4 days ago</td>
        <td>Views: 0</td>
    </tr>
    <tr>
        <td><img src="/html/sample4.jpg"></td>
        <td>Posted 5 days ago.</td>
        <td>Views: 12390231</td>
    </tr>
    <tr>
        <td><img src="/html/sample5.jpg"></td>
        <td>Posted 6 days ago.</td>
        <td>Views: 4213279</td>
    </tr>
    <tr>
        <td><img src="/html/sample6.jpg"></td>
        <td>Posted 7 days ago.</td>
        <td>Views: 1</td>
    </tr>
    <tr>
        <td><img src="/html/sample7.jpg"></td>
        <td>Posted 8 days ago.</td>
        <td>Views: 765098</td>
    </tr>
    <tr>
        <td><img src="/html/sample8.jpg"></td>
        <td>Posted 9 days ago.</td>
        <td>Views: 50</td>
    </tr>
    <tr>
        <td><img src="/html/sample9.jpg"></td>
        <td>Posted 10 days ago.</td>
        <td>Views: 78560987809e3</td>
    </tr>
</tbody></table>
</div>
</body>
</html>
""")