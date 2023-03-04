package Pizzen;
public class HamburgStagioni implements Pizza{

    @Override
    public void backen() {
        System.out.println("HamburgStagioni backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("HamburgStagioni schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("HamburgStagioni einpacken ...");
    }
    
}
