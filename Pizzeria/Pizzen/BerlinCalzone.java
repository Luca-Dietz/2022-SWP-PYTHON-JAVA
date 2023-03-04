package Pizzen;
public class BerlinCalzone implements Pizza{

    @Override
    public void backen() {
        System.out.println("BerlinCalzone backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("BerlinCalzone schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("BerlinCalzone einpacken ...");
    }
    
}
