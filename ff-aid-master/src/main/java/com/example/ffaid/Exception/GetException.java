package com.example.ffaid.Exception;

/**
 * @author DIX
 * @date 2020/4/16 15:22
 */
public class GetException extends Exception{

    /**
     * 未定义错误
     */
    public static final Integer ERROR =400;
    /**
     * 格式错误
     */
    public static final Integer FORMAT_ERROR=401;
    /**
     * 资源获取失败错误
     */
    public static final Integer GET_RESOURCE_ERROR=403;
    /**
     * 资源未找到错误
     */
    public static final Integer NOT_FOUND_ERROR=404;

    private int state;

    public GetException(String info,int state)
    {
        super(info);
        this.state=state;
    }
}
