import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.ListIterator;
import java.util.Scanner;

//TODO: lavbel the data in a way that will be accepted my the ml
class labeler{
    public static void main(String[] args) throws IOException {
        File rawDataFile = new File("/Users/caleb/IdeaProjects/leetCode/labelingMonster/ExcelFiles/rawTrainingData.csv");
        File outputFile = new File("/Users/caleb/IdeaProjects/leetCode/labelingMonster/ExcelFiles/trainingData.csv");

        FileWriter fileWriter = new FileWriter(outputFile);
        fileWriter.write("questionID,tsStamp,pulse,skin_conductivity,respiration_belt,blood_pressure,actual_ans\n");

        Scanner fileReader = new Scanner(rawDataFile);

        ArrayList examID = new ArrayList();
        ArrayList  questionID = new ArrayList();
        ArrayList  tsStamp = new ArrayList();
        ArrayList  pulse = new ArrayList();
        ArrayList  skin_conductivity = new ArrayList();
        ArrayList  respiration_belt = new ArrayList();
        ArrayList  blood_pressure = new ArrayList();
        ArrayList  actual_ans = new ArrayList();

        while(fileReader.hasNextLine()){
            String [] regex = fileReader.nextLine().split(",");
            examID.add(regex[0]);
            questionID.add(regex[1]);
            tsStamp.add(regex[4]);
            pulse.add(regex[5]);
            skin_conductivity.add(regex[6]);
            respiration_belt.add(regex[7]);
            blood_pressure.add(regex[8]);
            actual_ans.add(regex[11]);


        }
        String qID = (String) questionID.get(1);
        double ts = 0.00;
        double plse = 0.00;
        double skin_con = 0.00;
        double repi = 0.00;
        double bp = 0.00;
        String actualAns = "";

        int counter = 0;
        //old
       for(int  i = 1;  i < examID.size(); i++){
           counter++;

               if(qID.equals((String) questionID.get(i))){//
                 try {
                     ts += Double.parseDouble((String) tsStamp.get(i));
                 }   catch (NumberFormatException E){
                        ts += 0;
                 }
                 try {
                     plse += Double.parseDouble((String) pulse.get(i)) ;
                 }   catch (NumberFormatException E){
                     plse += 0;
                 }
                 try {
                     skin_con += Double.parseDouble((String) skin_conductivity.get(i)) ;
                 }   catch (NumberFormatException E){
                     skin_con += 0;
                 }
                 try {
                     repi += Double.parseDouble((String) respiration_belt.get(i));
                 }   catch (NumberFormatException E){
                     repi += 0;
                 }
                 try {
                     bp += Double.parseDouble((String) blood_pressure.get(i));
                 }   catch (NumberFormatException E){
                     bp+= 0;
                 }
                   actualAns = String.valueOf((label(String.valueOf(actual_ans.get(i)))));
               }else {
                  fileWriter.write(qID +"," +(ts/counter)+","+ (plse/counter) + "," + (skin_con/counter) +"," +(repi/counter)+","+ (bp/counter)+","+ actualAns +"\n" );

                   qID = (String) questionID.get(i);
                   //System.out.printf("%s, %s, %s, %s, %s, %s, %s\n", qID, ts, plse,skin_con, repi, bp, actualAns );
                   try {
                       ts = Double.parseDouble((String) tsStamp.get(i));
                   }   catch (NumberFormatException E){
                       ts = 0;
                   }
                   try {
                       plse = Double.parseDouble((String) pulse.get(i)) ;
                   }   catch (NumberFormatException E){
                       plse = 0;
                   }
                   try {
                       skin_con = Double.parseDouble((String) skin_conductivity.get(i)) ;
                   }   catch (NumberFormatException E){
                       skin_con = 0;
                   }
                   try {
                       repi = Double.parseDouble((String) respiration_belt.get(i));
                   }   catch (NumberFormatException E){
                       repi = 0;
                   }
                   try {
                       bp  = Double.parseDouble((String) blood_pressure.get(i));
                   }   catch (NumberFormatException E){
                       bp = 0;
                   }
                   actualAns = "false";
                   counter = 0;

               }
               //System.out.printf("%s, %s, %s, %s, %s, %s, %s\n", qID, ts, plse,skin_con, repi, bp, actualAns );
                qID = (String) questionID.get(i);


       }
        fileWriter.close();

    //get the index where the exam id chnages
        //get the index where the question id chnages
        //
    }

    static double mean(ArrayList <Double>list){
        double sum = 0;
        for(int i = 0; i < list.size(); i++){
            sum += list.get(i);
        }
        return (sum/list.size());
    }
    static boolean label(String string){
        if(string.equals("True") || string.equals("T") || string.equals("true") || string.equals("t")){
            return true;
        }
        return false;
    }




}