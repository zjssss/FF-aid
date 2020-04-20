package com.example.ffaid.domain;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.sql.Date;
import java.util.List;
import java.util.Objects;

public class User implements Serializable {

    private Integer id;
    /**
     * 密码
     */
    private String password;

    /**
     * 名字
     */
    private String username;
    /**
     * 性别 0 男 1 女
     */
    private Integer sex;
    /**
     * status 在线与否 0 不在线 1 在线
     */
    private Integer status;
    /**
     * 电话
     */
    private String tel;
    /**
     * 人脸图片
     */
    private String pic;
    /**
     * 生日
     */
    private Date birthday;

    /**
     * 是否删除
     */
    private Integer deleted;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


    public Integer getSex() {
        return sex;
    }

    public void setSex(Integer sex) {
        this.sex = sex;
    }

    public Integer getStatus() {
        return status;
    }

    public void setStatus(Integer status) {
        this.status = status;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getPic() {
        return pic;
    }

    public void setPic(String pic) {
        this.pic = pic;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public Integer getDeleted() {
        return deleted;
    }

    public void setDeleted(Integer deleted) {
        this.deleted = deleted;
    }
}