
public class BoundedBufferTests {

    public static void main(String[] args) {
        BoundedBuffer test = new BoundedBuffer();
        
        class InsertRunnable extends Thread {
          public void run() {
            try {
              test.insert(10);
              System.out.println("10 input into buffer");
            } catch (InterruptedException e) {
              System.out.println("wat");
            }
          }
        }

        class RetriveRunnable extends Thread {
          public void run() {
            try {
              System.out.print("we have retrieved: ");
              System.out.println(test.retrieve());
            } catch (InterruptedException e) {
              System.out.println("wat");
            }
          }
        }

        InsertRunnable t1 = new InsertRunnable();
        RetriveRunnable t2 = new RetriveRunnable();
        
        t1.start();
        t2.start();

        try {
          t1.join();
          t2.join();
        } catch (InterruptedException e) {
          System.out.println("strange");
        }
        
      }
    
}
