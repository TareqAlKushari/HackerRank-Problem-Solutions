package com.mycompany.stringsolving;

public class LogLevels {
    
    public static String message(String logLine) {
        int n = (int)logLine.indexOf(":");
        String str = new String();
        str = logLine.substring(n+2).trim();
        return (String)(str);
    }

    public static String logLevel(String logLine) {
        int n = (int)logLine.indexOf("]");
        String str = new String();
        str = logLine.substring(1, n).toLowerCase().trim();
        return (String)(str);
    }

    public static String reformat(String logLine) {
        int n = (int)logLine.indexOf(":");
        int m = (int)logLine.indexOf("]");
        String str = new String();
        str = logLine.substring(1, m).toLowerCase();
        return (String)(logLine.substring(n+2) + " (" + str + ")");
    }
}