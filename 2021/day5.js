// advent of code 5

let dt = document.getElementsByTagName('pre')[0].innerText.split('\n');
// for
let xy = dt[0].split(' -> ');
let unit = xy[0].split(',');
let x1 = unit[0];
let y1 = unit[1];

function matrix(rows, cols, defaultValue) {
    let arr = [];
    for (let i = 0; i < rows; i++) {
        arr.push([]);
        arr[i].push(new Array(cols));
        for (var j = 0; j < cols; j++) {
            arr[i][j] = defaultValue;
        }
    }
    return arr;
}

console.log(x1 + " : " + y1);
