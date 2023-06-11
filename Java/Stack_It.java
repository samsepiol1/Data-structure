import java.util.Iterator;

import org.w3c.dom.Node;
public class Stack_It<item> implements Iterable<Item>{

    public Iterator<Item> iterator()
    {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item>{
        private Node current = first;

        public boolean hasNext(){
            return current != null;
        }

        public void remove(){
            
        }

        public Item next(){

            Item item = current.item;
            current = current.next;
            return item;
        }

    }


    
}
