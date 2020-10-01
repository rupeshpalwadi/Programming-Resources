import java.util.*;

public class BubbleSort {
    static int arr[] = {7, 1, 4, 6, 2, 3, 4, 4, 5};
    
    public static void main(String[] args) {
        System.out.println(Arrays.toString(sort(arr)));
    }
    
    static int[] sort(int[] arr) {
        int temp = 0;
        
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        
        return arr;
    }
}
