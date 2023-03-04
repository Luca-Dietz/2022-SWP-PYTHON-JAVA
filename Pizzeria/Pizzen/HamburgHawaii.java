package Pizzen;
public class HamburgHawaii implements Pizza{

    @Override
    public void backen() {
        System.out.println("HamburgHawaii backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("HamburgHawaii schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("HamburgHawaii einpacken ...");
    }
    
}
