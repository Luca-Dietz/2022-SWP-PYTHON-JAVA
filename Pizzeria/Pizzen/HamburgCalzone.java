package Pizzen;
public class HamburgCalzone implements Pizza{

    @Override
    public void backen() {
        System.out.println("HamburgCalzone backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("HamburgCalzone schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("HamburgCalzone einpacken ...");
    }
    
}
