package com.example.ffaid.service;

import com.alibaba.fastjson.JSONObject;
import com.example.ffaid.VO.RelatedDiseases;
import org.neo4j.driver.*;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
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

    public String searchNode(String disease,String data_kind) {
        Driver driver = createDrive();
        JSONObject js1 = new JSONObject();
        String output="";
        String data="n."+data_kind;
        try (Session session = driver.session()) {
            String neoSql = "Match(n:disease{name:'"+disease+"'}) return "+data;
            StatementResult result = session.run(neoSql);
            while (result.hasNext()) {
                Record record = result.next();
//                System.out.println( record.get( "title" ).asString() + " " + record.get( data ).asString() );
                output = record.get( data ).asString();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        if(data_kind.equals("care")&&output.contains("西医治疗"))
        {
            int loc1=output.indexOf("西医治疗");
            String output1=output.substring(loc1-disease.length());
            return output1;
        }
        return output;
    }

    public List<RelatedDiseases> searchNodeList(String disease, String data_kind) {
        List<RelatedDiseases> diseasesList=new ArrayList<RelatedDiseases>();
        Driver driver = createDrive();
        JSONObject js1 = new JSONObject();
        String data="n."+data_kind;
        try (Session session = driver.session()) {
            String neoSql = "Match(n:disease{name:'"+disease+"'}) return "+data;
            StatementResult result = session.run(neoSql);
            while (result.hasNext()) {
                Record record = result.next();
                for(int i=0;i<record.get(data).size();i++)
                {
                    System.out.println(record.get(data).size());
                    String this_disease = record.get( data ).get(i).asString();
                    RelatedDiseases relatedDiseases=new RelatedDiseases();
                    relatedDiseases.setRelatedDisease(this_disease);
                    relatedDiseases.setDiscrib(this.searchNode(this_disease,"description"));
                    diseasesList.add(relatedDiseases);
                }

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return diseasesList;
    }


}

