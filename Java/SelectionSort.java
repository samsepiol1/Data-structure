public class SelectionSort {
    int indexMin; 

    public static void SelectionSort(int [] vals){
        indexMin = i;


        // Nested Loop

        for(int i = 0; i < vals.length; i++){
            indexMin = i;


            // O(n - (i + 1))

            for(int j= i + 1; j < vals.length; j++){

                // O(1)
                if(vals[j] < vals[indexMin]){
                    indexMin = j;
                }
            }

            // O(1)

            // Swap Operation

            // temp = vals[indexMin]

            // vals[indexMin] = vals[i]
            // vals[i] = temp


            swap(vals, indexMin, i)
        }
    }
    
}
