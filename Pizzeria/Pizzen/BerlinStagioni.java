package Pizzen;
public class BerlinStagioni implements Pizza{

    @Override
    public void backen() {
        System.out.println("BerlinStagioni backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("BerlinStagioni schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("BerlinStagioni einpacken ...");
    }
    
}
