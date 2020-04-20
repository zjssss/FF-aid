package com.example.ffaid.service;

import com.example.ffaid.domain.IllData;
import com.example.ffaid.mapper.IllDataMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.swing.*;
import java.util.List;

/**
 * @author DIX
 * @date 2019/12/9 11:57
 */
@Service
public class IllDataService {

    @Autowired
    private IllDataMapper illDataMapper;

    public IllData findIllData(Integer id){return illDataMapper.findIllData(id);}

    public List<IllData> findUserIllData(Integer userId){return  illDataMapper.findUserIllData(userId);}

    public int createIllData(IllData illData){return illDataMapper.createIllData(illData);}

    public int updateIllData(IllData illData){return illDataMapper.updateIllData(illData);}

    public int deleteIllData(Integer id){return illDataMapper.deleteIllData(id);}
}