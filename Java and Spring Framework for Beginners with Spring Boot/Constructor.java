class Human
{
    private int age;
    private String name ;

    Human(){
        age = 11;
        name = "Manas";
    }

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

public class Constructor
{
    public static void main(String args[]){
        Human obj = new Human();
        obj.setAge(20);
        System.out.println(obj.getName()+" "+
        obj.getAge());
    }
}