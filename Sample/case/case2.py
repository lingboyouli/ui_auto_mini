# 1.导入appium和TouchAction
import time
from appium import webdriver


# 2.创建Desired capabilities对象，添加启动参数
desired_caps = {
    "platformName": "Android",  # 系统名称
    # "platformVersion": "7.1.2",  # 系统版本
    "deviceName": "UMX0221928008013",  # 设备名称
    "appPackage": "com.tencent.mm",  # APP包名
    "appActivity": ".ui.LauncherUI",  # APP启动名
    "noReset": True,  # 表示不重置应用
    "chromeOptions": {"androidprocess": "com.tencent.mm:appbrand0"}
}

# 3.启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)

# 4.操作APP
# 点击发现
driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
# 点击小程序
driver.find_element_by_android_uiautomator('new UiSelector().text("小程序")').click()
# 点击ofo小黄车官方版,进入小程序
driver.wait_activity("/.plugin.appbrand.ui.AppBrandLauncherUI", 10)
# time.sleep(3)
driver.find_element_by_android_uiautomator('new UiSelector().text("ofo小黄车官方版")').click()
# driver.find_element_by_xpath("//*[@text='ofo小黄车官方版']").click()

# 接下来就是操作微信小程序，和以前的操作一样。
# 都是一步一步定位，一步一步操作。

# 5.关闭APP
time.sleep(3)
driver.quit()
