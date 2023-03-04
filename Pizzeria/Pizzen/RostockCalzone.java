package Pizzen;
public class RostockCalzone implements Pizza{

    @Override
    public void backen() {
        System.out.println("RostockCalzone backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("RostockCalzone schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("RostockCalzone einpacken ...");
    }
    
}
