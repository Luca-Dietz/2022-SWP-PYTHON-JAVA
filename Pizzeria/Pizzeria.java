import Pizzen.*;

public abstract class Pizzeria {
    public Pizza newpizza(String name) {
        Pizza p = getpizza(name);
        p.backen();
        p.schneiden();
        p.einpacken();
        return p;
    }

    protected abstract Pizza getpizza(String name);

}
