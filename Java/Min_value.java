public static void reduce (int [] vals) {


    // Part One

    // O(1)

    int minIndex = 0;

    // Part Two

    // The whole loop is O(N)

                       // O(N)    //O(N)
    for(int i=0; i < vals.length;  i++){

        if(vals[i] < vals[minIndex]){
            minIndex = i; //O(N)
        }


    // Part Three 

    // O(1)

    int minVal = vals[minIndex];



    // Part Four

      // The whole loop is O(N)
    for(int i = 0; i < vals.lenght; i++){
        vals[i] = vals[i] - minVal;
    }


    }
    
}
