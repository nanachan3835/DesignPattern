"""
    _summary_ : Sắp xếp mảng bằng phương pháp merge sort
    Input:
        - arr: Mảng cần sắp xếp
        - left: Vị trí bắt đầu của mảng cần sắp xếp
        - right: Vị trí kết thúc của mảng cần sắp xếp
    Output:
        - Mảng đã sắp xếp 
        - list 
    
    _description_:
    - Hàm merge_sort sử dụng phương pháp đệ quy để sắp xếp mảng arr
    - Hàm merge sử dụng để gộp hai mảng đã sắp xếp thành một mảng
    - Độ phức tạp thời gian: O(nlogn) với n là số phần tử của mảng arr
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Tách mảng thành hai phần bằng nhau
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Đệ quy gọi hàm merge_sort cho từng nửa mảng
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Gộp hai mảng đã sắp xếp thành một mảng
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        # So sánh phần tử hiện tại của hai mảng
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Gắn thêm các phần tử còn lại của mảng trái (nếu có)
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # Gắn thêm các phần tử còn lại của mảng phải (nếu có)
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result