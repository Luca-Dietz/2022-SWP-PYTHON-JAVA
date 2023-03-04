package Pizzen;
public class HamburgQuattro implements Pizza{

    @Override
    public void backen() {
        System.out.println("HamburgQuattro backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("HamburgQuattro schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("HamburgQuattro einpacken ...");
    }
    
}
