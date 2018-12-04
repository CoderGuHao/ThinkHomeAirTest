# -*- encoding=utf8 -*-
__author__ = "wenglibing"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


start_app("com.thinkhome.v3")
sleep(5)

#登录18158288412
poco("android:id/tabs").child("android.widget.RelativeLayout")[0].click()

poco(text="能源").click()
if poco("com.thinkhome.v3:id/btn_setting").exists():
    poco("com.thinkhome.v3:id/btn_setting").click()
poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
sleep(5.0)
#能源设置
num=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
#电能设置状态为全不选
if num.split('/')[0] == "0":
    #全选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    
    sleep(5.0)
    #部分选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], str(int(message.split('/')[-1] )-1), "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
    #全不选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
#电能设置状态为全选
if num.split('/')[0] == num.split('/')[-1]:
    #部分选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], str(int(message.split('/')[-1] )-1), "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
    #全选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    
    #全不选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")

#电能设置状态为部分选
if (num.split('/')[0] != "0") & (num.split('/')[0] != num.split('/')[-1]):        
    #全选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    
    sleep(5.0)
    #部分选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], str(int(message.split('/')[-1])-1), "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
    #全不选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")

#数据清零
poco(text="数据清零").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco("android:id/button1").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据清零已成功", "数据清零验证通过")
except:
    print("Error")
else:
    print("Ok")
finally: 
    poco("android:id/button3").click()

#固定电价设置
#为空
poco(text="电价设置").click()
poco("com.thinkhome.v3:id/radio_static_price").click()
poco("com.thinkhome.v3:id/btn_rmb").click()
poco("com.thinkhome.v3:id/et_price").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "电价设置的值不能为空或者小于等于0的值", "固定电价为空验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#为0
poco("com.thinkhome.v3:id/et_price").set_text("0")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "请输入大于0的数字", "固定电价为0验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#包含中文，无法输入
#包含英文，无法输入

#过大
poco("com.thinkhome.v3:id/et_price").set_text("123456")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "电价设置值过大，请检查值是否正确", "固定电价过大验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#输入正确
poco("com.thinkhome.v3:id/et_price").set_text("3.4")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
if poco("com.thinkhome.v3:id/setting_price_setting").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text() != "峰谷电价":
    poco(text="电价设置").click()
    try:
        message=poco("com.thinkhome.v3:id/et_price").get_text()
        assert_equal(message, "3.4", "固定电价输入正确验证通过")
    except:
        print("Error")
    else:
        print("Ok")  
    finally:
        poco("com.thinkhome.v3:id/toolbar_btn_back").click()

    
