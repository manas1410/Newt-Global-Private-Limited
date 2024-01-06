class Human
{
    private int age = 11;
    private String name = "Manas";

    public String getName()
    {
        return name;
    }
    
}

public class Encapsulation
{
    public static void main(String args[]){
        Human obj = new Human();
        System.out.println(obj.getName());
    }
}