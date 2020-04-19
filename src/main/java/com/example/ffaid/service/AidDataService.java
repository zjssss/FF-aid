package com.example.ffaid.service;

import com.example.ffaid.domain.AidData;
import com.example.ffaid.mapper.AidDataMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author DIX
 * @date 2019/12/14 14:15
 */
@Service
public class AidDataService {

    @Autowired
    private AidDataMapper aidDataMapper;

    public int createAidData(AidData aidData){return aidDataMapper.createAidData(aidData);}

    public List<AidData> getNewAidData(){return aidDataMapper.getNewAidData();}

    public int endAidData(Integer id){return aidDataMapper.endAidData(id);}
}
