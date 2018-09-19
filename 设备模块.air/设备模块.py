# -*- encoding=utf8 -*-
__author__ = "guhao"

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
num1 = random.randint(0,8)
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="修改图标").click()
num2 = random.randint(0,8)
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
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="修改图标").click()
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
poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[num1].child("com.thinkhome.v3:id/img_icon").long_click()
poco(text="修改图标").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
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

#修改名称：包含特殊字符＇
poco("com.thinkhome.v3:id/tv_name").set_text("＇")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含特殊字符＇")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()
    
#修改名称：包含特殊字符\
poco("com.thinkhome.v3:id/tv_name").set_text("\")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含特殊字符\")
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

    

