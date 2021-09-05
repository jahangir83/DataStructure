public class SortingAlgoritm {
    
//TODO: Quick Sort Algorithms Start
// Create swap Function  Start
public static void swap(int[] arr, int i, int j){
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

// TODO: There will be parameter inside < Array, 0 Index, arr length >

public static void Quick_sort(int[] arr, int low, int heigh){

    // cheack array length
    if(low < heigh){

        // partition index and is now at the right place
        int partition = __partition(arr, low, heigh);

        // Seperately sort elment before Parameter and after partition ( Recursive call)
        Quick_sort(arr, low, partition - 1);
        Quick_sort(arr, partition + 1, heigh);
    }
}
// TODO: Create Partition function
static int __partition(int[] arr, int low, int heigh){

    // Declare pivot item
    int pivot = arr[heigh];
    // Index of smaller element and indicates the right position of pivot found so far
    int i = low - 1;

    // Run the loop
    for(int j = low; j <= heigh - 1; j++){
        // If current element is smaller than the pivot
        if(arr[j] < pivot){
            
            // Increment index of smaller element
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, heigh);

    return i + 1;  
  
}
// TODO: Quick Sort Algorithms End  

// TODO: Merge Sort Algorithm Start
public static void MergeSort(int[] arr, int low, int arrlength){
    if(low < arrlength){
        
        // Declare middle point
        int middle = low + (arrlength - low) / 2;

        // Sort the first to middle ( Recursive call)
        MergeSort(arr, low, middle);
        MergeSort(arr, middle + 1, arrlength);

        // Then my array merge
        merge(arr, low, middle, arrlength);


    }
}

// TODO: Create Merge function 
static void merge(int[] arr, int low, int middle, int arrlenght){

    // Innitial Temp Array ( Left & Rignt ) size
    int Left_size = middle - low + 1;
    int Right_size = arrlenght - middle;

    // Initial Temp Array ( Left & Right)
    int[] Left = new int[Left_size];
    int[] Right = new int[Right_size];


    //  copy the Value array Assing  ( Left & Right) Array
    for(int i =0; i < Left_size; i++){
        Left[i] = arr[low + i];
    }
    for(int j = 0; j < Right_size; j++){
        Right[j] = arr[j + 1 + middle];
    }

    int i =0;int j = 0; int k = low;
    while(i < Left_size && j < Right_size){
        if(Left[i] <= Right[j]){
            arr[k] = Left[i];
            i++;
        }else{
            arr[k] = Right[j];
            j++;
        }
        k++;
    }

    // Copy remaining element of Left[] 
    while(i < Left_size){
        arr[k] = Left[i];
        i++;
        k++;
    }
    // Copy remaining element of Right[] 
    while(i < Right_size){
        arr[k] = Right[j];
        j++;
        k++;
    }
}
// TODO: Merge Sort Algorithm End



// TODO: Create Insertion Algorithms Start 
public static void insertionSort(int[] arr){
    //Need Variable
    int j, item;

    // Run the loop i
    for(int i = 0; i < arr.length; i++){
        j = i -1;
        item = arr[i];
        while(j >= 0 && arr[j] > item){
            arr[j + 1] = arr[j];
            j -= 1;
        }
        arr[j + 1] = item;
        
    }
}
// TODO: Create Insertion Algorithms End

// TODO: Create Selection Algorithms Start
public static void SelectionSort(int[] arr){
int i , j , min_index;
    for(i = 0 ; i < arr.length - 1; i++){

        min_index = i;
        for(j = i + 1; j < arr.length ; j++){
            if(arr[j] < arr[min_index]){
                min_index = j;
            }
        }
        //swap
        swap(arr, i, min_index);
    }
}
// TODO: Create Selection Algorithms End
// TODO: Create Bubble Sort Algorithms Start
public static void Bubble_sort(int[] arr) {
    for (int i = 0; i < arr.length; i++) {

        for (int j = 0; j < arr.length - i - 1; j++) {

            // Check The value and swap
            if (arr[j] > arr[j + 1]) {
                swap(arr, j, j + 1);
            }
        }
    }
}
// TODO: Create Bubble Sort Algorithms End

// Defual print element function
static void PrintItem(int[] arr){
    for(int i = 0; i < arr.length; i++){
        System.out.print(arr[i] + " ");
    }
    System.out.println();
}

    public static void main(String[] args) {
        int[] array = {2,4,5,1,7,10,9,8};
        PrintItem(array);
        // Quick_sort(array, 0, array.length-1);
        // MergeSort(array, 0, array.length - 1);
        // Bubble_sort(array);
        // insertionSort(array);
        SelectionSort(array);
        PrintItem(array);
    }
}
