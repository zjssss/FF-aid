package com.example.ffaid.mapper;

import com.example.ffaid.domain.User;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * @author DIX
 * @date 2019/11/29 19:43
 */
@Mapper
@Repository
public interface UserMapper {

    /**
     * @param username
     * @param password
     * @return
     */
    User userLogin(String username, String password);

    /**
     * 添加新用户
     *
     * @param user
     * @return
     */
    int userRegister(User user);

    /**
     * 根据不同的条目修改用户信息
     *
     * @param user
     * @return
     */
    int update(User user);
    //@Param("user")

    /**
     * 逻辑删除
     * @param id
     * @return
     */
    int logicalDelete(Integer id);

    /**
     * 得到单个用户的信息
     * @param id
     * @return
     */
    User getUser(Integer id);

    /**
     * 通过电话得到单个用户的信息
     * @param tel
     * @return
     */
    User getUserByTel(String tel);
}
