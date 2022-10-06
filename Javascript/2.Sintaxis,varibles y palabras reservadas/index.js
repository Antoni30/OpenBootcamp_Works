let fecha_nacimiento = new Date(1998,11,19);
const libro={
    "titulo":"El sabueso de Baskerville",
    "autor":"Conan Doyle",
    "fecha":2010,
    "url":"http:amazon/Sabueso-de-Baskerville/..."
}
const lista=["Antoni",23,true, fecha_nacimiento,libro]

console.log(lista)

/*
function contParalelas(arr1, arr2) {
  let cont = 0;
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2.length; j++) {
      if (arr1[i] === arr2[j]) {
          if (arr1[i + 1] === arr2[j + 1] && arr1[i + 1] != undefined) {
            console.log(
              arr1[i] + ":" + arr2[j] + " " + arr1[i + 1] + ":" + arr2[j + 1]
            );
            cont++;
          }
      }
    }
  }
  return cont;
}
const arr = ["b", "a", "c", "d", "f", "e"];
const arr2 = ["a", "c", "b", "c", "d", "f", "e"];

console.log("Existe " + contParalelas(arr, arr2) + " paralelas");
//Solucion de numero de paralelas
*/
