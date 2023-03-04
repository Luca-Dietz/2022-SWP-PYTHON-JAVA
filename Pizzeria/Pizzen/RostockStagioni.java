package Pizzen;
public class RostockStagioni implements Pizza{

    @Override
    public void backen() {
        System.out.println("RostockStagioni backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("RostockStagioni schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("RostockStagioni einpacken ...");
    }
    
}
