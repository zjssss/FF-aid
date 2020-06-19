package com.example.ffaid.service;

import com.example.ffaid.VO.Description;
import com.example.ffaid.VO.Output;
import com.example.ffaid.VO.Result;
import com.example.ffaid.VO.TelResult;
import com.example.ffaid.dao.UserDao;
import com.example.ffaid.domain.IllData;
import com.example.ffaid.domain.UrgentTel;
import com.example.ffaid.domain.User;
import com.example.ffaid.faceapi.FaceAdd;
import com.example.ffaid.faceapi.FaceIdentify;
import com.example.ffaid.speechapi.AsrMain;
import com.example.ffaid.speechapi.common.DemoException;
import com.example.ffaid.util.AdviceUtil;
import com.example.ffaid.util.FileUpLoadUtil;
import com.example.ffaid.util.GsonUtils;
import com.example.ffaid.util.IdUtil;
import org.omg.CORBA.PUBLIC_MEMBER;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

/**
 * @author DIX
 * @date 2019/11/29 19:57
 */
@Service
public class UserService {
    @Autowired
    UserDao userDao;

    @Autowired
    UrgentTelService urgentTelService;

    @Autowired
    IllDataService illDataService;

    AdviceUtil adviceUtil=new AdviceUtil();

    /**
     * 标识上传服务器或是在本地调试
     */
    private static boolean up_server=true;

    public static String UPLOAD_PATH="/root/imag/picStore/";

    public static String CHECK_PATH="/root/imag/picCheck/";

    public static String LOCAL_PATH="C:\\Users\\Administrator\\Desktop\\下\\ImageData\\";

    public static String LOCAL_CHECK_PATH="C:\\Users\\Administrator\\Desktop\\下\\ImageData\\check\\";

    public String handleUploadPicture(MultipartFile file) {
        String ranName = IdUtil.getValue(8)
                + file.getOriginalFilename();

        /**
         * 判断是否在服务器上运行，若在本地调试使用本地的路径
         */
        String path = up_server?UPLOAD_PATH+ranName:LOCAL_PATH+ ranName;

        String ok = "Success";
        if (ok.equals(FileUpLoadUtil.upload(file, path))) {
            return ranName;
        }
        return null;
    }

    public String handleUploadPictureCheck(MultipartFile file) {
        String ranName1 = IdUtil.getValue(8)
                + file.getOriginalFilename();

        String path = up_server?CHECK_PATH+ranName1:LOCAL_CHECK_PATH + ranName1;

        System.out.println(path);
        String ok;ok = "Success";
        if (ok.equals(FileUpLoadUtil.upload(file, path))) {
            return path;
        }
        return null;
    }


    public Object speechIdentify(MultipartFile file) throws IOException, DemoException {
        String speechPath=handleUploadPictureCheck(file);
        AsrMain asrMain=new AsrMain();
        String result=asrMain.runFile(speechPath);
        int loc1=result.indexOf("result");
        int loc2=result.indexOf("\"",loc1+10);
        String result1=result.substring(loc1+10,loc2);
        return result1;
    }

