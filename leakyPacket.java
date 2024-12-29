import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter initial packets in the bucket: ");
        int storage = scanner.nextInt();

        System.out.print("Enter total number of times bucket content is checked: ");
        int no_of_queries = scanner.nextInt();

        System.out.print("Enter total number of packets that can be accommodated in the bucket: ");
        int bucket_size = scanner.nextInt();

        System.out.print("Enter number of packets that enter the bucket at a time: ");
        int input_pkt_size = scanner.nextInt();

        System.out.print("Enter number of packets that exit the bucket at a time: ");
        int output_pkt_size = scanner.nextInt();

        for (int i = 0; i < no_of_queries; i++) {
            int size_left = bucket_size - storage;

            if (input_pkt_size <= size_left) {
                storage += input_pkt_size;
            } else {
                System.out.println("Packet loss = " + input_pkt_size);
            }

            System.out.println("Buffer size = " + storage + " out of bucket size = " + bucket_size);

            storage -= output_pkt_size;

        }

    }
}


/*
Enter initial packets in the bucket: 3
Enter total number of times bucket content is checked: 5
Enter total number of packets that can be accommodated in the bucket: 10
Enter number of packets that enter the bucket at a time: 5
Enter number of packets that exit the bucket at a time: 2
Buffer size = 8 out of bucket size = 10
Packet loss = 5
Buffer size = 6 out of bucket size = 10
Buffer size = 9 out of bucket size = 10
Packet loss = 5
Buffer size = 7 out of bucket size = 10
Buffer size = 10 out of bucket size = 10

=== Code Execution Successful ===
*/
