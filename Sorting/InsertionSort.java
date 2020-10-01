import java.util.*;

public class InsertionSort {
    static int arr[] = {7, 1, 4, 6, 2, 3, 4, 4, 5};

    public static void main(String[] args) {
        System.out.println(Arrays.toString(sort(arr)));
    }

    static int[] sort(int[] arr) {
        int key, temp, c;

        for (int i = 1; i < arr.length; i++) {
            key = arr[i];
            c = i - 1;

            while (c >= 0 && key < arr[c]) {
                temp = arr[c+1];
                arr[c+1] = arr[c];
                arr[c] = temp;
                
                c--;
            }
        }

        return arr;
    }
}
