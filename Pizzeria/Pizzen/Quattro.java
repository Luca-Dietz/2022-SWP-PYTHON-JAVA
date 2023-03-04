package Pizzen;
public class Quattro implements Pizza{

    @Override
    public void backen() {
        System.out.println("Quattro backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("Quattro schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("Quattro einpacken ...");
    }
    
}
