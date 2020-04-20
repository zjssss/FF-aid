package com.example.ffaid.controller;

import com.alibaba.fastjson.JSONObject;
import com.example.ffaid.service.Neo4jService;
import io.swagger.annotations.Api;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/**
 * @author DIX
 * @date 2020/4/17 15:51
 */
@Api(value="连接Neo4J数据库controller",tags={"Neo4J数据访问操作接口"})
@RestController
@CrossOrigin
@RequestMapping(value = "/neo")
public class Neo4jController {
    @Autowired
    private Neo4jService neo4jService;
    @GetMapping(value = "/aidCare")
    public Object searchNode(@RequestParam("disease") String disease)throws Exception{

        return ResponseEntity.ok(neo4jService.searchNode(disease));
    }

    @GetMapping(value="/aidCare/L1")
    public Object searchNodeL1(@RequestParam("disease") String disease)throws Exception{

        disease=disease.substring(0,disease.length()-1);
        return ResponseEntity.ok(neo4jService.searchNode(disease));
    }

}
