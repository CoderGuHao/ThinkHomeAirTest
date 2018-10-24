# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

start_app("com.thinkhome.v3")
sleep(5.0)

#登录181***
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()

#添加房间
poco("com.thinkhome.v3:id/toolbar_btn_setting").click()

#选择房间图标
poco("com.thinkhome.v3:id/icon_layout").click()
while poco("android:id/numberpicker_input").get_text() != "卧室":
    poco("android.widget.NumberPicker").swipe("up")
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/icon_layout").click()
try:
    message=poco("android:id/numberpicker_input").get_text()
    assert_equal(message, "卧室", "选择房间图标验证通过")
except:
    print("Error")
else:
    print("Ok") 
finally:
    poco("android:id/button2").click()

#选择楼层
poco("com.thinkhome.v3:id/floor_layout").click()
while poco("android:id/numberpicker_input").get_text() != "1F":
    poco("android.widget.NumberPicker").swipe("up")
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/floor_layout").click()
try:
    message=poco("android:id/numberpicker_input").get_text()
    assert_equal(message, "1F", "选择房间楼层验证通过")
except:
    print("Error")
else:
    print("Ok") 
finally:
    poco("android:id/button2").click()
    
#房间名称：为空
poco("com.thinkhome.v3:id/tv_name_value").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "房间名称不能为空", "房间名称为空验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#房间名称：包含<符号
poco("com.thinkhome.v3:id/tv_name_value").set_text("<")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "房间名称包含<符号验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#房间名称：包含>符号
poco("com.thinkhome.v3:id/tv_name_value").set_text(">")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "房间名称包含>符号验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    
#房间名称：包含\符号
poco("com.thinkhome.v3:id/tv_name_value").set_text("\\")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "房间名称包含\符号验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    
#房间名称：包含&符号
poco("com.thinkhome.v3:id/tv_name_value").set_text("&")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "房间名称包含&符号验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    
# #房间名称：包含'符号
# poco("com.thinkhome.v3:id/tv_name_value").set_text("'")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "房间名称包含'符号验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
# 
# #房间名称：包含"符号
# poco("com.thinkhome.v3:id/tv_name_value").set_text("\"")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "房间名称包含\"符号验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()    
                 
#房间名称：正确输入
poco("com.thinkhome.v3:id/tv_name_value").set_text("w测试卧室")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
for i in range(1,100):
    if poco(text="w测试卧室").exists():
        poco(text="w测试卧室").click() 
        break
    else:
        poco("android.widget.ListView").swipe("up")
try:
    message=poco("com.thinkhome.v3:id/title_text").get_text()
    assert_equal(message, "一层w测试卧室", "房间名称正常输入验证通过")
except:
    print("Error")
else:
    print("Ok")

#修改房间
poco("com.thinkhome.v3:id/img_setting").click()
poco(text="房间设置").click()

#修改房间图标：拍照
poco("com.thinkhome.v3:id/icon_layout").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/img_photo").click()
poco(text="拍照").click()
poco("com.huawei.camera:id/shutter_button").click()
poco("com.huawei.camera:id/btn_done").click()
poco("com.thinkhome.v3:id/btn_crop").click()

#修改房间图标：本地图片
poco("com.thinkhome.v3:id/img_photo").click()
poco(text="从相册选择").click()
poco(text="最近").click()
poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[0].child("android.widget.LinearLayout").child("com.android.documentsui:id/icon_mime").click()
poco("com.thinkhome.v3:id/btn_crop").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#修改房间图标：默认
poco("com.thinkhome.v3:id/icon_layout").click()
poco(text="客厅").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")   
poco("com.thinkhome.v3:id/icon_layout").click()
if poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[2].child("android.widget.LinearLayout").child("com.thinkhome.v3:id/tv_room").poco(checked="True").exists:
    message = "客厅"
try:
    assert_equal(message,"客厅","修改房间图标：默认，验证通过")
except:
    print("error")
else:
    print("ok")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#修改楼层
poco("com.thinkhome.v3:id/setting_floor").click()
while poco("android:id/numberpicker_input").get_text() != "2F":
    poco("android.widget.NumberPicker").swipe("up")