    public Object WordIdentify(String word) throws IOException, DemoException {
        String result="";
        String[] arguments = new String[]{up_server?"python3":"pythona", up_server?"/root/py/bayesBasedModel.py":"C:\\Users\\Administrator\\Desktop\\下\\OPPO\\v2\\bayesBasedModel.py", word};
//        String[] arguments = new String[]{"python", "/root/py/bayesBasedModel.py", word};
        try {
            Process process = Runtime.getRuntime().exec(arguments);
            BufferedReader in  = new BufferedReader(new InputStreamReader(process.getInputStream(),up_server?"utf-8":"GBK"));
//            BufferedReader in  = new BufferedReader(new InputStreamReader(process.getInputStream(),"utf-8"));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
                result=result+line;
            }
            in.close();
            int re = process.waitFor();
            System.out.println(re);
        } catch (Exception e) {
            e.printStackTrace();
        }
        Description resultObj= GsonUtils.fromJson(result,Description.class);
        String[] s=new String[9];
        Output output=new Output();
        for(int i=0;i<3;i++)
        {
            if(resultObj.getDisease().size()>i)
            {
                s[i]=resultObj.getDisease().get(i).getName();
            }

        }
        for(int i=3;i<9;i++)
        {
            if(resultObj.getSymptoms().get(i-3)!=null)
            {
                s[i]=resultObj.getSymptoms().get(i-3);
            }

        }
        output.setAid1(s[0]);
        output.setAid2(s[1]);
        output.setAid3(s[2]);
        output.setS1(s[3]);
        output.setS2(s[4]);
        output.setS3(s[5]);
        output.setS4(s[6]);
        output.setS5(s[7]);
        output.setS6(s[8]);
        return output;
    }

    public Object searchFace(MultipartFile file) {
        TelResult telResult = new TelResult();
        String picPath = handleUploadPictureCheck(file);
        System.out.println(picPath);
        Result result = FaceIdentify.identify(picPath);

        int userId = result.getUserId();
        System.out.println(userId);
        if (result.getScore() > 80.0) {
            List<UrgentTel> tels = urgentTelService.findUserTel(userId);
            if (tels.size() >= 1) {
                telResult.setTel1(tels.get(0).getUrgentTel());
            }
            if (tels.size() >= 2) {
                telResult.setTel2(tels.get(1).getUrgentTel());
            }
            if (tels.size() >= 3) {
                telResult.setTel3(tels.get(2).getUrgentTel());
            }
            List<IllData> illDataList=illDataService.findUserIllData(userId);
            if(illDataList.size()>0)
            {
                telResult.setMedicine(illDataList.get(0).getMedicine());
                telResult.setCare(illDataList.get(0).getDetail());
            }
            return telResult;
        } else {
            return "not found";
        }
    }

    public Object speechIdentifyDoc(MultipartFile file) throws IOException, DemoException {
        String speechPath=handleUploadPictureCheck(file);
        AsrMain asrMain=new AsrMain();
        String result=asrMain.runFile(speechPath);
        String result2="";
        int loc1=result.indexOf("result");
        int loc2=result.indexOf("\"",loc1+10);
        String result1=result.substring(loc1+10,loc2);
        String[] arguments = new String[]{up_server?"python3":"pythona", up_server?"/root/py/bayesBasedModel.py":"C:\\Users\\Administrator\\Desktop\\下\\OPPO\\v2\\bayesBasedModel.py", result1};
        try {
            Process process = Runtime.getRuntime().exec(arguments);
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream(),up_server?"utf-8":"GBK"));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
                result2=result2+line;
            }
            in.close();
            //java代码中的process.waitFor()返回值为0表示我们调用python脚本成功，
            //返回值为1表示调用python脚本失败，这和我们通常意义上见到的0与1定义正好相反
            int re1 = process.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result2;
    }

    public Object epidemicTest(String describe) throws IOException, DemoException {
        double rate=0;
        System.out.println(describe);
        String result="";
                String[] arguments = new String[] {up_server?"python3":"pythona", up_server?"/root/py/specialDiseaseDiagnosis.py":"C:\\Users\\Administrator\\Desktop\\下\\OPPO\\v2\\specialDiseaseDiagnosis.py",describe};
        try {
            Process process = Runtime.getRuntime().exec(arguments);
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream(),up_server?"utf-8":"GBK"));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
                result=result+line;
            }
            System.out.println(result);
            rate=Double.valueOf(result);
            in.close();
            int re1 = process.waitFor();
            System.out.println(re1);
        } catch (Exception e) {
            e.printStackTrace();
        }
        if(rate==0)
        {
            rate=30;
        }
        return rate;
    }

    public int userFaceRegister(MultipartFile file,String tel)
    {
        String ranName=handleUploadPicture(file);
        User user1 =getUserByTel(tel);
        System.out.println(user1.getUsername());
        user1.setPic(ranName);
        FaceAdd.add(user1.getId(),ranName);
        return userDao.update(user1);
    }

    public User userLogin(String username, String password) {
        return userDao.userLogin(username, password);
    }

    public int userRegister(User user) {
        return userDao.userRegister(user);
    }

    public int update(User user) {
        return userDao.update(user);
    }

    public int logicalDelete(Integer id) {
        return userDao.logicalDelete(id);
    }

    public User getUser(Integer id) {
        return userDao.getUser(id);
    }

    public User getUserByTel(String tel) {
        return userDao.getUserByTel(tel);
    }
}
