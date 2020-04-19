package com.example.ffaid.controller;

import com.example.ffaid.domain.IllData;
import com.example.ffaid.service.IllDataService;
import io.swagger.annotations.Api;
import org.omg.CORBA.OBJ_ADAPTER;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/**
 * @author DIX
 * @date 2019/12/9 12:13
 */
@Api(value="既往病史controller",tags={"既往病史操作接口"})
@RestController
@CrossOrigin
public class IllDataController {
    @Autowired
    private IllDataService illDataService;

    @GetMapping("/user/{id}/illData")
    public Object findUserIllData(@PathVariable("id") Integer id)
    {
        return ResponseEntity.ok(illDataService.findUserIllData(id));
    }

    @GetMapping("/illData/{id}")
    public Object findIllData(@PathVariable("id") Integer id)
    {
        return ResponseEntity.ok(illDataService.findIllData(id));
    }

    @PostMapping("/illData")
    public Object createIllData(IllData illData)
    {
        return ResponseEntity.ok(illDataService.createIllData(illData));
    }

    @PutMapping("/illData/{id}")
    public Object updataIllData(@PathVariable("id") Integer id,IllData illData)
    {
        illData.setId(id);
        return ResponseEntity.ok(illDataService.updateIllData(illData));
    }

    @DeleteMapping("/illData/{id}")
    public Object deleteIllData(@PathVariable("id") Integer id)
    {
        return ResponseEntity.ok(illDataService.deleteIllData(id));
    }
}