poco("android:id/button1").click()
try:
    message=poco("com.thinkhome.v3:id/setting_floor").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
    assert_equal(message, "二层", "修改楼层验证通过")
except:
    print("Error")
else:
    print("Ok") 
    
#房间名称：为空
poco("com.thinkhome.v3:id/icon_layout").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/tv_name").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "名称不能为空", "修改房间名称为空验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#房间名称：包含<字符
poco("com.thinkhome.v3:id/tv_name").set_text("<")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称包含<字符验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#房间名称：包含>字符
poco("com.thinkhome.v3:id/tv_name").set_text(">")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称包含>字符验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#房间名称：包含\字符
poco("com.thinkhome.v3:id/tv_name").set_text("\\")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称包含\字符验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#房间名称：包含&字符
poco("com.thinkhome.v3:id/tv_name").set_text("&")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称包含&字符验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

# #房间名称：包含'字符
# poco("com.thinkhome.v3:id/tv_name").set_text("'")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "修改房间名称包含'字符验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     
# #房间名称：包含"字符
# poco("com.thinkhome.v3:id/tv_name").set_text("\"")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "数据包含特殊字符", "修改房间名称包含\"字符验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()   
    
#房间名称：正确输入
poco("com.thinkhome.v3:id/tv_name").set_text("w测试客厅")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(message, "w测试客厅", "修改房间名称正常输入验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#新增房屋分享
poco("com.thinkhome.v3:id/setting_share").click()
poco("com.thinkhome.v3:id/btn_add_new_share_ms").click()
#分享名称：为空
poco("com.thinkhome.v3:id/share_name_edt").set_text("")
poco("com.thinkhome.v3:id/qr_code_is_generated").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "分享名称不能为空", "分享名称为空验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#分享名称：正确输入
poco("com.thinkhome.v3:id/share_name_edt").set_text("w测试分享")
poco("com.thinkhome.v3:id/qr_code_is_generated").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
try:
    if poco(text="w测试分享").exists:
        message="w测试分享"
    else:
        message=""
    assert_equal(message, "w测试分享", "分享名称正确输入验证通过")
except:
    print("Error")
else:
    print("Ok") 
    
#当前时间已有分享
poco("com.thinkhome.v3:id/btn_add_new_share_ms").click()
poco("com.thinkhome.v3:id/share_name_edt").set_text("w测试分享2")
poco("com.thinkhome.v3:id/qr_code_is_generated").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "当前选择时间已有分享，请重新设置时间！", "当前时间已有分享")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#分享开始时间早于当前时间
poco("com.thinkhome.v3:id/start_time_iteam").click()
poco("com.thinkhome.v3:id/year").swipe("down")
poco("com.thinkhome.v3:id/tv_ensure").click()
poco("com.thinkhome.v3:id/qr_code_is_generated").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "开始时间不能早于当前时间", "分享开始时间早于当前时间验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    
#分享开始时间晚于截止时间
poco("com.thinkhome.v3:id/btn_add_new_share_ms").click()
poco("com.thinkhome.v3:id/share_name_edt").set_text("w测试分享2")
poco("com.thinkhome.v3:id/start_time_iteam").click()
poco("com.thinkhome.v3:id/year").swipe("up")
poco("com.thinkhome.v3:id/tv_ensure").click()
poco("com.thinkhome.v3:id/qr_code_is_generated").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "开始时间不能晚于截止时间", "分享开始时间晚于截止时间验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    
# #分享开始时间等于截止时间
# poco("com.thinkhome.v3:id/start_time_iteam").click()
# poco("com.thinkhome.v3:id/year").swipe("up")
# poco("com.thinkhome.v3:id/tv_ensure").click()
# poco("com.thinkhome.v3:id/qr_code_is_generated").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "开始时间不能晚于截止时间", "分享开始时间等于截止时间验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
    
#保存二维码图片
poco("com.thinkhome.v3:id/list_view_share_list_ms").click()
poco("com.thinkhome.v3:id/save_qr_code_image").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "图片已保存至系统相册", "保存二维码图片验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

