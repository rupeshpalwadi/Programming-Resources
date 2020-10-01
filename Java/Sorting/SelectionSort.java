import java.util.*;

public class SelectionSort {
    static int arr[] = {7, 1, 4, 6, 2, 3, 4, 4, 5};

    public static void main(String[] args) {
        System.out.println(Arrays.toString(sort(arr)));
    }

    static int[] sort(int[] arr) {
        int min, temp;

        for (int i = 0; i < arr.length; i++) {
            min = i;

            for (int j = i; j < arr.length; j++) {
                if (arr[j] < arr[min])
                    min = j;
            }
            
            temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;

        }

        return arr;
    }
}
