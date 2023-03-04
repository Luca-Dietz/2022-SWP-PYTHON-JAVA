package Pizzen;
public class BerlinHawaii implements Pizza{

    @Override
    public void backen() {
        System.out.println("BerlinHawaii backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("BerlinHawaii schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("BerlinHawaii einpacken ...");
    }
    
}
