package com.example.ffaid.dao;

import com.example.ffaid.domain.User;
import com.example.ffaid.mapper.UserMapper;
import org.apache.ibatis.annotations.Param;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.data.redis.core.RedisTemplate;
import redis.clients.jedis.Jedis;

import java.io.Serializable;
import java.util.logging.Logger;

/**
 * @author DIX
 * @date 2019/11/29 19:48
 */
@Repository
public class UserDao {
    @Autowired
    private UserMapper userMapper;

    @Autowired
    private RedisTemplate redisTemplate;

    /**
     * 登录
     */
    public User userLogin(String username, String password) {
        return userMapper.userLogin(username, password);
    }

    /**
     * 注册
     */
    public int userRegister(User user) {
        return userMapper.userRegister(user);
    }

    public int update(User user) {
        return userMapper.update(user);
    }

    public int logicalDelete(Integer id) {
        return userMapper.logicalDelete(id);
    }

    public User getUser(Integer id) {
//        long startTime=System.currentTimeMillis();
//        String key = "U_" + id;
//        User user = (User) redisTemplate.opsForValue().get(key);
//        if (user == null) {
//            user = userMapper.getUser(id);
//            redisTemplate.opsForValue().set(key, user);
//        }
//        long endTime=System.currentTimeMillis();
//        System.out.println(key);
//        System.out.println(endTime-startTime);
        return userMapper.getUser(id);
    }

    public User getUserByTel(String tel)
    {
        return userMapper.getUserByTel(tel);
    }

//    public User getUser(Integer id)
//    {
//        Jedis jedis=new Jedis("121.199.2.219",6379);
//        String key="U_"+id;
//        User user=(User)
//    }
}
