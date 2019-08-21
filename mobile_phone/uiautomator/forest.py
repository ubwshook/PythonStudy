import uiautomator2 as u2
import time


def get_energy(d):
    for i in range(1, 7):
        try:
            d.xpath('//*[@resource-id="J_barrier_free"]/android.widget.Button[{}]'.format(i)).click()
            time.sleep(2)
            if d.exists(scrollable=False, text="进入地图"):
                d.press("back")
                break
            #time.sleep(2)
        except:
            pass

    d.press("back")
    time.sleep(2)


def swipe_energy(d, batch):
    if batch != 0:
        d.swipe(0.494, 0.800, 0.523, 0.370)
        if d.exists(scrollable=False, text="没有更多了"):
            return

    for i in range(batch * 6 + 1, (batch + 1) * 6 + 1):
        if i == 16:
            continue
        try:
            d.xpath('//*[@resource-id="J_rank_list_append"]/android.view.View[{}]'.format(i)).click()
            time.sleep(3)
            if d.exists(scrollable=False, text="返回我的森林"):
                d.press("back")
            get_energy(d)
        except:
            pass


def get_all_forest(d):
    # 启动App
    d.screen_on()
    d.swipe(0.494, 0.800, 0.523, 0.370)
    d.app_start("com.eg.android.AlipayGphone")
    time.sleep(5)
    d.xpath('//*[@text="蚂蚁森林"]').click()
    time.sleep(5)
    d.click(0.462, 0.327)
    time.sleep(1)
    d.click(0.317, 0.335)
    time.sleep(1)
    d.click(0.637, 0.339)
    time.sleep(1)
    d.click(0.545, 0.417)
    time.sleep(2)
    d.swipe(0.387, 0.648, 0.471, 0.197)
    time.sleep(2)
    d.swipe(0.387, 0.648, 0.471, 0.197)
    time.sleep(2)
    d.swipe(0.387, 0.648, 0.471, 0.197)
    time.sleep(2)
    d(text="查看更多好友").click()
    time.sleep(5)
    swipe_energy(d, 0)
    swipe_energy(d, 1)
    swipe_energy(d, 2)
    swipe_energy(d, 3)
    swipe_energy(d, 4)
    swipe_energy(d, 5)
    swipe_energy(d, 6)
    swipe_energy(d, 7)
    swipe_energy(d, 8)
    d.app_stop_all()


# d = u2.connect('192.168.3.14')
while True:
    d = u2.connect_usb()
    print(d.info)
    get_all_forest(d)
    time.sleep(60)



