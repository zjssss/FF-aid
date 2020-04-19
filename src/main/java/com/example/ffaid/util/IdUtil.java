package com.example.ffaid.util;

import java.security.SecureRandom;

/**
 * @author DIX
 * @version 1.0
 * @description
 * @date 2019/12/9 17:54
 */
public class IdUtil {
    public static String getValue(int length) {
        String pattern = "abcdefghijklmnopqrstuvwxyz" +
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
                "0123456789";
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < length; i++) {
            result.append(pattern.charAt(new SecureRandom().nextInt(pattern.length())));
        }
        return result.toString();
    }
}
