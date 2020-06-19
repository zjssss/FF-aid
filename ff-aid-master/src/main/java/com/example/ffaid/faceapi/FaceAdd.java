package com.example.ffaid.faceapi;


import com.example.ffaid.util.*;

import java.net.URLEncoder;

/**
 * @author DIX
 * @date 2020/3/3 9:20
 * 人脸注册
 */
public class FaceAdd {

    public static String add(Integer id,String fileName) {
        // 请求url
        String url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add";

        String uid=""+id;
        String userInfo="{'username:弟弟6'}";
        String groupId="u_g_1";
        String faceImage="/root/imag/picStore/"+fileName;
        try {

            byte[] imgData=FileUtil.readFileByBytes(faceImage);
            String imgStr1=Base64Util.encode(imgData);

            String param="user_id="+uid+"&image_type=BASE64"+"&userInfo="+userInfo+"&group_id="+groupId+"&"+ URLEncoder.encode("image","UTF-8")+"="+URLEncoder.encode(imgStr1,"UTF-8");

            // 注意这里仅为了简化编码每一次请求都去获取access_token，线上环境access_token有过期时间， 客户端可自行缓存，过期后重新获取。
            String accessToken = "24.22992ca6894d3cf5949478ca25f02bff.2592000.1593675540.282335-18646513";

            String result = HttpUtil.post(url, accessToken, "application/json", param);
            System.out.println(result);
            return result;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

//    public static void main(String[] args) {
//        FaceAdd.add();
//    }
}