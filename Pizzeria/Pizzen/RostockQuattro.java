package Pizzen;
public class RostockQuattro implements Pizza{

    @Override
    public void backen() {
        System.out.println("RostockQuattro backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("RostockQuattro schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("RostockQuattro einpacken ...");
    }
    
}
