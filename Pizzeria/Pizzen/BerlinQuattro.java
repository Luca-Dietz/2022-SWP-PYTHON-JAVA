package Pizzen;
public class BerlinQuattro implements Pizza{

    @Override
    public void backen() {
        System.out.println("BerlinQuattro backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("BerlinQuattro schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("BerlinQuattro einpacken ...");
    }
    
}
