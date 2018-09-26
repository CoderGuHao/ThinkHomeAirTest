# -*- encoding=utf8 -*-
__author__ = "guhao"

#执行该脚本前确保app权限均打开，关闭系统密码、欢迎页、动态背景下载、成员管理邀请等干扰,退出所有账号

import random
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

auto_setup(__file__)

start_app("com.thinkhome.v3")
sleep(5)

poco("com.thinkhome.v3:id/et_account").set_text("18158288412")
poco("com.thinkhome.v3:id/et_password").set_text("0123456")
poco("com.thinkhome.v3:id/btn_login").click()
sleep(5)

#修改类型
poco(text="类别").click()
poco(text="灯光").click()
num1 = random.randint(0,1)
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="修改图标").click()
num2 = random.randint(0,7)
poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[num2].child("com.thinkhome.v3:id/img_icon_custom").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="修改图标").click()
if poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[num2].child("com.thinkhome.v3:id/img_icon_custom").poco(checked="True").exists:
    message = "当前类型为修改类型"
try:
    assert_equal(message,"当前类型为修改类型","修改类型")
except:
    print("error")
else:
    print("ok")

#修改图标：拍照
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/img_photo").click()
poco(text="拍照").click()
poco("com.huawei.camera:id/shutter_button").click()
poco("com.huawei.camera:id/btn_done").click()
poco("com.thinkhome.v3:id/btn_crop").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#修改图标：从相册选择
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="修改图标").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/img_photo").click()
poco(text="选择本地图片").click()
poco(text="最近").click()
poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[0].child("android.widget.LinearLayout").child("com.android.documentsui:id/icon_mime").click()
poco("com.thinkhome.v3:id/btn_crop").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#修改图标：使用默认
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="修改图标").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/img_icon").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#修改名称：为空
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="修改图标").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/tv_name").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"名称不能为空","修改名称：为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()
    
#修改名称：包含特殊字符<
poco("com.thinkhome.v3:id/tv_name").set_text("<")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含特殊字符<")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()
    
#修改名称：包含特殊字符>
poco("com.thinkhome.v3:id/tv_name").set_text(">")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含特殊字符>")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

# #修改名称：包含特殊字符＇
# poco("com.thinkhome.v3:id/tv_name").set_text("＇")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# message = poco("android:id/message").get_text()
# try:
#     assert_equal(message,"数据包含特殊字符","修改名称：包含特殊字符＇")
# except:
#     print("error")
# else:
#     print("ok")
# finally:
#     poco("android:id/button3").click()
    
#修改名称：包含特殊字符\
poco("com.thinkhome.v3:id/tv_name").set_text("\\")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含特殊字符\\")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()
    
#修改名称：包含特殊字符&
poco("com.thinkhome.v3:id/tv_name").set_text("&")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含特殊字符&")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()
                 
#修改名称：正确修改
poco("com.thinkhome.v3:id/tv_name").set_text("测试")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message=poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/name_layout").child("com.thinkhome.v3:id/tv_device").get_text()
try:
    assert_equal(message,"测试","修改名称：正确修改")
except:
    print("error")
else:
    print("ok")

#设置房间
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="更多设置").click()
poco(text="房间").click()
num3 = random.randint(0,7)
poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num3].child("com.thinkhome.v3:id/checked_text_view").click()
message1 = poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num3].child("com.thinkhome.v3:id/checked_text_view").get_text()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
message2 = poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/name_layout").child("com.thinkhome.v3:id/tv_room").get_text()
try:
    assert_equal(message1,message2,"设置房间")
except:
    print("error")
else:
    print("ok")   

#添加定时：不选择任何时间
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="定时设置").click()

#清除所有已有定时
while 1:
    try:
        poco("com.thinkhome.v3:id/timing_list").child("android.widget.RelativeLayout")[0].exists
    except:
        break
    else:
        poco("com.thinkhome.v3:id/timing_list").child("android.widget.RelativeLayout")[0].long_click()
        poco(text="删除").click()
        continue
    
poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
poco("android.widget.RelativeLayout").child("com.thinkhome.v3:id/start_time_layout").child("com.thinkhome.v3:id/open_checkbox").click()
poco("android.widget.RelativeLayout").child("com.thinkhome.v3:id/end_time_layout").child("com.thinkhome.v3:id/off_checkbox").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"至少选择一个时间","添加定时：不选择任何时间")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#添加定时：有效添加
poco("android.widget.RelativeLayout").child("com.thinkhome.v3:id/start_time_layout").child("com.thinkhome.v3:id/open_checkbox").click()
poco("android.widget.RelativeLayout").child("com.thinkhome.v3:id/end_time_layout").child("com.thinkhome.v3:id/off_checkbox").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    if poco("com.thinkhome.v3:id/timing_list").child("android.widget.RelativeLayout")[0].exists:
        message = "添加定时成功"
    assert_equal(message,"添加定时成功","添加定时：有效添加")
except:
    print("error")
else:
    print("ok")
    
#修改定时：修改动作
poco("com.thinkhome.v3:id/timing_list").child("android.widget.RelativeLayout")[0].click()
poco("com.thinkhome.v3:id/model_on").click()
poco("android:id/numberpicker_input").swipe([-0.0100, 0.1000])
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#修改定时：修改时间
poco("com.thinkhome.v3:id/timing_list").child("android.widget.RelativeLayout")[0].click()
poco("com.thinkhome.v3:id/open_time").click()
hour = random.randint(1,23)
poco(str(hour)).click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#修改定时：切换到日出日落
poco("com.thinkhome.v3:id/timing_list").child("android.widget.RelativeLayout")[0].click()
poco("com.thinkhome.v3:id/radio_on_sunsets").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#修改定时：选择日期
poco("com.thinkhome.v3:id/timing_list").child("android.widget.RelativeLayout")[0].click()
poco("com.thinkhome.v3:id/checkbox_monday").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#停用定时
poco("com.thinkhome.v3:id/switch_view").click()

#启用定时
poco("com.thinkhome.v3:id/switch_view").click()

#设置倒计时
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="更多设置").click()
poco(text="倒计时").click()
num4 = random.randint(0,6)
poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num4].click()
num4 = random.randint(0,6)
poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num4].click()
message = poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num4].child("com.thinkhome.v3:id/checked_text_view").get_text()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message1 = poco("com.thinkhome.v3:id/setting_countdown").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()

print(message1)
try:
    assert_equal(message,message1,"设置倒计时")
except:
    print("error")
else:
    print("ok")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#执行倒计时
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco("com.thinkhome.v3:id/item_id")[1].click()
poco("android:id/button1").click()

# #设置最长开启时间
# poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
# poco(text="更多设置").click()
# poco(text="最长开启").click()
# poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].click()
# num2 = random.randint(0,7)
# poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].click()
# message = poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].child("com.thinkhome.v3:id/checked_text_view").get_text()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# message1 = poco("com.thinkhome.v3:id/setting_max_on_time").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
# try:
#     assert_equal(message,message1,"设置最长开启时间")
# except:
#     print("error")
# else:
#     print("ok")
# finally:
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    
# #超时提醒
# poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# poco(text="电源").click()
# poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
# poco(text="更多设置").click()
# poco(text="超时提醒").click()
# poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].click()
# num2 = random.randint(0,7)
# poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].click()
# message = poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].child("com.thinkhome.v3:id/checked_text_view").get_text()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# message1 = poco("com.thinkhome.v3:id/setting_overtime").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
# try:
#     assert_equal(message,message1,"设置最长开启时间")
# except:
#     print("error")
# else:
#     print("ok")

#设置过载电流
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco(text="电源").click()
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="更多设置").click()
poco(text="过载电流").click()
poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].click()
num2 = random.randint(0,7)
poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].click()
message = poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[num2].child("com.thinkhome.v3:id/checked_text_view").get_text()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message1 = poco("com.thinkhome.v3:id/setting_over_current").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
try:
    assert_equal(message,message1,"设置过载电流")
