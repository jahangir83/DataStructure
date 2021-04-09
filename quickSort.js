console.log("Starting sort ' jahangir' ")


let arr = [1,3,5,6,22,45,6,33,7,9]

// for(let i = 0; i < arr.length -1; i++){
    
//     if(arr[i] > arr[i+1]){
//         let temp = arr[i];
//         arr[i] = arr[i + 1]
//         arr[i + 1] = temp
//     }
// }

for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
        if (arr[i] > arr[j]) {
            let temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

}
//
for(let i = 0; i < arr.length; i++){
    console.log(arr[i])
}