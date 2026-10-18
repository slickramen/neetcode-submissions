class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        val sortedS = s.toCharArray().sorted();
        val sortedT = t.toCharArray().sorted();

        return sortedS == sortedT;
    }
}