except:
    print("error")
else:
    print("ok")
    
#设置过压欠压：关闭该路电源停启用
poco(text="过压/欠压").click()
poco("com.thinkhome.v3:id/switch_view").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="过压/欠压").click()
poco("com.thinkhome.v3:id/switch_view").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#设置过压欠压：恢复默认
poco(text="过压/欠压").click()
poco("com.thinkhome.v3:id/btn_restore").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#按钮显示：停启用
poco(text="按钮显示").click()
poco("com.thinkhome.v3:id/switch_view").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="按钮显示").click()
poco("com.thinkhome.v3:id/switch_view").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#按钮显示：修改按钮上下方显示内容
poco(text="按钮显示").click()
poco("com.thinkhome.v3:id/item_top").click()
poco("android:id/numberpicker_input").swipe([-0.0070, 0.1060])
poco("android:id/button1").click()
message = poco("com.thinkhome.v3:id/item_top").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
poco("com.thinkhome.v3:id/item_bottom").click()
poco("android:id/numberpicker_input").swipe([0.0, -0.1040])
poco("android:id/button1").click()
message = message + ", " + poco("com.thinkhome.v3:id/item_bottom").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message1 = poco("com.thinkhome.v3:id/setting_home_page_showing").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
try:
    assert_equal(message,message1,"按钮显示：修改按钮上下方显示内容")
except:
    print("error")
else:
    print("ok")

#清除数据
poco(text="清除数据").click()
poco("android:id/button1").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据清零已成功","清除数据")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#分享：云子分享
poco("com.thinkhome.v3:id/scrollView").swipe([0.01, -0.73])
poco(text="分享").click()
poco(text="Beacon").click()
poco("com.thinkhome.v3:id/tv_device").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="Beacon").click()
poco("com.thinkhome.v3:id/tv_device").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#设备密码：启用
poco(text="设备密码").click()
poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco(text="开启").click()
poco(checked="不开启").click()
poco(text="开启").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("com.thinkhome.v3:id/setting_password").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
try:
    assert_equal(message,"开启","设备密码：启用")
except:
    print("error")
else:
    print("ok")
    
#设备密码：不启用
poco(text="设备密码").click()
poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco(text="不开启").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("com.thinkhome.v3:id/setting_password").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
try:
    assert_equal(message,"未启用","设备密码：不启用")
except:
    print("error")
else:
    print("ok")

#所属控制器：查看
poco(text="所属控制器").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#设备隐藏：隐藏
poco(text="设备隐藏").click()
poco(text="在“全部”列表中隐藏").click()
poco(text="在“全部”列表中隐藏").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="设备隐藏").click()
poco(text="在“全部”列表中隐藏").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#日志：查看、删除
poco(text="日志").click()
try:
    if poco("com.thinkhome.v3:id/tv_content").exists:
        poco("com.thinkhome.v3:id/tv_content").long_click();
        poco(text="删除").click()
except:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#参数调整:恢复默认
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco(text="环境").click()
for i in range(1,10):
    if  poco(text="K温度").exists():
        poco(text="K温度").long_click()
        poco(text="更多设置").click()
        poco(text="参数调整").click()
        break
    else:
        poco("android.support.v4.widget.SlidingPaneLayout").swipe([0.00, -0.31])
        sleep(1)
poco("com.thinkhome.v3:id/btn_restore").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#数值校准
poco(text="数值校准").click()
poco("com.thinkhome.v3:id/btn_increase").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="数值校准").click()
poco("com.thinkhome.v3:id/btn_decrease").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#自定义按键名称:为空
poco(text="遥控器").click()
for i in range(1,10):
    if  poco(text="红外九键遥控").exists():
        poco(text="红外九键遥控").click()
        break
    else:
        poco("android.support.v4.widget.SlidingPaneLayout").swipe([0.00, -0.31])
        sleep(1)
poco("com.thinkhome.v3:id/btn_2").long_click()
poco("com.thinkhome.v3:id/et_name").set_text("")
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"名称不能为空","自定义按键名称:为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()
    
