# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

start_app("com.thinkhome.v3")
sleep(5)

# #登录181*** 
# poco("android:id/tabs").child("android.widget.RelativeLayout")[0].click()
# poco(text="联动").click()
# 
# #添加联动
# #联动名称为空
# poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
# poco("com.thinkhome.v3:id/et_name").set_text("")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "名称不能为空", "添加联动名称为空验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     
# #联动条件为空
# poco("com.thinkhome.v3:id/et_name").set_text("<")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "必须添加一项联动条件项", "添加联动条件为空验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# 
# #联动动作为空
# poco("android:id/button3").click()
# poco("android.widget.ListView").child("android.view.ViewGroup")[0].child("com.thinkhome.v3:id/item_layout").click()
# poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[3].click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "必须添加一项联动动作项", "添加联动动作为空验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# 
# #APP推送信息为空
# poco("android:id/button3").click()
# poco("android.widget.ListView").child("android.view.ViewGroup")[1].child("com.thinkhome.v3:id/item_layout").click()
# poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
# poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "App或Email信息不能为空，请编辑信息后再保存。", "APP推送信息为空验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# 
# #联动名称包含<
# poco("android:id/button3").click()
# poco("android.widget.ListView").child("android.view.ViewGroup")[1].child("android.widget.FrameLayout").click()
# poco("com.thinkhome.v3:id/feedback").set_text("测试联动APP推送信息")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "添加联动名称包含<验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# #联动名称包含>
# poco("com.thinkhome.v3:id/et_name").set_text(">")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "添加联动名称包含>验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# #联动名称包含\
# poco("com.thinkhome.v3:id/et_name").set_text("\\")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "添加联动名称包含\验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#                                              
# #联动名称包含&
# poco("com.thinkhome.v3:id/et_name").set_text("&")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "添加联动名称包含&验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     
# # #联动名称包含'
# # poco("com.thinkhome.v3:id/et_name").set_text("'")
# # poco("com.thinkhome.v3:id/toolbar_right_text").click()
# # try:
# #     message=poco("android:id/message").get_text()
# #     assert_equal(message, "数据包含特殊字符", "添加联动名称包含'验证通过")
# # except:
# #     print("Error")
# # else:
# #     print("Ok")
# # finally:
# #     poco("android:id/button3").click()
# #                                              
# # #联动名称包含"
# # poco("com.thinkhome.v3:id/et_name").set_text("\"")
# # poco("com.thinkhome.v3:id/toolbar_right_text").click()
# # try:
# #     message=poco("android:id/message").get_text()
# #     assert_equal(message, "数据包含特殊字符", "添加联动名称包含\"验证通过")
# # except:
# #     print("Error")
# # else:
# #     print("Ok")
# # finally:
# #     poco("android:id/button3").click()
# 
# # #联动名称正确
# poco("com.thinkhome.v3:id/et_name").set_text("w测试联动")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# if poco(text="密码").exists():
#     poco("com.thinkhome.v3:id/et_password").set_text("1234")
# 
# while not poco(text="w测试联动").exists():    
#     poco("com.thinkhome.v3:id/list_background").swipe("up")
# try:
#     message=("w测试联动")
#     assert_equal(message, "w测试联动", "添加联动名称输入正确验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")  
# 
# #联动名称重复
# poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
# poco("com.thinkhome.v3:id/et_name").set_text("w测试联动")
# poco("android.widget.ListView").child("android.view.ViewGroup")[0].child("com.thinkhome.v3:id/item_layout").click()
# poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[3].click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# poco("android.widget.ListView").child("android.view.ViewGroup")[1].child("com.thinkhome.v3:id/item_layout").click()
# poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
# poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# poco("android.widget.ListView").child("android.view.ViewGroup")[1].child("android.widget.FrameLayout").click()
# poco("com.thinkhome.v3:id/feedback").set_text("重复名称联动APP推送信息")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# if poco(text="密码").exists():
#     poco("com.thinkhome.v3:id/et_password").set_text("1234")
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "联动名称已存在", "添加联动名称重复验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# 
# #修改联动
# #联动名称为空
# poco(text="w测试联动").click()
# sleep(5.0)
# poco("com.thinkhome.v3:id/et_name").set_text("")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "名称不能为空", "修改联动名称为空验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# #联动名称包含<
# poco("com.thinkhome.v3:id/et_name").set_text("<")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "修改联动名称包含<验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# #联动名称包含>
# poco("com.thinkhome.v3:id/et_name").set_text(">")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "修改联动名称包含>验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# #联动名称包含\
# poco("com.thinkhome.v3:id/et_name").set_text("\\")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "修改联动名称包含\验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# #联动名称包含&
# poco("com.thinkhome.v3:id/et_name").set_text("&")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "修改联动名称包含&验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# # #联动名称包含'
# # poco("com.thinkhome.v3:id/et_name").set_text("'")
# # poco("com.thinkhome.v3:id/toolbar_right_text").click()
# # try:
# #     message=poco("android:id/message").get_text()
# #     assert_equal(message, "数据包含特殊字符", "修改联动名称包含'验证通过")
# # except:
# #     print("Error")
# # else:
# #     print("Ok")
# # finally:
# #     poco("android:id/button3").click()
# # 
# # #联动名称包含"
# # poco("com.thinkhome.v3:id/et_name").set_text("\"")
# # poco("com.thinkhome.v3:id/toolbar_right_text").click()
# # try:
# #     message=poco("android:id/message").get_text()
# #     assert_equal(message, "数据包含特殊字符", "修改联动名称包含\"验证通过")
# # except:
# #     print("Error")
# # else:
# #     print("Ok")
# # finally:
# #     poco("android:id/button3").click()
#     
# #联动名称重复
# poco("com.thinkhome.v3:id/et_name").set_text("勿删")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# if poco(text="密码").exists:
#     poco("com.thinkhome.v3:id/et_password").set_text("1234")
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "联动名称已存在", "修改联动名称重复验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# #联动名称正确
# poco("com.thinkhome.v3:id/et_name").set_text("w测试联动修改")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# if poco(text="w测试联动修改").exists:
#     message=("w测试联动修改")
# else:
#     poco("com.thinkhome.v3:id/scroll").swipe("up")
# try:
#     assert_equal(message, "w测试联动修改", "修改联动名称输入正确验证通过")
# except:
#     print("Error")
# else:
#     print("Ok") 
#  
# # #联动条件为空
# # poco(text="w测试联动修改").click()
# # sleep(5.0)
# # poco("android.widget.ListView").child("android.view.View")[0].child("android.widget.FrameLayout").swipe("left")
# # poco("com.thinkhome.v3:id/tv_delete").click()
# # poco("android.widget.ListView").child("android.view.View")[1].swipe("left")
# # poco(boundsInParent="[0.125, 0.04765625]").click()
# # poco("com.thinkhome.v3:id/toolbar_right_text").click()
# # try:
# #     message=poco("android:id/message").get_text()
# #     assert_equal(message, "必须添加一项联动条件项", "修改联动条件为空验证通过")
# # except:
# #     print("Error")
# # else:
# #     print("Ok")
# # finally:    
# #     poco("android:id/button3").click()
# # poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# # 
# # #联动动作为空
# # poco(text="w测试联动修改").click()
# # poco("android.widget.ListView").child("android.view.View")[2].child("android.widget.FrameLayout").swipe("left")
# # poco("com.thinkhome.v3:id/tv_delete").click()
# # poco("com.thinkhome.v3:id/toolbar_right_text").click()
# # try:
# #     message=poco("android:id/message").get_text()
# #     assert_equal(message, "必须添加一项联动动作项", "修改联动动作为空验证通过")
# # except:
# #     print("Error")
# # else:
# #     print("Ok")
# # finally:  
# #     poco("android:id/button3").click()
# # poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# # 
# # #APP推送信息为空
# # poco(text="w测试联动修改").click()
# # poco("android.widget.ListView").child("android.view.ViewGroup")[1].child("android.widget.FrameLayout").click()
# # poco("com.thinkhome.v3:id/feedback").set_text("")
# # poco("com.thinkhome.v3:id/toolbar_right_text").click()
# # try:
# #     message=poco("android:id/message").get_text()
# #     assert_equal(message, "App或Email信息不能为空，请编辑信息后再保存。", "APP推送信息为空验证通过")
# # except:
# #     print("Error")
# # else:
# #     print("Ok")
# # finally:  
# #     poco("android:id/button3").click()
# # poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# #     
# #创建类似
# poco(text="w测试联动修改").long_click()
# poco(text="创建类似").click()
# poco("android:id/button1").click()
# if poco(text="密码").exists():
#     poco("com.thinkhome.v3:id/et_password").set_text("1234")
# while not poco(text="w测试联动修改副本").exists():
#     poco("com.thinkhome.v3:id/list_background").swipe("up")
# try:
#     message=("w测试联动修改副本")
#     assert_equal(message, "w测试联动修改副本", "创建类似验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# 
# #同个联动重复创建类似
# poco(text="w测试联动修改").long_click()
# poco(text="创建类似").click()
# poco("android:id/button1").click()
# if poco(text="密码").exists():
#     poco("com.thinkhome.v3:id/et_password").set_text("1234")
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "联动名称已存在", "同个联动重复创建类似验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:  
#     poco("android:id/button3").click()
# 
# #隐藏
# poco(text="w测试联动修改").long_click()
# poco(text="隐藏").click()
# poco(text="展开隐藏项(1)").click()
# if poco(text="w测试联动修改").exists():
#     message="w测试联动修改"
# try:
#     assert_equal(message, "w测试联动修改", "联动隐藏验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# 
# #取消隐藏
# poco(text="w测试联动修改").long_click()
# poco(text="取消隐藏").click()
# if poco(text="w测试联动修改").exists():
#     message="w测试联动修改"
# try:
#     assert_equal(message, "w测试联动修改", "联动取消隐藏验证通过")
# except:
#     print("Error")
# else:
#     print("Ok") 
#     
# #联动：停用
# poco("com.thinkhome.v3:id/scroll").child("android.widget.LinearLayout")[0].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
# if poco(text="密码").exists():
#     poco("com.thinkhome.v3:id/et_password").set_text("1234")
# if poco("com.thinkhome.v3:id/scroll").child("android.widget.LinearLayout")[0].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").poco(checked="False").exists:
#     message = "联动停用"
# try:
#     assert_equal(message,"联动停用","联动停用验证通过")
# except:
#     print("error")
# else:
#     print("ok")
# 
# #联动：启用
# poco("com.thinkhome.v3:id/scroll").child("android.widget.LinearLayout")[0].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
# if poco(text="密码").exists():
#     poco("com.thinkhome.v3:id/et_password").set_text("1234")
# if poco("com.thinkhome.v3:id/scroll").child("android.widget.LinearLayout")[0].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").poco(checked="True").exists:
#     message = "联动启用"
# try:
#     assert_equal(message,"联动启用","联动启用验证通过")
# except:
#     print("error")
# else:
#     print("ok")
#     
# #排序：从上往下
# #排序：从下往上
# #推送：前台
# #推送：后台
# 
#联动日志：查看联动日志
poco("android:id/tabs").child("android.widget.RelativeLayout")[3].click()
poco(text="消息" ).click()
poco(text="联动日志").click()
sleep(5.0)
poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.RelativeLayout")[0].click()

