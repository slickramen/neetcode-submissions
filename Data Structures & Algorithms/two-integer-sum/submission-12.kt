class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val inv = HashMap<Int, Int>()

        for ((index, num) in nums.withIndex()) {
            if (num in inv) {
                return intArrayOf(inv.getValue(num), index);
            }

            inv[target-num] = index;
        }    

        return intArrayOf();
    }
}
