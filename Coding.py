class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_rect = 0
        for h in range(len(heights)):
            if len(stack) == 0:
                stack.append(h)
            elif heights[stack[-1]] <= heights[h]:
                stack.append(h)
            else:
                print("stack in the while:  ", stack)
                while(len(stack) > 0):
                    if heights[stack[-1]] > heights[h]:
                        stack_top = stack.pop()
                        if len(stack) > 0:
                            window_size = h - 1 - stack[-1]
                        else:
                            window_size = h
                            print("window_size:  ", window_size)

                        rect_size = window_size * heights[stack_top]
                        max_rect = max(max_rect, rect_size)
                        print("max_rect ", max_rect)
                    else:
                        break
                stack.append(h)
        for idx in range(len(stack)):
            if idx == 0:
                rect_size = heights[stack[idx]] * (stack[-1] + 1)
                print("rect_size ", rect_size)
            else:
                rect_size = heights[stack[idx]] * (stack[-1] - stack[idx-1])
            max_rect = max(max_rect, rect_size)
            print("max_rect2 ", max_rect)

        return max_rect

# heights = [4,2]
# heights = [2,1,5,6,2,3]
heights = [2,4]
# heights = [2,1,5,6,2,3]

Sol = Solution()
print(Sol.largestRectangleArea(heights))