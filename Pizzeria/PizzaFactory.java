import Pizzen.Calzone;
import Pizzen.Hawaii;
import Pizzen.Pizza;
import Pizzen.Quattro;
import Pizzen.Salami;
import Pizzen.Stagioni;

public class PizzaFactory extends Pizzeria{

    @Override
    protected Pizza getpizza(String name) {
        if (name == null || name.isEmpty())
            return null;
        switch (name) {
        case "Salami":
            return new Salami();
        case "Hawaii":
            return new Hawaii();
        case "Calzone":
            return new Calzone();
        case "Quattro":
            return new Quattro();
        case "Stagioni":
            return new Stagioni();
        default:
            throw new IllegalArgumentException("Unknown pizza " + name);
        }
    }
}