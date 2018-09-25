# -*- encoding=utf8 -*-
__author__ = "guhao"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

name="测试"

auto_setup(__file__)

start_app("com.thinkhome.v3")
sleep(5)

#手动输入：为空
poco(text="设置").click()
poco(text="设备管理").click()
# poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
# poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
# poco(text="手动输入").click()
# poco("com.thinkhome.v3:id/manually_enter_id").set_text("")
# poco("com.thinkhome.v3:id/btn_ok").click()
# try:
#     assert_exists(Template(r"tpl1536719197979.png", record_pos=(-0.003, 0.529), resolution=(1080, 1920)), "手动输入：为空")
# except:
#     print("Error")
# else:
#     print("Ok") 
#     
# #手动输入：ID格式不正确
# poco("com.thinkhome.v3:id/manually_enter_id").set_text("1")
# poco("com.thinkhome.v3:id/btn_ok").click()
# try:
#     assert_exists(Template(r"tpl1536719983748.png", record_pos=(-0.001, 0.527), resolution=(1080, 1920)), "#手动输入：ID格式不正确")
# except:
#     print("Error")
# else:
#     print("Ok")
#     
# #手动输入：ID不存在
# poco("com.thinkhome.v3:id/manually_enter_id").set_text("12345678")
# poco("com.thinkhome.v3:id/btn_ok").click()
# message = poco("android:id/message").get_text()
# try:
#     assert_equal(message,"控制器不存在","手动输入：ID不存在")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     
# #手动输入：已被该账号添加       
# poco("com.thinkhome.v3:id/manually_enter_id").set_text("74780900")
# poco("com.thinkhome.v3:id/btn_ok").click()
# poco("com.thinkhome.v3:id/btn_active").click()
# poco("com.thinkhome.v3:id/btn_active").click()
# message = poco("android:id/message").get_text()
# try:
#     assert_equal(message,"控制器已被该帐号添加","手动输入：已被该账号添加")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
#     
# #手动输入：已被其他账号添加
# poco("com.thinkhome.v3:id/manually_enter_id").set_text("97557754")
# poco("com.thinkhome.v3:id/btn_ok").click()
# message = poco("android:id/message").get_text()
# try:
#     assert_equal(message,"控制器已被其他帐号添加","手动输入：已被其他账号添加")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()    
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
#     
# #控制器删除：主机下还有从机挂载
# poco(text="ThinkID:66762741").long_click()
# poco(text="更多设置").click()
# poco("com.thinkhome.v3:id/btn_delete").click()
# poco("android:id/button1").click()
# message = poco("android:id/message").get_text()
# try:
#     assert_equal(message,"请先删除该控制器下挂载的从机","控制器删除：主机下还有从机挂载")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# 
# #控制器删除：删除成功
# for i in range(1,10):
#     if  poco(text="ThinkID:33049825").exists():
#         poco(text="ThinkID:33049825").long_click()
#         poco(text="更多设置").click()
#         poco("com.thinkhome.v3:id/btn_delete").click()
#         poco("android:id/button1").click()
#         break
#     else:
#         poco("com.thinkhome.v3:id/expand_listview").swipe([-0.02, -0.40])
#         sleep(2)
# 
# if(poco(text="ThinkID:33049825").exists()):
#     message="删除失败"
# else:
#     message="删除成功"
# try:
#     assert_equal(message,"删除成功","控制器删除：删除成功")
# except:
#     print("Error")
# else:
#     print("Ok")    

#修改名称：为空
poco(text="ThinkID：77670215").long_click()
poco(text="名称").click()
poco("com.thinkhome.v3:id/tv_name").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"名称不能为空","修改名称：为空")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

# 修改名称：包含<字符
poco("com.thinkhome.v3:id/tv_name").set_text("<")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含<字符")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

# 修改名称：包含>字符
poco("com.thinkhome.v3:id/tv_name").set_text(">")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含>字符")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

# 修改名称：包含&字符
poco("com.thinkhome.v3:id/tv_name").set_text("&")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含&字符")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

# 修改名称：包含\字符
poco("com.thinkhome.v3:id/tv_name").set_text("\\")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"数据包含特殊字符","修改名称：包含\字符")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    
# # 修改名称：包含＇字符
# poco("com.thinkhome.v3:id/tv_name").set_text("＇")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# message = poco("android:id/message").get_text()
# try:
#     assert_equal(message,"数据包含特殊字符","修改名称：包含＇字符")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()

# 修改名称：正确输入
poco("com.thinkhome.v3:id/tv_name").set_text(name)
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="ThinkID：77670215").long_click()
poco(text="更多设置").click()
message = poco("com.thinkhome.v3:id/tv_name").get_text()
try:
    assert_equal(message,"name","修改名称：正确输入")
except:
    print("Error")
else:
    print("Ok")

# 位置：拍照
poco(text="位置").click()
poco("com.thinkhome.v3:id/iv").click()
poco(text="拍照").click()
poco("com.huawei.camera:id/shutter_button").click()#考虑用图像识别
poco("com.huawei.camera:id/btn_done").click()#考虑用图像识别
poco("com.android.gallery3d:id/head_select_right").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 位置：从相册选择
poco(text="位置").click()
poco("com.thinkhome.v3:id/iv").click()
poco(text="选择本地图片").click()
poco(text="最近").click()
poco("com.android.documentsui:id/icon_mime").click()
poco("com.android.gallery3d:id/head_select_right").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 位置：删除
poco(text="位置").click()
poco("com.thinkhome.v3:id/iv").click()
poco(text="删除").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 位置：添加描述
poco(text="位置").click()
poco("com.thinkhome.v3:id/feedback").set_text(name)
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 功能停启用：停用
poco(text="功能停启用").click()
poco(text="A门锁1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 功能停启用：启用
poco(text="功能停启用").click()
poco(text="A门锁1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 反馈数据选项设置
poco("com.thinkhome.v3:id/expand_listview").child("com.thinkhome.v3:id/detail_layout")[4].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/expand_img").click()
for i in range(1,10):
    if  poco(text="ThinkID:94299091").exists():
        poco(text="ThinkID:33049825").long_click()
        poco(text="更多设置").click()
        poco(text="指示灯方案").click()
        break
    else:
        poco("com.thinkhome.v3:id/expand_listview").swipe([-0.02, -0.40])
        sleep(1)


poco(text="反馈数据选项").click()
poco(text="二氧化碳").click()
poco(text="TVOC").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 反馈数据选项：恢复默认
poco(text="反馈数据选项").click()
poco("com.thinkhome.v3:id/btn_restore").click()
poco(text="反馈数据选项").click()

# 夜间显示：设置
poco(text="反馈数据选项").click()
poco(text="昏暗不显示").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 替换：为空
poco("com.thinkhome.v3:id/expand_listview").child("com.thinkhome.v3:id/detail_layout")[0].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/expand_img").click()
poco(text="ThinkID:94170840").click()
poco(text="更多设置").click()
poco(text="替换").click()
poco("com.thinkhome.v3:id/edit_text_view").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("com.thinkhome.v3:id/tv_name").get_text()
try:
    assert_equal(message,"内容不能为空","替换：为空")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    
# 替换：控制器不存在
poco("com.thinkhome.v3:id/edit_text_view").set_text("111")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("com.thinkhome.v3:id/tv_name").get_text()
try:
    assert_equal(message,"控制器不存在","替换：控制器不存在")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()