# #分享给微信好友：安装了微信
# poco("com.thinkhome.v3:id/wechat_share_to_friends").click()
# poco("com.tencent.mm:id/h8").child("android.widget.RelativeLayout")[1].click()
# poco("com.tencent.mm:id/apj").click()
# try:
#     message=poco("com.tencent.mm:id/apv").get_text()
#     assert_equal(message, "已发送", "微信分享房间验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("com.tencent.mm:id/api").click()

#删除房间：还存在分享    
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/btn_delete").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try: 
    message=poco("android:id/message").get_text()
    assert_equal(message, "房间分享未结束，禁止删除！", "删除房间：分享未结束,验证通过")
except:
    print("Error")
else:
    print("Ok")   
finally:
    poco("android:id/button3").click()
    
#修改分享
#分享名称：为空
poco(text="房间分享").click()
poco(text="w测试分享").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/share_name_edt").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "分享名称不能为空", "修改分享名称为空验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    
#分享名称：正确输入
poco("com.thinkhome.v3:id/share_name_edt").set_text("w测试分享修改")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="w测试分享修改").exists():
    message="w测试分享修改"
try:
    assert_equal(message, "w测试分享修改", "修改分享名称正确输入验证通过")   
except:
    print("Error")
else:
    print("Ok")
poco(text="w测试分享修改").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#分享开始时间早于当前时间
poco("com.thinkhome.v3:id/start_time_iteam").click()
poco("com.thinkhome.v3:id/year").swipe("down")
poco("com.thinkhome.v3:id/tv_ensure").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "开始时间不能早于当前时间", "分享开始时间早于当前时间验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    
#分享开始时间晚于截止时间
poco("com.thinkhome.v3:id/start_time_iteam").click()
poco("com.thinkhome.v3:id/year").swipe("up")
poco("com.thinkhome.v3:id/year").swipe("up")
poco("com.thinkhome.v3:id/tv_ensure").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "开始时间不能晚于截止时间", "分享开始时间晚于截止时间验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
    
# #分享开始时间等于截止时间
# poco("com.thinkhome.v3:id/start_time_iteam").click()
# poco("com.thinkhome.v3:id/year").swipe("up")
# poco("com.thinkhome.v3:id/tv_ensure").click()
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# try:
#     message=poco("android:id/message").get_text()
#     assert_equal(message, "开始时间不能晚于截止时间", "分享开始时间等于截止时间验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#取消分享
poco("com.thinkhome.v3:id/cancel_the_share_btn").click()
poco("android:id/button1").click()
if not poco(text="w测试分享修改").exists():
    try:
        message=poco("com.thinkhome.v3:id/ongoing_sharing_hint").get_text()
        assert_equal(message, "无进行中的分享。", "取消分享验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    finally:
        poco("com.thinkhome.v3:id/toolbar_btn_back").click()


if poco("com.thinkhome.v3:id/setting_bookmark").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text() == "已标星":
    #取消标星
    poco(text="标星").click()
    poco(text="取消标星").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_bookmark").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message, "未标星", "房间取消标星验证通过")
    except:
        print("Error")
    else:
        print("Ok")
else:   
    #标星
    poco(text="标星").click()
    poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/checked_text_view").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_bookmark").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message, "已标星", "房间标星验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
#删除房间
poco("com.thinkhome.v3:id/btn_delete").click()
poco("android:id/button1").click()
if not poco(text="w测试客厅").exists():
    try:
        message=poco("com.thinkhome.v3:id/toolbar_tv_name").get_text()
        assert_equal(message, "房间", "删除房间验证通过")
    except:
        print("Error")
    else:
        print("Ok") 

# #楼层控制：灯光全开
# poco(text="1F").long_click()
# poco(text="灯光全开").click()
# #楼层控制：灯光全关
# poco(text="1F").long_click()
# poco(text="灯光全关").click()
# #楼层控制：设备全关
# poco(text="1F").long_click()
# poco(text="设备全关").click()
# #房间控制：灯光全开
# poco(text="客厅").long_click()
# poco(text="灯光全开").click()
# #房间控制：灯光全关
# poco(text="客厅").long_click()
# poco(text="灯光全关").click()
# #房间控制：设备全关
# poco(text="客厅").long_click()
# poco(text="设备全关").click()

