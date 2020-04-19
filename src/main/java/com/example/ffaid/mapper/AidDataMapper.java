package com.example.ffaid.mapper;

import com.example.ffaid.domain.AidData;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @author DIX
 * @date 2019/12/14 13:52
 */
@Mapper
@Repository
public interface AidDataMapper {

    /**
     * 创建一条消息
     * @param aidData
     * @return
     */
    int createAidData(AidData aidData);

    /**
     * 获得新的信息
     * @return
     */
    List<AidData> getNewAidData();

    /**
     * 消息结束
     * @return
     */
    int endAidData(Integer id);


}
