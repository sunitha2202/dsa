class Solution:

    def mergeSort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(arr, left, mid)  # Sort the left half
            self.mergeSort(arr, mid + 1, right)  # Sort the right half
            self.merge(arr, left, mid, right)  # Merge the sorted halves

    def merge(self, arr, left, mid, right):
        result = []
        i = left
        j = mid + 1

        # Merge the two halves
        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                result.append(arr[i])
                i += 1
            else:
                result.append(arr[j])
                j += 1

        # Add remaining elements from the left half
        while i <= mid:
            result.append(arr[i])
            i += 1

        # Add remaining elements from the right half
        while j <= right:
            result.append(arr[j])
            j += 1

        # Copy the sorted elements back into the original array
        for k in range(len(result)):
            arr[left + k] = result[k]


# Example usage for testing
arr = [4, 1, 3, 9, 7]
sol = Solution()
sol.mergeSort(arr, 0, len(arr) - 1)
print(" ".join(map(str, arr)))  # Print the sorted array in the correct format
