package com.example.ffaid.controller;

import com.example.ffaid.domain.AidData;
import com.example.ffaid.service.AidDataService;
import io.swagger.annotations.Api;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author DIX
 * @date 2019/12/14 14:21
 */
@Api(value="求救信息controller",tags={"求救信息操作接口"})
@CrossOrigin
@RestController
public class AidDataController {

    @Autowired
    AidDataService aidDataService;

    @PostMapping("/aidData")
    public Object createAidData(AidData aidData){return ResponseEntity.ok(aidDataService.createAidData(aidData));}

    @PostMapping("/aidDatas")
    public Object createAidDatas(@RequestParam("byId") Integer byId,@RequestParam("location") String location,@RequestParam("details") String details,@RequestParam("isSelf") Integer isSelf)
    {
        AidData aidData1=new AidData();
        aidData1.setById(byId);
        aidData1.setDetails(details);
        aidData1.setIsSelf(isSelf);
        aidData1.setLocation(location);
        return ResponseEntity.ok(aidDataService.createAidData(aidData1));
    }

    @GetMapping("/aidData")
    public List<AidData> getNewAidData(){return aidDataService.getNewAidData();}

    @PostMapping("/aidData/{id}")
    public Object endAidData(@PathVariable("id") Integer id){return ResponseEntity.ok(aidDataService.endAidData(id));}
}
