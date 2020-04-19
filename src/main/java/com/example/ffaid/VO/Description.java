package com.example.ffaid.VO;

import java.io.Serializable;
import java.util.List;

/**
 * @author DIX
 * @date 2020/4/9 17:38
 */
public class Description implements Serializable {
    private List<Symptoms> disease;

    private List<String> symptoms;

    public List<Symptoms> getDisease() {
        return disease;
    }

    public void setDisease(List<Symptoms> disease) {
        this.disease = disease;
    }

    public List<String> getSymptoms() {
        return symptoms;
    }

    public void setSymptoms(List<String> symptoms) {
        this.symptoms = symptoms;
    }
}
