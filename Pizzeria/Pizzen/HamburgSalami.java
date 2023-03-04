package Pizzen;
public class HamburgSalami implements Pizza{

    @Override
    public void backen() {
        System.out.println("HamburgSalami backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("HamburgSalami schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("HamburgSalami einpacken ...");
    }
    
}
