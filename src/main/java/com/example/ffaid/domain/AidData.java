package com.example.ffaid.domain;

import java.sql.Timestamp;

/**
 * @author DIX
 * @version 1.0
 * @description
 * @date 2019/11/28 22:26
 */

public class AidData {

    private Integer id;
    /**
     * 求救者
     */
    private Integer byId;

    /**
     * 求救发出时间
     */
    private Timestamp createTime;
    /**
     * 地址
     */
    private String location;
    /**
     * 详情
     */
    private String details;
    /**
     * 是否结束（被处理）
     */
    private int isEnd;
    /**
     * 是不是自我求救 0不是 1是
     */
    private int isSelf;
    /**
     * 结束时间
     */
    private Timestamp endTime;

    private Integer deleted;

    public Integer getDeleted() {
        return deleted;
    }

    public void setDeleted(Integer deleted) {
        this.deleted = deleted;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }


    public Integer getById() {
        return byId;
    }

    public void setById(Integer byId) {
        this.byId = byId;
    }

    public Timestamp getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Timestamp createTime) {
        this.createTime = createTime;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }

    public int getIsEnd() {
        return isEnd;
    }

    public void setIsEnd(int isEnd) {
        this.isEnd = isEnd;
    }

    public int getIsSelf() {
        return isSelf;
    }

    public void setIsSelf(int isSelf) {
        this.isSelf = isSelf;
    }

    public Timestamp getEndTime() {
        return endTime;
    }

    public void setEndTime(Timestamp endTime) {
        this.endTime = endTime;
    }
}