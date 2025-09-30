import java.util.Scanner;

public class DiffieHellman {
    // Modular exponentiation function (to compute g^x mod p efficiently)
    static long modPow(long base, long exp, long mod) {
        long result = 1;
        base = base % mod;
        while (exp > 0) {
            if ((exp & 1) == 1) { // if exp is odd
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1; // divide exp by 2
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Prime p: ");
        int p = sc.nextInt();

        System.out.print("Primitive root g: ");
        int g = sc.nextInt();

        System.out.print("Alice key (a): ");
        int a = sc.nextInt();

        System.out.print("Bob key (b): ");
        int b = sc.nextInt();

        // Public keys
        long A = modPow(g, a, p);
        long B = modPow(g, b, p);

        // Shared secrets
        long aliceSecret = modPow(B, a, p);
        long bobSecret = modPow(A, b, p);

        // Final shared key (g^(a*b) mod p)
        long key = modPow(g, (long) a * b, p);

        System.out.println("Alice secret: " + aliceSecret);
        System.out.println("Bob secret:   " + bobSecret);
        System.out.println("Out (Shared Key): " + key);

        sc.close();
    }
}
