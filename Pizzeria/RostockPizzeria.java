import Pizzen.*;

public class RostockPizzeria extends Pizzeria{

    @Override
    protected Pizza getpizza(String name) {
        if (name == null || name.isEmpty())
            return null;
        switch (name) {
        case "RostockSalami":
            return new RostockSalami();
        case "RostockHawaii":
            return new RostockHawaii();
        case "RostockCalzone":
            return new RostockCalzone();
        case "RostockQuattro":
            return new RostockQuattro();
        case "RostockStagioni":
            return new RostockStagioni();
        default:
            throw new IllegalArgumentException("Unknown pizza " + name);
        }
    }
    
}
