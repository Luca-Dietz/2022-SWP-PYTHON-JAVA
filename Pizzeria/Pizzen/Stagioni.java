package Pizzen;
public class Stagioni implements Pizza{

    @Override
    public void backen() {
        System.out.println("Stagioni backen ...");
    }

    @Override
    public void schneiden() {
        System.out.println("Stagioni schneiden ...");
    }

    @Override
    public void einpacken() {
        System.out.println("Stagioni einpacken ...");
    }
    
}
