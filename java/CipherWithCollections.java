public class CipherWithCollections {

    // Caesar Cipher
    public static String caesarCipher(String text, int shift) {
        char[] chars = text.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                chars[i] = (char) ((c - base + shift) % 26 + base);
            }
        }
        return new String(chars);
    }

    // Atbash Cipher
    public static String atbashCipher(String text) {
        char[] chars = text.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                chars[i] = (char) (25 - (c - base) + base);
            }
        }
        return new String(chars);
    }

    // ROT13 Cipher
    public static String rot13Cipher(String text) {
        return caesarCipher(text, 13);
    }

    public static void main(String[] args) {
        String msg = "Hello World";

        System.out.println("Caesar (+3): " + caesarCipher(msg, 3));
        System.out.println("Atbash: " + atbashCipher(msg));
        System.out.println("ROT13: " + rot13Cipher(msg));
    }
}
