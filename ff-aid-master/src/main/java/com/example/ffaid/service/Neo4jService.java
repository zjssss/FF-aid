package com.example.ffaid.service;

import com.alibaba.fastjson.JSONObject;
import org.neo4j.driver.*;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * @author DIX
 * @date 2020/4/17 15:46
 */
@Service
public class Neo4jService {
    private String uri = "bolt://liublack.cn:7687/";  //neo4j端口
    private String username = "neo4j";    //用户名
    private String password = "200001";   //密码

    public Driver createDrive() {

        return GraphDatabase.driver(uri, AuthTokens.basic(username, password));
    }

    public String searchNode(String disease) {
        Driver driver = createDrive();
        JSONObject js1 = new JSONObject();
        String output="";
        try (Session session = driver.session()) {
            String neoSql = "Match(n:disease{name:'"+disease+"'}) return n.care";
            StatementResult result = session.run(neoSql);
            while (result.hasNext()) {

                Record record = result.next();
                System.out.println( record.get( "title" ).asString() + " " + record.get( "n.care" ).asString() );
                output = record.get( "n.care" ).asString();
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
        return output;
    }


}

