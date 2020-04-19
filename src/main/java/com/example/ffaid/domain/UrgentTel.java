package com.example.ffaid.domain;

import java.sql.Timestamp;

/**
 * @author DIX
 * @version 1.0
 * @description
 * @date 2019/11/29 18:47
 */
public class UrgentTel {

    private Integer id;
    /**
     * 对应的用户
     */
    private Integer userId;
    /**
     * 该用户的一个紧急联系人电话
     */
    private String urgentTel;
    /**
     * 对该联系人的描述
     */
    private String describ;
    /**
     * 添加时间
     */
    private Timestamp addtime;

    private Integer deleted;

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

    public String getUrgentTel() {
        return urgentTel;
    }

    public void setUrgentTel(String urgentTel) {
        this.urgentTel = urgentTel;
    }

    public String getDescrib() {
        return describ;
    }

    public void setDescrib(String describ) {
        this.describ = describ;
    }

    public Timestamp getAddtime() {
        return addtime;
    }

    public void setAddtime(Timestamp addtime) {
        this.addtime = addtime;
    }

    public Integer getDeleted() {
        return deleted;
    }

    public void setDeleted(Integer deleted) {
        this.deleted = deleted;
    }
}
