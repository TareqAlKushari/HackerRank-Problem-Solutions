package com.mycompany.stringsolving;

public class Main {
    
    
    public static void main(String[] args) { 
        /*String s1 = "hello";
        String s2 = "world";
        
        String grater = "";
        
        int sum = (s1.length() + s2.length());
        int n = s1.compareTo(s2);
        if(n>0) {
            grater = "Yes";
        }
        else
            grater = "No";
        
         
        System.out.println(sum);
        System.out.println(grater);
        System.out.println(s1.substring(0, 1).toUpperCase() + s1.substring(1) + " " + s2.substring(0, 1).toUpperCase() + s2.substring(1));*/
        
        System.out.println(LogLevels.message("[ERROR]: Invalid operation"));
        System.out.println(LogLevels.message("[WARNING]:  Disk almost full\r\n"));
        System.out.println(LogLevels.logLevel("[ERROR]: Invalid operation"));
        System.out.println(LogLevels.reformat("[INFO]: Operation completed"));
    }
}
