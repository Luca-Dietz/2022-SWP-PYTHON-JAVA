import Pizzen.*;

public class BerlinPizzeria extends Pizzeria{
    @Override
    protected Pizza getpizza(String name) {
        if (name == null || name.isEmpty())
            return null;
        switch (name) {
        case "BerlinSalami":
            return new BerlinSalami();
        case "BerlinHawaii":
            return new BerlinHawaii();
        case "BerlinCalzone":
            return new BerlinCalzone();
        case "BerlinQuattro":
            return new BerlinQuattro();
        case "BerlinStagioni":
            return new BerlinStagioni();
        default:
            throw new IllegalArgumentException("Unknown pizza " + name);
        }
    }
    
}