#联动日志：删除单个联动日志中单条数据
poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.LinearLayout")[0].long_click()
poco(text="删除").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco("com.thinkhome.v3:id/toolbar_btn_back").click()


if poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/detail_layout").child("com.thinkhome.v3:id/img_mute").exists():
    #联动日志：打开通知
    poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.RelativeLayout")[0].long_click()
    poco(text="打开通知").click()
    if poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/detail_layout").child("com.thinkhome.v3:id/img_mute").exists():
        message="关闭通知"
    else:
        message="打开通知"
    try:
        assert_equal(message, "打开通知", "打开通知验证通过")
    except:
        print("Error")
    else:
        print("Ok")
else:
    #联动日志：关闭通知
    poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.RelativeLayout")[0].long_click()
    poco(text="关闭通知").click()
    if poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/detail_layout").child("com.thinkhome.v3:id/img_mute").exists():
        message="关闭通知"
    else:
        message="打开通知"
    try:
        assert_equal(message, "关闭通知", "关闭通知验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    
#联动日志：删除单个联动日志
poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.RelativeLayout")[0].long_click()
poco(text="删除").click()

#联动日志：全部已读联动日志
poco(text="批量处理").click()
poco(text="全部已读").click()

#联动日志：全部删除联动日志
poco(text="批量处理").click()
poco(text="全部删除").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#联动警报：查看联动警报
poco(text="联动警报").click()

#联动警报：删除单个联动警报
poco("com.thinkhome.v3:id/setting_message_list").child("android.widget.LinearLayout")[0].long_click()
poco(text="删除").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#联动警报：删除全部联动警报
poco(text="联动警报").long_click()
poco(text="删除").click()

#消息：全部已读
poco(text="批量处理").click()
poco(text="全部已读").click()

#消息：全部删除
poco(text="批量处理").click()
poco(text="全部删除").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
