package com.example.ffaid.controller;

import com.example.ffaid.domain.UrgentTel;
import com.example.ffaid.service.UrgentTelService;
import io.swagger.annotations.Api;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author DIX
 * @date 2019/12/9 17:17
 */
@Api(value="紧急联系人controller",tags={"紧急联系人操作接口"})
@CrossOrigin
@RestController
public class UrgentTelController {

    @Autowired
    private UrgentTelService urgentTelService;



    @GetMapping("/urgentTel/{id}")
    public UrgentTel findTel(@PathVariable("id") Integer id) {
        return urgentTelService.findTel(id);
    }

    @GetMapping("/users/{id}/urgentTel")
    public List<UrgentTel> findUserTel(@PathVariable("id") Integer userId) {
        return urgentTelService.findUserTel(userId);
    }

    @PutMapping("/urgentTel/{id}")
    public int updateTel(@PathVariable("id") Integer id, UrgentTel urgentTel)
    {
        urgentTel.setId(id);
        return urgentTelService.updateTel(urgentTel);
    }

    @PostMapping("/urgentTel")
    public int createTel(UrgentTel urgentTel)
    {
        return urgentTelService.createTel(urgentTel);
    }

    @DeleteMapping("/urgentTel/{id}")
    public int deleteTel(@PathVariable("id") Integer id)
    {
        return urgentTelService.deleteTel(id);
    }
}
