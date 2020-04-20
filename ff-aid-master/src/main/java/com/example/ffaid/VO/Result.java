package com.example.ffaid.VO;

/**
 * @author DIX
 * @date 2020/3/26 0:13
 */
public class Result {
    private String group_id;

    private int userId;

    private double score;

    public String getGroup_id() {
        return group_id;
    }

    public void setGroup_id(String group_id) {
        this.group_id = group_id;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }
}
