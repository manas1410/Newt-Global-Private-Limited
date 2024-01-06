class Human
{
    private int age = 11;
    private String name = "Manas";

    public String getName()
    {
        return name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public int getAge(){
        return age;
    }
}

public class Encapsulation
{
    public static void main(String args[]){
        Human obj = new Human();
        obj.setAge(20);
        System.out.println(obj.getName()+" "+
        obj.getAge());
    }
}