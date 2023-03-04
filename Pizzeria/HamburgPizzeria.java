import Pizzen.*;

public class HamburgPizzeria extends Pizzeria{

    @Override
    protected Pizza getpizza(String name) {
        if (name == null || name.isEmpty())
        return null;
        switch (name) {
        case "HamburgSalami":
            return new HamburgSalami();
        case "HamburgHawaii":
            return new HamburgHawaii();
        case "HamburgCalzone":
            return new HamburgCalzone();
        case "HamburgQuattro":
            return new HamburgQuattro();
        case "HamburgStagioni":
            return new HamburgStagioni();
        default:
            throw new IllegalArgumentException("Unknown pizza " + name);
    }
    }
    
}
