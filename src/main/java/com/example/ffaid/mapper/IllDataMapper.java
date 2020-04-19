package com.example.ffaid.mapper;

import com.example.ffaid.domain.IllData;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @author DIX
 * @date 2019/12/9 11:49
 */
@Mapper
@Repository
public interface IllDataMapper {

    /**
     * 查看一个用户的所有病史
     * @param userId
     * @return
     */
    List<IllData> findUserIllData(Integer userId);

    /**
     * 查看一个病逝信息
     * @param id
     * @return
     */
    IllData findIllData(Integer id);

    /**
     * 新建病史
     * @param illData
     * @return
     */
    int createIllData(IllData illData);

    /**
     * 修改病史
     * @param illData
     * @return
     */
    int updateIllData(IllData illData);

    /**
     * 删除病史
     * @param id
     * @return
     */
    int deleteIllData(Integer id);
}
