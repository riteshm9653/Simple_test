public class RailFenceWithoutCollections {

    public static String railFenceCipher(String text, int rails) {
        // Use array of char arrays to simulate the fence
        char[][] fence = new char[rails][text.length()];

        // Fill with spaces initially
        for (int i = 0; i < rails; i++) {
            for (int j = 0; j < text.length(); j++) {
                fence[i][j] = '\0'; // null char
            }
        }

        int rail = 0, step = 1;
        for (int col = 0; col < text.length(); col++) {
            fence[rail][col] = text.charAt(col);
            rail += step;

            if (rail == 0 || rail == rails - 1) {
                step *= -1;
            }
        }

        // Read row by row
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < rails; i++) {
            for (int j = 0; j < text.length(); j++) {
                if (fence[i][j] != '\0') {
                    result.append(fence[i][j]);
                }
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String msg = "HELLO WORLD";

        System.out.println("3 rails: " + railFenceCipher(msg, 3));
        System.out.println("4 rails: " + railFenceCipher(msg, 4));
    }
}

// import java.util.*;

// public class RailFenceWithCollections {

// public static String railFenceCipher(String text, int rails) {
// // Create a list of StringBuilder (one for each rail)
// List<StringBuilder> fence = new ArrayList<>();
// for (int i = 0; i < rails; i++) {
// fence.add(new StringBuilder());
// }

// int rail = 0;
// int step = 1;

// for (char c : text.toCharArray()) {
// fence.get(rail).append(c);

// rail += step;

// if (rail == 0 || rail == rails - 1) {
// step *= -1; // change direction
// }
// }

// // Merge all rails
// StringBuilder result = new StringBuilder();
// for (StringBuilder sb : fence) {
// result.append(sb);
// }
// return result.toString();
// }

// public static void main(String[] args) {
// String msg = "HELLO WORLD";

// System.out.println("3 rails: " + railFenceCipher(msg, 3));
// System.out.println("4 rails: " + railFenceCipher(msg, 4));
// }
// }
