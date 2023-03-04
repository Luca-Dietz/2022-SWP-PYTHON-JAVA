package Pizzen;
public class RostockHawaii implements Pizza{

    @Override
    public void backen() {
        System.out.println("RostockHawaii backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("RostockHawaii schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("RostockHawaii einpacken ...");
    }
    
}
