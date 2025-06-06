class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # n = len(arr)

        # pre_comp = sum(arr)


        # for window_size in range(2, n+1):

        #     for i in range(n - window_size + 1):
        #         store = sorted(arr[i : i + window_size])
        #         pre_comp += store[0]

        # return pre_comp%(pow(10,9) + 7)
        
        
        stack = []
        sub_sum = 0
        for i in range(len(arr) + 1):

            curr_val = arr[i] if i < len(arr) else 0

            while stack and arr[stack[-1]] > curr_val:
                mid = stack.pop()
                mid_val = arr[mid]

                left_bound = stack[-1] if stack else -1

                right_bound = i

                num_of_times = (mid - left_bound) * (right_bound - mid)
                sub_sum += num_of_times*mid_val

            stack.append(i)

        # print(stack)
        # print(sub_sum)
        return sub_sum % (pow(10,9) + 7)
        
