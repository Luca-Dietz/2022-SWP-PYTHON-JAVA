package Pizzen;
public class Salami implements Pizza{

    @Override
    public void backen() {
        System.out.println("Salami backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("Salami schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("Salami einpacken ...");
    }
    
}
