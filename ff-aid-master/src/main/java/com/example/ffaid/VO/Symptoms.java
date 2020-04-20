package com.example.ffaid.VO;

import com.google.gson.Gson;

import java.io.Serializable;
import java.util.List;

/**
 * @author DIX
 * @date 2020/4/9 17:02
 */
public class Symptoms implements Serializable {
    private String name;

    private String care;

    private String complication;

    private String department;

    private String description;

    private String examination;

    private String otherName;

    public List<String> getRelatedDisease() {
        return relatedDisease;
    }

    public void setRelatedDisease(List<String> relatedDisease) {
        this.relatedDisease = relatedDisease;
    }

    private List<String> relatedDisease;

    private String position;

    private String prevention;

    private String reason;

    private String symptom;

    private String treatment;

    private String typicalSymptom;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCare() {
        return care;
    }

    public void setCare(String care) {
        this.care = care;
    }

    public String getComplication() {
        return complication;
    }

    public void setComplication(String complication) {
        this.complication = complication;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getExamination() {
        return examination;
    }

    public void setExamination(String examination) {
        this.examination = examination;
    }

    public String getOtherName() {
        return otherName;
    }

    public void setOtherName(String otherName) {
        this.otherName = otherName;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public String getPrevention() {
        return prevention;
    }

    public void setPrevention(String prevention) {
        this.prevention = prevention;
    }

    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }


    public String getSymptom() {
        return symptom;
    }

    public void setSymptom(String symptom) {
        this.symptom = symptom;
    }

    public String getTreatment() {
        return treatment;
    }

    public void setTreatment(String treatment) {
        this.treatment = treatment;
    }

    public String getTypicalSymptom() {
        return typicalSymptom;
    }

    public void setTypicalSymptom(String typicalSymptom) {
        this.typicalSymptom = typicalSymptom;
    }

}
