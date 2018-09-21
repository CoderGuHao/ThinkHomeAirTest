# -*- encoding=utf8 -*-
__author__ = "guhao"

#执行该脚本前确保app权限均打开，关闭系统密码、欢迎页、动态背景下载、成员管理邀请等干扰

import random
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

auto_setup(__file__)

start_app("com.thinkhome.v3")
sleep(5)

# poco("com.thinkhome.v3:id/et_account").set_text("18158288412")
# poco("com.thinkhome.v3:id/et_password").set_text("0123456")
# poco("com.thinkhome.v3:id/btn_login").click()
# sleep(5)

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
    
#设置过压欠压：开启关闭电源

    
