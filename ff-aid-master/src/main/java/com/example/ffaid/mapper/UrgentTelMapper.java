package com.example.ffaid.mapper;

import com.example.ffaid.domain.UrgentTel;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @author DIX
 * @date 2019/12/9 14:54
 */
@Mapper
@Repository
public interface UrgentTelMapper {

    /**
     * 查看单个紧急联系人信息
     * @param id
     * @return
     */
    UrgentTel findTel(Integer id);

    /**
     * 查看一个人的紧急联系人列表
     * @param userId
     * @return
     */
    List<UrgentTel> findUserTel(Integer userId);

    /**
     * 新建一条紧急联系人记录
     * @param urgentTel
     * @return
     */
    int createTel(UrgentTel urgentTel);

    /**
     * 更新紧急联系人信息
     * @param urgentTel
     * @return
     */
    int updateTel(UrgentTel urgentTel);

    /**
     * 删除一个紧急联系人
     * @param id
     * @return
     */
    int deleteTel(Integer id);
}
