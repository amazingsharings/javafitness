/*
    problem: ZigZag Conversion
    author: everpuck
    date: 02/13/2019
*/
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        StringBuffer[] retArray = new StringBuffer[numRows];
        for (int i = 0; i < numRows; ++i) {
            retArray[i] = new StringBuffer("");
        }

        int curRow = 0;
        boolean goingDown = false;
        for (int i = 0; i < s.length(); ++i) {
            retArray[curRow].append(s.charAt(i));
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }
            curRow += goingDown ? 1:-1;
        }
        String retString = "";
        for (int i = 0; i < numRows; ++i) {
            retString += retArray[i].toString();
        }
        return retString;
    }

    // StringBuilder is faster
    public String convert2(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        StringBuilder[] retArray = new StringBuilder[numRows];
        for (int i = 0; i < numRows; ++i) {
            retArray[i] = new StringBuilder("");
        }

        int curRow = 0;
        boolean goingDown = false;
        for (int i = 0; i < s.length(); ++i) {
            retArray[curRow].append(s.charAt(i));
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }
            curRow += goingDown ? 1:-1;
        }
        String retString = "";
        for (int i = 0; i < numRows; ++i) {
            retString += retArray[i].toString();
        }
        return retString;
    }
}


public class ZigZagConversion {
    public static void main(String[] args) {
        String retString = "";
        String s = new String("AB");
        int numRows = 1;
        Solution solution = new Solution();
        // retString = solution.convert(s, numRows);
        retString = solution.convert2(s, numRows);
        System.out.println(retString);
    }
}