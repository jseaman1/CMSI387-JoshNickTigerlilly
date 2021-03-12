import java.util.Random;
import java.lang.*;

class Question_9_Loops {
    public static void main(String args[]) { 

        
        int arrayLength = 5000;
        Random rd = new Random();
        byte[] testArray = new byte[arrayLength];
        rd.nextBytes(testArray);

        int iterateAmount = 5000;
        double[] timeAverage = new double[iterateAmount];
        for(int i = 0; i < iterateAmount; i++){
          double currentTime = System.nanoTime();
            for(int j = 0; j < arrayLength; j++){
                if(j == 4096){
                    System.out.println("4096th Element Found: " + testArray[j]);
                    double elapsedTime = (System.nanoTime() - currentTime);
                    System.out.println("elaspedTime: " + elapsedTime *.000000001);
                    timeAverage[i] = elapsedTime * .000000001;
                }
            }
        }
        double total = 0;
        for(int i = 0; i < iterateAmount; i++){
          total += timeAverage[i];
        }
        System.out.println("average time per access: " + total/iterateAmount);
    } 
  }