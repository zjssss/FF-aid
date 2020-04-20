package com.example.ffaid.service;

import com.example.ffaid.domain.UrgentTel;
import com.example.ffaid.mapper.UrgentTelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author DIX
 * @date 2019/12/9 16:47
 */
@Service
public class UrgentTelService {

    @Autowired
    UrgentTelMapper urgentTelMapper;

    public List<UrgentTel> findUserTel(Integer userId)
    {
        return urgentTelMapper.findUserTel(userId);
    }

    public UrgentTel findTel(Integer id)
    {
        return urgentTelMapper.findTel(id);
    }

    public int updateTel(UrgentTel urgentTel)
    {
        return urgentTelMapper.updateTel(urgentTel);
    }

    public int createTel(UrgentTel urgentTel)
    {
        return urgentTelMapper.createTel(urgentTel);
    }

    public int deleteTel(Integer id)
    {
        return urgentTelMapper.deleteTel(id);
    }
}
