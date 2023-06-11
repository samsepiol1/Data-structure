// Resize Application in Java
public class ResizeArray {
    private String [] s;
    private int N = 0;

    public ResizeArray(int capacity)
    {
        s = new String[1];
    }

    public void push(String item)
    {
        if(N == s.length) resize(2 * s.length);{
            s[N++] = item;
        }
       
    }

    private void resize(int capacity) {
        String[] copy = new String[capacity];
        for(int i = 0; i < N; i++){
            copy[i] = s[i];
        }
    }


    
}
