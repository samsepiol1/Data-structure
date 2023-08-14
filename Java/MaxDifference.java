public class MaxDifference {
    // Part 1
    int max = 0;
    public static int MaxDifference(int [] vals){

        // Part 2

                // The Two Fors the represent O(N2)
        for(int i = 0; i < vals.length; i++){
            for(int j = 0; j < vals.length; j++){
                // O(1)
                if(vals [i] - vals[j] > max){
                    max = vals[i] - vals[j];
                }
            }
        }

      

    }
         // Part 2
         // O(1)
      return max;
    
}
