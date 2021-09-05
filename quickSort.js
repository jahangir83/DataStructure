console.log("Starting sort ' jahangir' ")




// for(let i = 0; i < arr.length -1; i++){
    
//     if(arr[i] > arr[i+1]){
//         let temp = arr[i];
//         arr[i] = arr[i + 1]
//         arr[i + 1] = temp
//     }
// }
let arr = [1,3,5,6,22,45,6,33,7,9]
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
console.log(7 + ( 10 - 7) / 2)
console.log((5 ^ 8) % 2)
/*

  static List<Integer> dynamicArray(int n, List<List<Integer>> queries) {
    List<List<Integer>>  computation = new ArrayList<>();
    List<Integer>  result = new ArrayList<>();

    for (int i = 0; i < n; i++) {
      computation.add(new ArrayList<>());
    }

    int lastAnswer = 0;
    for (int i = 0; i < queries.size(); i++) {
      List<Integer> q = queries.get(i);

      if (q.get(0) == 1) {
        computation.get((q.get(1) ^ lastAnswer) % n).add(q.get(2));
      } else {
        List<Integer> seq = computation.get((q.get(1) ^ lastAnswer) % n);
        lastAnswer = seq.get(q.get(2) % seq.size());
        result.add(lastAnswer);
      }
    }

    return result;
  }

*/

let sum = [1,2,4,5,6,7,8]
console.log(sum)
sum.forEach((a) => {
    console.log(a += a) 
})