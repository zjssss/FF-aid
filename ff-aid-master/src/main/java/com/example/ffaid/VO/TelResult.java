package com.example.ffaid.VO;

import java.io.Serializable;

/**
 * @author DIX
 * @date 2020/4/13 17:21
 */
public class TelResult implements Serializable {
    private String Tel1;
    private String Tel2;
    private String Tel3;

    public String getTel1() {
        return Tel1;
    }

    public void setTel1(String tel1) {
        Tel1 = tel1;
    }

    public String getTel2() {
        return Tel2;
    }

    public void setTel2(String tel2) {
        Tel2 = tel2;
    }

    public String getTel3() {
        return Tel3;
    }

    public void setTel3(String tel3) {
        Tel3 = tel3;
    }
}
