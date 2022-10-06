let num=10;
let acum=1;
factorial: while(true){
    acum=acum*num;
    num--;
    if(num<1){
        break factorial;
    }
}
console.log(acum)