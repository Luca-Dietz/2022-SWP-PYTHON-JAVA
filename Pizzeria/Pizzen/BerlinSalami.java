package Pizzen;
public class BerlinSalami implements Pizza{

    @Override
    public void backen() {
        System.out.println("BerlinSalami backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("BerlinSalami schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("BerlinSalami einpacken ...");
    }
    
}
