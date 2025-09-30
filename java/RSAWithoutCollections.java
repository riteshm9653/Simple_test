import java.util.Scanner;

public class RSAWithoutCollections {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input primes and message
        System.out.print("Prime p: ");
        int p = sc.nextInt();

        System.out.print("Prime q: ");
        int q = sc.nextInt();

        System.out.print("Message: ");
        int m = sc.nextInt();

        int n = p * q;
        int phi = (p - 1) * (q - 1);

        // Choose e
        int e = 13;
        while (phi % e == 0) {
            e += 2;
        }

        // Find d (multiplicative inverse of e mod phi)
        int d = 1;
        while ((e * d) % phi != 1) {
            d++;
        }

        // Encryption: c = (m^e) mod n
        int c = modPow(m, e, n);
        System.out.println("Out (Encrypted): " + c);

        // Decryption: m = (c^d) mod n
        int decrypted = modPow(c, d, n);
        System.out.println("Decrypted text: " + decrypted);

        sc.close();
    }

    // Modular exponentiation (to avoid overflow)
    static int modPow(int base, int exp, int mod) {
        long result = 1;
        long b = base % mod;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * b) % mod;
            }
            b = (b * b) % mod;
            exp >>= 1;
        }

        return (int) result;
    }
}