#切换货币
poco(text="电价设置").click()
poco("com.thinkhome.v3:id/btn_euro").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco(text="电价设置").click()
try:
    message=poco("com.thinkhome.v3:id/tv_price_symbol").get_text()
    assert_equal(message, "€/kWh", "固定电价切换货币验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#峰谷电价设置
poco("com.thinkhome.v3:id/radio_dynamic_price").click()
while poco(text="删除").exists():
    poco(text="删除").click()
poco("com.thinkhome.v3:id/add_layout").click()
#为空
poco("com.thinkhome.v3:id/radio_dynamic_price").click()
poco("com.thinkhome.v3:id/btn_rmb").click()
poco("com.thinkhome.v3:id/et_price").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "电价设置的值不能为空或者小于等于0的值", "峰谷电价为空验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#为0
poco("com.thinkhome.v3:id/et_price").set_text("0")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "请输入大于0的数字", "峰谷电价为0验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#包含中文，无法输入
#包含英文，无法输入

#过大
poco("com.thinkhome.v3:id/et_price").set_text("123456")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "电价设置值过大，请检查值是否正确", "峰谷电价过大验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#区间错误
poco("com.thinkhome.v3:id/et_price").set_text("3.4")
poco("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text() != "00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text() != "12":
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message")
    assert_equal(message, "有时间段未设置电价，请填写完电价后再进行保存", "峰谷电价区间错误验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#输入正确
poco("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
if poco("com.thinkhome.v3:id/setting_price_setting").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()=="峰谷电价":
    poco(text="电价设置").click()
    try:
        message=poco("com.thinkhome.v3:id/et_price").get_text()
        assert_equal(message, "3.4", "峰谷电价输入正确验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    finally:
        poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#切换货币
poco(text="电价设置").click()
poco("com.thinkhome.v3:id/btn_euro").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco("com.thinkhome.v3:id/setting_price_setting").click()
try:
    message=poco("com.thinkhome.v3:id/tv_price_symbol").get_text()
    assert_equal(message, "€/kWh", "峰谷电价切换货币验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#添加电价区间
poco("com.thinkhome.v3:id/add_layout").click()
poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").set_text("0.28")

poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()

poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="08": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()

poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").click()
text("0.56")
poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="08": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()

poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00" : 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco(text="电价设置").click()
try:
    message=poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").get_text()
    assert_equal(message, "0.56", "添加电价区间验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#删除电价区间
poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tv_delete").click()
poco("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco(text="电价设置").click()
sleep(5.0)
if not poco(text="电价区间2").exists():
    try:
        message=poco("com.thinkhome.v3:id/et_price").get_text()
        assert_equal(message, "0.56", "删除电价区间验证通过")
    except:
        print("Error")
    else:
        print("Ok")
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
  
#图表

#楼层
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()
floor = ['G','-1F','-2F','-3F','-4F','-5F','不设楼层']
for i in range(1,101):
    floorName=str(i)+"F"
    floor.insert(i,floorName)
print(floor)
for i in floor:
    if poco(text=i).exists():
        poco(text=i).click()
        if poco(text="能源").exists():
            poco(text="能源").click()
            if poco("com.thinkhome.v3:id/btn_setting").exists():
                poco("com.thinkhome.v3:id/btn_setting").click()
            poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
            sleep(5.0)
            #能源设置
            num2=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
            #电能设置状态为全不选
            if num2.split('/')[0] == "0":
                #全选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

                #部分选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], str(int(message.split('/')[-1] )-1), "电能设置部分选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

                #全不选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

            #电能设置状态为全选
            if num2.split('/')[0] == num2.split('/')[-1]:
                #部分选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], str(int(message.split('/')[-1] )-1), "电能设置部分选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

                #全选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

                #全不选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

            #电能设置状态为部分选
            if (num2.split('/')[0] != "0") & (num2.split('/')[0] != num2.split('/')[-1]):        
                #全选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

                sleep(5.0)
                #部分选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], str(int(message.split('/')[-1])-1), "电能设置部分选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

                #全不选
                poco(text="电能设置").click()
                sleep(5.0)
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
                poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
                poco("com.thinkhome.v3:id/toolbar_right_text").click()
                if poco(text="密码").exists():
                    poco("com.thinkhome.v3:id/et_password").set_text("1234")
                try:
                    message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
                    assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")

            #数据清零
            poco(text="数据清零").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            poco("android:id/button1").click()
            try:
                message=poco("android:id/message").get_text()
                assert_equal(message, "数据清零已成功", "数据清零验证通过")
            except:
                print("Error")
            else:
                print("Ok")
            finally: 
                poco("android:id/button3").click()

            #固定电价设置
            #为空
            poco(text="电价设置").click()
            poco("com.thinkhome.v3:id/radio_static_price").click()
            poco("com.thinkhome.v3:id/btn_rmb").click()
            poco("com.thinkhome.v3:id/et_price").set_text("")
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            try:
                message=poco("android:id/message").get_text()
                assert_equal(message, "电价设置的值不能为空或者小于等于0的值", "固定电价为空验证通过")
            except:
                print("Error")
            else:
                print("Ok")
            finally:
                poco("android:id/button1").click()

            #为0
            poco("com.thinkhome.v3:id/et_price").set_text("0")
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            try:
                message=poco("android:id/message").get_text()
                assert_equal(message, "请输入大于0的数字", "固定电价为0验证通过")
            except:
                print("Error")
            else:
                print("Ok")
            finally:
                poco("android:id/button1").click()

            #包含中文，无法输入
            #包含英文，无法输入

            #过大
            poco("com.thinkhome.v3:id/et_price").set_text("123456")
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            try:
                message=poco("android:id/message").get_text()
                assert_equal(message, "电价设置值过大，请检查值是否正确", "固定电价过大验证通过")
            except:
                print("Error")
            else:
                print("Ok")
            finally:
                poco("android:id/button1").click()

            #输入正确
            poco("com.thinkhome.v3:id/et_price").set_text("3.4")
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            if poco("com.thinkhome.v3:id/setting_price_setting").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text() != "峰谷电价":
                poco(text="电价设置").click()
                try:
                    message=poco("com.thinkhome.v3:id/et_price").get_text()
                    assert_equal(message, "3.4", "固定电价输入正确验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")  
                finally:
                    poco("com.thinkhome.v3:id/toolbar_btn_back").click()


            #切换货币
            poco(text="电价设置").click()
            poco("com.thinkhome.v3:id/btn_euro").click()
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            poco(text="电价设置").click()
            try:
                message=poco("com.thinkhome.v3:id/tv_price_symbol").get_text()
                assert_equal(message, "€/kWh", "固定电价切换货币验证通过")
            except:
                print("Error")
            else:
                print("Ok")

            #峰谷电价设置
            poco("com.thinkhome.v3:id/radio_dynamic_price").click()
            while poco(text="删除").exists():
                poco(text="删除").click()
            poco("com.thinkhome.v3:id/add_layout").click()
            #为空
            poco("com.thinkhome.v3:id/radio_dynamic_price").click()
            poco("com.thinkhome.v3:id/btn_rmb").click()
            poco("com.thinkhome.v3:id/et_price").set_text("")
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            try:
                message=poco("android:id/message").get_text()
                assert_equal(message, "电价设置的值不能为空或者小于等于0的值", "峰谷电价为空验证通过")
            except:
                print("Error")
            else:
                print("Ok")
            finally:
                poco("android:id/button1").click()

            #为0
            poco("com.thinkhome.v3:id/et_price").set_text("0")
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            try:
                message=poco("android:id/message").get_text()
                assert_equal(message, "请输入大于0的数字", "峰谷电价为0验证通过")
            except:
                print("Error")
            else:
                print("Ok")
            finally:
                poco("android:id/button1").click()

            #包含中文，无法输入
            #包含英文，无法输入

            #过大
            poco("com.thinkhome.v3:id/et_price").set_text("123456")
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            try:
                message=poco("android:id/message").get_text()
                assert_equal(message, "电价设置值过大，请检查值是否正确", "峰谷电价过大验证通过")
            except:
                print("Error")
            else:
                print("Ok")
            finally:
                poco("android:id/button1").click()

            #区间错误
            poco("com.thinkhome.v3:id/et_price").set_text("3.4")
            poco("com.thinkhome.v3:id/tv_start_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text() != "00": 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
            poco("android:id/button1").click()
            poco("com.thinkhome.v3:id/tv_end_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text() != "12":
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
            poco("android:id/button1").click()
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            try:
                message=poco("android:id/message")
                assert_equal(message, "有时间段未设置电价，请填写完电价后再进行保存", "峰谷电价区间错误验证通过")
            except:
                print("Error")
            else:
                print("Ok")
            finally:
                poco("android:id/button1").click()

            #输入正确
            poco("com.thinkhome.v3:id/tv_start_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            else:
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            poco("android:id/button1").click()
            poco("com.thinkhome.v3:id/tv_end_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            else:
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            poco("android:id/button1").click()
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            if poco("com.thinkhome.v3:id/setting_price_setting").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()=="峰谷电价":
                poco(text="电价设置").click()
                try:
                    message=poco("com.thinkhome.v3:id/et_price").get_text()
                    assert_equal(message, "3.4", "峰谷电价输入正确验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")
                finally:
                    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

            #切换货币
            poco(text="电价设置").click()
            poco("com.thinkhome.v3:id/btn_euro").click()
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            poco("com.thinkhome.v3:id/setting_price_setting").click()
            try:
                message=poco("com.thinkhome.v3:id/tv_price_symbol").get_text()
                assert_equal(message, "€/kWh", "峰谷电价切换货币验证通过")
            except:
                print("Error")
            else:
                print("Ok")

            #添加电价区间
            poco("com.thinkhome.v3:id/add_layout").click()
            poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").set_text("0.28")

            poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_start_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            else:
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            poco("android:id/button1").click()

            poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_end_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="08": 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            else:
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            poco("android:id/button1").click()

            poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").click()
            text("0.56")
            poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_start_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="08": 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            else:
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            poco("android:id/button1").click()

            poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_end_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00" : 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            else:
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            poco("android:id/button1").click()
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            poco(text="电价设置").click()
            try:
                message=poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").get_text()
                assert_equal(message, "0.56", "添加电价区间验证通过")
            except:
                print("Error")
            else:
                print("Ok")

            #删除电价区间
            poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tv_delete").click()
            poco("com.thinkhome.v3:id/tv_start_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            else:
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            poco("android:id/button1").click()
            poco("com.thinkhome.v3:id/tv_end_time").click()
            while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
                poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            else:
                if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
                    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
            poco("android:id/button1").click()
            poco("com.thinkhome.v3:id/toolbar_right_text").click()
            if poco(text="密码").exists():
                poco("com.thinkhome.v3:id/et_password").set_text("1234")
            poco(text="电价设置").click()
            if not poco(text="电价区间2").exists():
                try:
                    message=poco("com.thinkhome.v3:id/et_price").get_text()
                    assert_equal(message, "0.56", "删除电价区间验证通过")
                except:
                    print("Error")
                else:
                    print("Ok")
            poco("com.thinkhome.v3:id/toolbar_btn_back").click()
            poco("com.thinkhome.v3:id/toolbar_btn_back").click()
            poco("com.thinkhome.v3:id/toolbar_btn_back").click()
        else:
            poco("com.thinkhome.v3:id/toolbar_btn_back").click()
            poco("com.thinkhome.v3:id/stickyListView").swipe("up")

#房间            
poco(text="网页版App勿删").click()
poco(text="能源").click()
if poco("com.thinkhome.v3:id/btn_setting").exists():
    poco("com.thinkhome.v3:id/btn_setting").click()
poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
sleep(5.0)
#能源设置
num3=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
#电能设置状态为全不选
if num3.split('/')[0] == "0":
    #全选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    
    #部分选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], str(int(message.split('/')[-1] )-1), "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
    #全不选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
#电能设置状态为全选
if num3.split('/')[0] == num3.split('/')[-1]:
    #部分选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], str(int(message.split('/')[-1] )-1), "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
    #全选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    
    #全不选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")

#电能设置状态为部分选
if (num3.split('/')[0] != "0") & (num3.split('/')[0] != num3.split('/')[-1]):        
    #全选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], message.split('/')[-1], "电能设置全选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    
    sleep(5.0)
    #部分选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], str(int(message.split('/')[-1])-1), "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")
        
    #全不选
    poco(text="电能设置").click()
    sleep(5.0)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[0].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco(text="密码").exists():
        poco("com.thinkhome.v3:id/et_password").set_text("1234")
    try:
        message=poco("com.thinkhome.v3:id/setting_device").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
        assert_equal(message.split('/')[0], "0", "电能设置部分选验证通过")
    except:
        print("Error")
    else:
        print("Ok")

#数据清零
poco(text="数据清零").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco("android:id/button1").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据清零已成功", "数据清零验证通过")
except:
    print("Error")
else:
    print("Ok")
finally: 
    poco("android:id/button3").click()

#固定电价设置
#为空
poco(text="电价设置").click()
poco("com.thinkhome.v3:id/radio_static_price").click()
poco("com.thinkhome.v3:id/btn_rmb").click()
poco("com.thinkhome.v3:id/et_price").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "电价设置的值不能为空或者小于等于0的值", "固定电价为空验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#为0
poco("com.thinkhome.v3:id/et_price").set_text("0")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "请输入大于0的数字", "固定电价为0验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#包含中文，无法输入
#包含英文，无法输入

#过大
poco("com.thinkhome.v3:id/et_price").set_text("123456")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "电价设置值过大，请检查值是否正确", "固定电价过大验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#输入正确
poco("com.thinkhome.v3:id/et_price").set_text("3.4")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
if poco("com.thinkhome.v3:id/setting_price_setting").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text() != "峰谷电价":
    poco(text="电价设置").click()
    try:
        message=poco("com.thinkhome.v3:id/et_price").get_text()
        assert_equal(message, "3.4", "固定电价输入正确验证通过")
    except:
        print("Error")
    else:
        print("Ok")  
    finally:
        poco("com.thinkhome.v3:id/toolbar_btn_back").click()

    
#切换货币
poco(text="电价设置").click()
poco("com.thinkhome.v3:id/btn_euro").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco(text="电价设置").click()
try:
    message=poco("com.thinkhome.v3:id/tv_price_symbol").get_text()
    assert_equal(message, "€/kWh", "固定电价切换货币验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#峰谷电价设置
poco("com.thinkhome.v3:id/radio_dynamic_price").click()
while poco(text="删除").exists():
    poco(text="删除").click()
poco("com.thinkhome.v3:id/add_layout").click()
#为空
poco("com.thinkhome.v3:id/radio_dynamic_price").click()
poco("com.thinkhome.v3:id/btn_rmb").click()
poco("com.thinkhome.v3:id/et_price").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "电价设置的值不能为空或者小于等于0的值", "峰谷电价为空验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#为0
poco("com.thinkhome.v3:id/et_price").set_text("0")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "请输入大于0的数字", "峰谷电价为0验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#包含中文，无法输入
#包含英文，无法输入

#过大
poco("com.thinkhome.v3:id/et_price").set_text("123456")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "电价设置值过大，请检查值是否正确", "峰谷电价过大验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#区间错误
poco("com.thinkhome.v3:id/et_price").set_text("3.4")
poco("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text() != "00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text() != "12":
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
try:
    message=poco("android:id/message")
    assert_equal(message, "有时间段未设置电价，请填写完电价后再进行保存", "峰谷电价区间错误验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button1").click()

#输入正确
poco("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
if poco("com.thinkhome.v3:id/setting_price_setting").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()=="峰谷电价":
    poco(text="电价设置").click()
    try:
        message=poco("com.thinkhome.v3:id/et_price").get_text()
        assert_equal(message, "3.4", "峰谷电价输入正确验证通过")
    except:
        print("Error")
    else:
        print("Ok")
    finally:
        poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#切换货币
poco(text="电价设置").click()
poco("com.thinkhome.v3:id/btn_euro").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco("com.thinkhome.v3:id/setting_price_setting").click()
try:
    message=poco("com.thinkhome.v3:id/tv_price_symbol").get_text()
    assert_equal(message, "€/kWh", "峰谷电价切换货币验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#添加电价区间
poco("com.thinkhome.v3:id/add_layout").click()
poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").set_text("0.28")

poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()

poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="08": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()

poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").click()
text("0.56")
poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="08": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()

poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00" : 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco(text="电价设置").click()
try:
    message=poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[1].child("com.thinkhome.v3:id/price_layout").child("com.thinkhome.v3:id/et_price").get_text()
    assert_equal(message, "0.56", "添加电价区间验证通过")
except:
    print("Error")
else:
    print("Ok")
    
#删除电价区间
poco("com.thinkhome.v3:id/prices").child("com.thinkhome.v3:id/linear_layout")[0].child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tv_delete").click()
poco("com.thinkhome.v3:id/tv_start_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/tv_end_time").click()
while poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].child("android:id/numberpicker_input").get_text()!="00": 
    poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[0].swipe("up")
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
else:
    if poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android:id/numberpicker_input").get_text()!="00":
        poco("android:id/timePickerLayout").child("android.widget.LinearLayout").child("android.widget.NumberPicker")[1].child("android.widget.Button").click()
poco("android:id/button1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco(text="电价设置").click()
sleep(5.0)
if not poco(text="电价区间2").exists():
    try:
        message=poco("com.thinkhome.v3:id/et_price").get_text()
        assert_equal(message, "0.56", "删除电价区间验证通过")
    except:
        print("Error")
    else:
        print("Ok")
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
  
