# Explanation by Tushar Roy:
# https://www.youtube.com/watch?v=LPFhl65R7ww

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}

# Pseudo code below:

## binary search shorter array. (x)
## find partition of x - start + end / 2
## find corresponding partition of y (partition x + partition y = (x + y + 1) / 2 )

## check: is max left x <= min right Y AND is max left Y <= min Right X
## note for edge cases:
## if there are no elements on left side of an array- it's value is -INF
## if there are no elements on right side of an array- it's value is INF

## if max Left X > min Right Y: move x partition left
## if max Left Y > min Right X: move x partition right
## else you have the partition

## for even total elements
## median = avg( max(leftX, leftY ), min(rightX, rightY))
## for odd total elements
## median = max(leftX,leftY)

LARGE_NUM = 2**30
def find_median_sorted_arrays(nums1, nums2)
  return median_of_one_array(nums1) if nums2.empty?
  return median_of_one_array(nums2) if nums1.empty?
  return find_median_sorted_arrays(nums2,nums1) if nums2.length < nums1.length
  x,y = nums1.length, nums2.length
  start,fin = 0, x
  while start <= fin
    partX = (start+fin) / 2
    ## because partX + partY must equal middle of combined arrays:
    partY = (x+y+1)/2 - partX

    partX == 0 ? maxLeftX = -LARGE_NUM : maxLeftX = nums1[partX-1]
    partX == x ? minRightX = LARGE_NUM : minRightX = nums1[partX]

    partY == 0 ? maxLeftY = -LARGE_NUM : maxLeftY = nums2[partY-1]
    partY == y ? minRightY = LARGE_NUM : minRightY = nums2[partY]

    if maxLeftX > minRightY
      fin = partX - 1
    elsif maxLeftY > minRightX
      start = partX + 1
    else
      return [maxLeftX,maxLeftY].max if (x+y).odd?
      return ([maxLeftX,maxLeftY].max + [minRightX,minRightY].min) / 2.0
    end
  end
end

def median_of_one_array(nums)
  mid = nums.length/2
  return nums[mid] if nums.length.odd?
  return (nums[mid-1] + nums[mid]) / 2.0
end

puts find_median_sorted_arrays([5],[1,2,3,4,6])
