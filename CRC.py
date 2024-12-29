import java.util.Scanner;

public class Main {

    // XOR operation for binary strings
    public static String xor(String dividend, String divisor) {
        StringBuilder result = new StringBuilder();
        for (int i = 1; i < divisor.length(); i++) {
            result.append(dividend.charAt(i) == divisor.charAt(i) ? '0' : '1');
        }
        return result.toString();
    }

    // CRC computation using the given generator polynomial
    public static String crc(String data, String genPoly) {
        int genLength = genPoly.length();

        // Append n-1 zeros to the data
        String paddedData = data + "0".repeat(genLength - 1);
        String temp = paddedData.substring(0, genLength);

        for (int i = 0; i <= paddedData.length() - genLength; i++) {
            if (temp.charAt(0) == '1') {
                // Perform XOR if the first bit is 1
                temp = xor(temp, genPoly);
            } else {
                // Keep shifting if the first bit is 0
                temp = temp.substring(1);
            }
            // Shift left and append the next bit
            if (i + genLength < paddedData.length()) {
                temp += paddedData.charAt(i + genLength);
            }
        }

        // The remainder is the final n-1 bits
        return temp;
    }

    // Receiver side simulation to check for errors
    public static void receiver(String data, String genPoly) {
        System.out.println("\n-----------------------------");
        System.out.println("Data received: " + data);

        // Perform CRC computation on received data
        String remainder = crc(data, genPoly);

        // Check if the remainder is all zeros
        if (remainder.contains("1")) {
            System.out.println("Error detected");
        } else {
            System.out.println("No error detected");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input data and generator polynomial
        System.out.print("Enter data to be transmitted: ");
        String data = scanner.nextLine().trim();

        System.out.print("Enter the Generating polynomial: ");
        String genPoly = scanner.nextLine().trim();

        // Compute CRC check value
        String checkValue = crc(data, genPoly);
        System.out.println("\n----------------------------------------");
        System.out.println("Data padded with n-1 zeros: " + data + "0".repeat(genPoly.length() - 1));
        System.out.println("CRC or Check value is: " + checkValue);

        // Append check value to data for transmission
        String transmittedData = data + checkValue;
        System.out.println("Final data to be sent: " + transmittedData);
        System.out.println("---------------------------------------\n");

        // Simulate the receiver side
        System.out.print("Enter the received data: ");
        String receivedData = scanner.nextLine().trim();
        receiver(receivedData, genPoly);

        scanner.close();
    }
}
/*
Enter data to be transmitted: 1001100
Enter the Generating polynomial: 1101

----------------------------------------
Data padded with n-1 zeros: 1001100000
CRC or Check value is: 001
Final data to be sent: 1001100001
---------------------------------------

Enter the received data: 1001100001

-----------------------------
Data received: 1001100001
No error detected

=== Code Execution Successful ===
*/
