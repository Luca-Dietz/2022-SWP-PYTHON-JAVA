package Pizzen;
public class RostockSalami implements Pizza{

    @Override
    public void backen() {
        System.out.println("RostockSalami backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("RostockSalami schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("RostockSalami einpacken ...");
    }
    
}
