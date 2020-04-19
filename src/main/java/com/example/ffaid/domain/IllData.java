package com.example.ffaid.domain;

import java.sql.Time;
import java.sql.Timestamp;

/**
 * @author DIX
 * @version 1.0
 * @description
 * @date 2019/11/29 18:44
 */
public class IllData {

    private Integer id;
    /**
     * 对应的用户
     */
    private Integer userId;
    /**
     * 病史类型
     */
    private String illkind;
    /**
     * 添加病逝的时间
     */
    private Timestamp addtime;
    /**
     * 详情
     */
    private String detail;

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

    public Integer getUserId() {
        return userId;
    }

    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    public String getIllkind() {
        return illkind;
    }

    public void setIllkind(String illkind) {
        this.illkind = illkind;
    }

    public Timestamp getAddtime() {
        return addtime;
    }

    public void setAddtime(Timestamp addtime) {
        this.addtime = addtime;
    }

    public String getDetail() {
        return detail;
    }

    public void setDetail(String detail) {
        this.detail = detail;
    }
}
