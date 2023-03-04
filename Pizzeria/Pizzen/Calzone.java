package Pizzen;
public class Calzone implements Pizza{

    @Override
    public void backen() {
        System.out.println("Calzone backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("Calzone schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("Calzone einpacken ...");
    }
    
}
