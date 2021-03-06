package com.example.ffaid.util;

import com.example.ffaid.VO.AdviceHelp;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author DIX
 * @date 2020/4/22 17:41
 */
public class AdviceUtil {
    public AdviceHelp bet0___20=new AdviceHelp();

    public AdviceHelp bet20___40=new AdviceHelp();

    public AdviceHelp bet40___60=new AdviceHelp();

    public AdviceHelp bet60___100=new AdviceHelp();

    public String bet0_20="您患新型冠状病毒的概率较低!"+"新冠手册-居家日常预防\n" +
            "\n" +
            "1. 尽量避免出门，如需外出佩戴口罩；\n" +
            "2. 减少到人员密集的公共场所活动，尤其是空气流动性差的地方；\n" +
            "3. 不要接触、购买和食用野生动物（即野味），避免前往售卖活体动物（禽类、海产品、野生动物等）的市场，禽肉蛋要充分煮熟后食用；\n" +
            "4. 居室保持清洁，勤开窗，经常通风；\n" +
            "5. 随时保持手卫生。外出归家、触摸公共场所物品、饭前便后，用洗手液或香皂流水洗手，或者使用含酒精成分的免洗洗手液；";

    public List<String> bet0__20=Arrays.asList(bet0_20.split("!"));


    public String bet20_40="您患新型冠状病毒的概率略高，有一定风险!"+"新冠手册-居家日常建议\n" +
            "\n" +
            "1. 保持良好卫生和健康习惯。家庭成员不共用毛巾，保持家居、餐具清洁，勤晒衣被。不随地吐痰，口鼻分泌物用纸巾包好，弃置于有盖垃圾箱内。注意营养，勤运动；\n" +
            "2. 主动做好个人及家庭成员的健康监测。自觉发热时要主动测量体温，家中有小孩的，要早晚摸小孩的额头，如有发热要为其测量体温；\n" +
            "3. 准备常用物资。家庭备置体温计、一次性口罩、家庭用的消毒用品等物资。";

    public List<String> bet20__40=Arrays.asList(bet20_40.split("!"));

    public String bet40_60="您患新型冠状病毒的概率较高，请及时就医检测!"+"新冠手册-居家日常建议\n" +
            "\n" +
            "1. 对接触过的办公桌椅、使用的办公用品等一天2次擦拭消毒；\n" +
            "2. 多人办公时佩戴口罩，人与人之间保持1米以上距离；\n" +
            "3. 不在公共区域逗留、闲谈，工作也尽可能通过电话、微信、邮件等形式沟通；\n" +
            "4. 保持勤洗手、多饮水，使用有盖子的水杯；\n" +
            "5. 接待外来人员时双方佩戴口罩且保持1米以上距离，控制谈话时间。";

    public List<String> bet40__60=Arrays.asList(bet40_60.split("!"));

    public String bet60_100="您患新型冠状病毒的概率极高，为了您和您家人的健康，请立马就医检测。!"+"新冠手册-患病检测指导\n" +
            "\n" +
            "对于新型冠状病毒治疗方法，就是进行隔离治疗和对症治疗，现在还没有特效药物，对于病情较为轻微的患者，可以进行一般治疗，适当休息，通过静脉补充水分以及营养，同时监测身体的各项指标，根据每个患者的身体具体情况进行针对性治疗。";

    public List<String> bet60__100=Arrays.asList(bet60_100.split("!"));

    public AdviceHelp advice(Double rate) {
        bet0___20.setAdvice(bet0__20.get(1));
        bet0___20.setRateHelp(bet0__20.get(0));
        bet20___40.setAdvice(bet20__40.get(1));
        bet20___40.setRateHelp(bet20__40.get(0));
        bet40___60.setAdvice(bet40__60.get(1));
        bet40___60.setRateHelp(bet40__60.get(0));
        bet60___100.setAdvice(bet60__100.get(1));
        bet60___100.setRateHelp(bet60__100.get(0));
        if (rate > 0 && rate < 20) {
            return bet0___20;
        }
        if ((rate >= 20 && rate < 40) || rate==0 || rate==100) {
            return bet20___40;
        }
        if (rate >= 40 && rate < 60) {
            return bet40___60;
        }
        if (rate >= 60) {
            return bet60___100;
        }
        return null;
    }


}