# #自定义按键名称：超过4位 （4.6.14修改可开放）
# poco("com.thinkhome.v3:id/btn_2").long_click()
# poco("com.thinkhome.v3:id/et_name").set_text("12345")
# message = poco("android:id/message").get_text()
# try:
#     assert_equal(message,"名称长度不能超过四位","自定义按键名称：超过4位")
# except:
#     print("error")
# else:
#     print("ok")
# finally:
#     poco("android:id/button3").click()
    
#自定义按键名称：正确修改
poco("com.thinkhome.v3:id/btn_2").long_click()
poco("com.thinkhome.v3:id/et_name").set_text("1")
message = poco("com.thinkhome.v3:id/btn_2").get_text()
try:
    assert_equal(message,"1","自定义按键名称：正确修改")
except:
    print("error")
else:
    print("ok")
finally:
    poco("com.thinkhome.v3:id/btn_back").click()
    poco("com.thinkhome.v3:id/btn_back").click()

#删除设备：删除成功
poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
poco(text="设备管理").click()
poco(text="ThinkID:77670215").click()
poco("com.thinkhome.v3:id/tv_device").long_click()
poco(text="删除").click()
poco("android:id/button1").click()
message = poco("com.thinkhome.v3:id/tv_no_device").get_text()
try:
    assert_equal(message,"尚无设备","删除设备：删除成功")
except:
    print("error")
else:
    print("ok")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#删除设备：设备有关联属性
poco(text="ThinkID:37054164").click()
poco("com.thinkhome.v3:id/tv_device").long_click()
poco(text="删除").click()
poco("android:id/button1").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"部分设备有联动，无法停用这些设备","删除设备：设备有关联属性")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    
#排序：从上往下
poco("android:id/tabs").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tab_image").click()
poco("com.thinkhome.v3:id/img_setting").click()
poco(text="自定义排序").click()
message = poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/name_layout").child("com.thinkhome.v3:id/tv_device").get_text()
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/list_row_draganddrop_touchview").swipe([0.00, 0.14])
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message1 = poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/name_layout").child("com.thinkhome.v3:id/tv_device").get_text()
try:
    assert_equal(message,message1,"排序：从上往下")
except:
    print("error")
else:
    print("ok")
    
#排序：从下往上
poco("com.thinkhome.v3:id/img_setting").click()
poco(text="自定义排序").click()
message = poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/name_layout").child("com.thinkhome.v3:id/tv_device").get_text()
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/list_row_draganddrop_touchview").swipe([0.01, -0.14])
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message1 = poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/name_layout").child("com.thinkhome.v3:id/tv_device").get_text()
try:
    assert_equal(message,message1,"排序：从下往上")
except:
    print("error")
else:
    print("ok")
    
#排序：恢复默认
poco("com.thinkhome.v3:id/img_setting").click()
poco(text="恢复默认排序").click()
poco("android:id/button1").click()

#名称组合：名称以区域优先
poco("com.thinkhome.v3:id/img_setting").click()
poco(text="名称组合").click()
poco(text="名称以区域优先").click()

#名称组合：只显示设备号
poco("com.thinkhome.v3:id/img_setting").click()
poco(text="名称组合").click()
poco(text="只显示设备号").click()

#名称组合：名称与设备区域平行
poco("com.thinkhome.v3:id/img_setting").click()
poco(text="名称组合").click()
poco(text="名称与设备区域平行").click()

#名称组合：名称以设备优先
poco("com.thinkhome.v3:id/img_setting").click()
poco(text="名称组合").click()
poco(text="名称以设备优先").click()

#下拉全关
poco("com.thinkhome.v3:id/list_background").swipe([0.00, 0.28])
poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
poco("com.thinkhome.v3:id/list_background").swipe([0.00, 0.28])
sleep(1)
message = poco("com.thinkhome.v3:id/toolbar_header").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/toolbar_tv_name").get_text()
try:
    assert_equal(message,"未关(0)","下拉全关")
except:
    print("error")
else:
    print("ok")