#户型图功能：停用
poco("android:id/tabs").child("android.widget.RelativeLayout")[3].click()
poco(text="通用").click()
poco(text="户型图").click()
poco("com.thinkhome.v3:id/switch_view").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()
if not poco("com.thinkhome.v3:id/clickable_image_view").exists():
    message="无户型图"
else:
    message="有户型图"
try:
    assert_equal(message, "无户型图", "户型图停用验证通过")
except:
    print("Error")
else:
    print("Ok")

#户型图：启用
poco("android:id/tabs").child("android.widget.RelativeLayout")[3].click()
poco(text="通用").click()
poco(text="户型图").click()
poco("com.thinkhome.v3:id/switch_view").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()
if not poco("com.thinkhome.v3:id/clickable_image_view").exists():
    message="无户型图"
else:
    message="有户型图"
try:
    assert_equal(message, "有户型图", "户型图启用验证通过")
except:
    print("Error")
else:
    print("Ok")  

#添加楼层户型图：楼层下没有房间
poco("android:id/tabs").child("android.widget.RelativeLayout")[3].click()
poco(text="通用").click()
poco(text="户型图").click()
poco(text="四层").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "该楼层没有房间，不可以添加户型图，请先为此楼层添加房间。", "添加楼层户型图：楼层下没有房间，验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:   
    poco("android:id/button3").click()

#添加楼层户型图：从相册选择
poco(text="未设楼层").click()
if poco(text="更换底图").exists():
    poco("com.thinkhome.v3:id/tv_change").click()
else:
    poco("com.thinkhome.v3:id/add_img").click()
poco(text="从相册选择").click()
poco("android:id/list").child("android.widget.LinearLayout")[0].click()
poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[0].click()
poco("com.android.gallery3d:id/head_select_right").click()

#添加楼层户型图：从图库选择
poco("com.thinkhome.v3:id/tv_change").click()
poco(text="从图库选择").click()
poco("com.thinkhome.v3:id/recycler_view").child("android.widget.LinearLayout")[0].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/grid_view").child("android.widget.LinearLayout")[0].click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# #户型图房间设置：正确设置
# poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[0].click()
# touch((0.5,0.3),1)#点击户型图报错
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# poco(text="未设楼层").click()
# try:
#     message=poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/detail_layout").child("com.thinkhome.v3:id/tv_count").get_text()
#     assert_equal(message, "已设置", "户型图房间设置验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:   
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# 
# #户型图房间设置：删除设置
# poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[0].long_click()
# poco(text="删除").click()

#楼层户型图功能：停用
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco(text="未设楼层").long_click()
poco(text="停用").click()
try:
    message=poco(boundsInParent="[0.5583333333333333, 0.03125]").get_text()
    assert_equal(message, "停用", "楼层户型图停用验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#楼层户型图功能：启用
poco(text="未设楼层").long_click()
poco(text="启用").click()
try:
    message=poco(boundsInParent="[0.5583333333333333, 0.03125]").get_text()
    assert_equal(message, "启用", "楼层户型图启用验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#楼层户型图功能：删除
poco(text="未设楼层").long_click()
poco(text="删除").click()
try:
    message=poco(boundsInParent="[0.5583333333333333, 0.03125]").get_text()
    assert_equal(message, "未设置", "楼层户型图删除验证通过")
except:
    print("Error")
else:
    print("Ok")

poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()

#户型图操作：长按
poco("com.thinkhome.v3:id/clickable_image_view").long_click()
try:
    message=poco("android:id/alertTitle").get_text()
    assert_equal(message, "1F", "户型图长按验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco(text="取消").click()

# # 户型图操作：双击
# poco("com.thinkhome.v3:id/clickable_image_view").double_click()
# try:
#     message=poco("com.thinkhome.v3:id/title_text").get_text()
#     assert_equal(message, "一层", "户型图双击验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# 
# #户型图操作：单击设置区域
# poco("com.thinkhome.v3:id/clickable_image_view").click()
# try:
#     message=poco("com.thinkhome.v3:id/title_text").get_text()
#     assert_equal(message, "一层餐厅", "户型图单击设置区域验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
