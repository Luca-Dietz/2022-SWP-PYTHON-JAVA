package Pizzen;
public class Hawaii implements Pizza{

    @Override
    public void backen() {
        System.out.println("Hawaii backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("Hawaii schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("Hawaii einpacken ...");
    }
    
}
