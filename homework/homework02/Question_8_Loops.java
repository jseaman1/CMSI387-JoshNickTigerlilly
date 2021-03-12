package homework02;

import java.util.Random;
import java.time.Clock;


public class Question_8_Loops {  
    
    public static void main(String args[]) { 

        
        int arrayLength = 1000000000;
        Random rd = new Random();
        byte[] testArray = new byte[arrayLength];
        rd.nextBytes(testArray);

        int iterateAmount = 200;
        for(int i = 0; i < iterateAmount; i++){
            for(int j = 0; j < arrayLength; j++){
                if(j == 4096){
                    System.out.println.gc("4096th Element Found: " + testArray[j]);
                }
            }
        }
    } 
  }

//   int main(int argc, char * argv[]) {
//     char largeArray [4096];
//     char accessed;
//     clock_t t; 
//     t = clock();
//     for (int i = 0; i < sizeof(largeArray); i++) {
//         accessed = largeArray[i];
//     }
//     t = clock() - t; 
//     double time_taken = ((double)t)/CLOCKS_PER_SEC;
//     printf("loop took %f seconds to execute \n", time_taken);

//     return 0;
// }