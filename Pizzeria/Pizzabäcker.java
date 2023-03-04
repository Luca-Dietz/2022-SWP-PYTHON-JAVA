import Pizzen.Pizza;

public class Pizzabäcker{
    public static void main(String[] args)
    {
        Pizzeria pizzeria = new PizzaFactory();
        Pizza salaPizza = pizzeria.newpizza("Salami");
        
        Pizzeria rostockpizzeria = new RostockPizzeria();
        Pizza rostocksalami = rostockpizzeria.newpizza("RostockSalami");

        Pizzeria berlinpizzeria = new BerlinPizzeria();
        Pizza berlinsalami = berlinpizzeria.newpizza("BerlinSalami");

        Pizzeria hamburgpizzeria = new HamburgPizzeria();
        Pizza hamburgsalami = hamburgpizzeria.newpizza("HamburgSalami");
    }
}