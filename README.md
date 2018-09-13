# 一、Main Install 


## 1. Visual Studio Code
    https://code.visualstudio.com/ (一鍵安裝)
## 2. PYTHON (MAC預設2.7不用另外安裝)
- get python path
      $ which python 
## 3. pip
****    $ easy_install pip
## 4. Unit Test 
- unittest 
      $ pip install unittest
- install pytest
      $ sudo pip2.7 install pytest 
## 5. Jupyter

透過網頁介面，你可以將程式碼寫在不同的 Cell (區塊) 之中，並且分段落執行[@](https://jerrynest.io/install-jupyter-with-style/)

- install **Jupyter** Notebook
      $ pip3 install jupyter
      $ jupyter notebook
- http://localhost:8888/tree#notebooks
## 6. SELENIUM
- install **selenium**
      $ pip2.7 install selenium

=========================================================================

# 二、WEB測試
## 1. Driver Install
- 依照chrome版本安裝 **chromedriver**
    https://sites.google.com/a/chromium.org/chromedriver/downloads v2.33
    $ unzip chromedriver_mac32.zip -d /usr/local/bin/

=========================================================================

# 三、手機測試-APPIUM
## 1. APPIUM
- Install **npm**
      $ brew install npm
- install **appium**
      $ npm install -g appium
      $ npm install wd
      $ pip2.7 install Appium-Python-Client
- Install **Appium-desktop**
      Appium 官網 download 
- **appium-doctor** 檢查安裝有無error
      $ npm install appium-doctor -g 
      $ appium-doctor
- appium **port**
      http://localhost:4723/wd/hub/status


## 2. 手機測試依賴包
- install **node.js**
    $ brew install node

=========================================================================

# 四、IOS手機測試安裝
## 1. Install
****- Install **Xcode** on Apple store
      $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)".   
- Install **libimobiledevice** (连接iPhone/iPod Touch等iOS设备)
      $ brew install libimobiledevice --HEAD
- Install **ios-deploy**  (iOS10以上的系统才需要安装)
      $ npm install -g ios-deploy  
- install **Homebrew**  
      $ brew doctorbrew install libimobiledevice --HEAD  
- Install **Carthage**
      $ brew install carthage

=========================================================================

# 五、IOS 實體機
## 1. Driver Install

**應用程式憑證簽署** (安裝到ios實機上需要證書簽名)

- install **WebDriverAgent** (安裝憑證取得手機控制權)
          $ git clone https://github.com/facebook/WebDriverAgent.git
          $ cd WebDriverAgent
          $ mkdir -p Resources/WebDriverAgent.bundle
          $ sh ./Scripts/bootstrap.sh -d
          $ cd  /usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent
          $ open WebDriverAgent.xcodeproj
- **WebDriverAgentLib** 和 **WebDriverAgentRunner**，勾選“Automatically manage signing”，把Team改成自己的apple帳號來配置證書，點上方budil setting頁籤，Bundle Identifier改一個名字 [@教學](https://blog.csdn.net/yxys01/article/details/78293983)
![](http://www.7forz.com/wp-content/uploads/2017/05/xcode-config-800x329.png)

- **WebDriverAgentRunner** 裡的 framework 裡需要用到 Carthage 裡的一個包 , 如果沒有請在Carthage目錄下去找到 .framework 檔自行加入
![1](http://image.mamicode.com/info/201802/20180213131604414558.png)

- 把 **WebDriverAgentLib** 和 **WebDriverAgentRunner** 點上方執行箭頭, 或是点击 `Product->Test` , 兩個都編譯到真機運行一下了 , 或下指令
      $ cd  /usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent
      $ idevice_id -l      #查iOS的udid
      $ xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id={udid}' test
- 成功後會在手機桌面生成一個沒圖標的 **WebDriverAgentRunner**
- 運行成功後，在 Xcode 控制台印出一個 Ip 地址和 port 號
![](https://upload-images.jianshu.io/upload_images/1925310-edee15b71e9a2229.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)



## 2. 抓元素工具

**Macaca App Inspector**  (類似Appium Desktop抓元素工具,但xpath較完整)

- install **macaca-cli**
      $ npm install macaca-cli -g 
      $ macaca doctor
- install **app-inspector**
      $ npm install app-inspector -g
      $ app-inspector -u {udid} --verbose       #啟用,需填寫udid
- 會自動開啟**手機預覽網頁**,就可開始抓元素了
- 如果顯示 “Error: connect ECONNREFUSED 127.0.0.1:8001”
      $ cd /usr/local/lib/node_modules/app-inspector/node_modules/xctestwd/XCTestWD/
      $ xcodebuild -project XCTestWD.xcodeproj -scheme XCTestWDUITests -destination 'platform=iOS,id={udid}' XCTESTWD_PORT=8001 clean test


## 3. 執行自動化測試
- 啟動 **WebDriverAgent**
- 啟動 **appium** 
      $ appium -U {UUID} --app {bundleID}      #bundleID=com.telenavsoftware.doudouy
  


=========================================================================

# 六、IOS 虛擬機  
## 1. Driver Install
1. ios devices **path**
      ~/Library/Developer/CoreSimulator/Devices/70402A48-1C20-4496-B7D5-25CFB70BB844/data/
      <待補>



參考資料：
使用Appium进行iOS的真机自动化测试 [@](https://www.jianshu.com/p/ae8846736dba)
Appium+XCUITest基于Python的操作实例以及环境搭建 [@](https://my.oschina.net/u/2291665/blog/858538)
=========================================================================

# 七、android手機測試安裝

<待補>

=========================================================================

# 八、android 實體機
## 1. Driver Install
- 電腦端要安裝手機的驅動程式，HTC 手機請安裝 **HTC Sync**，MOTO 手機請安裝 Motorola USB drivers，Samsung 手機請安裝 Kies。
- 手機端要開啟「**USB除錯**」，進入手機設定>應用程式>開發>勾選USB除錯
- 查看手機裝置是否有順利連接
      $ adb devices
- get **log**
      $ adb logcat -v time > a.txt

<待補>

=========================================================================

# 九、android 虛擬機  
## 1. Driver Install
- install **android-studio**
      $ brew cask install android-studio

<待補>

SDK Folder: 

    /Users/cleo/Library/Android/sdk
    /Users/cleo/Library/Android/sdk/tools/bin/uiautomatorviewer

java_home 環境變數

    $(/usr/libexec/java_home)
    source ~/.bash_profile


