// Best Case in One letter is O(1)

// Worst Case - We have to complete the whole array O(N)
// Best Case <= Worst Case

public class has_letter {
    public static boolean hasLetter(String word, char letter){
        for(int i = 0; i < word.length() ; i++ ){
            if(word.charAt(i) == letter){
                return true; 
            }
        }
    }
    return false;
}

