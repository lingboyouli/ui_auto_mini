import time
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",  # 系统名称
    # "platformVersion": "7.1.2",  # 系统版本
    "deviceName": "UMX0221928008013",  # 设备名称
    "appPackage": "com.tencent.mm",  # APP包名
    "appActivity": ".ui.LauncherUI",  # APP启动名
    "noReset": True,  # 表示不重置应用
    "chromeOptions": {"androidprocess": "com.tencent.mm:appbrand2"}
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)

window = driver.get_window_size()
x1 = window['width'] * 0.5  # 起始x坐标
y1 = window['height'] * 0.2  # y1坐标，滑动起始点
y2 = window['height'] * 0.7  # y2坐标，滑动末尾点
driver.swipe(x1, y1, x1, y2, 500)  # 页面下拉
time.sleep(2)

driver.find_element(By.ID, 'com.tencent.mm:id/f1r').click()  # 点击‘快看漫画mini’

