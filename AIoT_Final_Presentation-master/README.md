# AIoT 期末報告
## 說明
- dataset\solar_data_202003_202007.csv 為 **新竹市北區海濱路240號** 新竹市環保局掩埋場復育地太陽能案場在 **3月至7月** 其中一個inverter(逆變器)的太陽能發電資料

將資料集(dataset)內的 solar_data_202003_202007.csv 的太陽能案場發電資料做為訓練資料集訓練你的預測模型，用機器學習及深度學習皆可，預測 2020年一月、二月、八月、九月、十月的 **"每小時"發電度數** 。

訓練完後需將模型做成 restful API 按照以下格式接收並回傳資料，restful API 需開啟對外連線的功能，可自行架設或直接使用 ngrok。
### ngrok 使用方式
- /ngrok 資料夾底下找相對應的 ngrok壓縮包解壓縮即可
- 若無您的版本，可至 [https://ngrok.com/download](https://ngrok.com/download) 下載
- 解壓縮完後 cd 至 ngrok 主程式資料夾底下
- 使用以下指令執行 ngrok 主程式，預設綁定 flask 預設 port(5000)
```
windows: 
>> ngrok.exe http 5000

mac:
>> ./ngrok http 5000
```
- 執行後即可取得 https 加密的 dns
![image](https://github.com/cheap122000/AIoT_Final_Presentation/blob/master/ngrok/ngrok_capture.PNG)
- 在 dns 後加上你的 api url 即可

&nbsp;
### [作業網址: http://aiotfinal.ddns.net:8000/ ](http://aiotfinal.ddns.net:8000/)
### 登入帳號為
- 大同大學： ttu + 學號
- 臺科大： ntust + 學號

&nbsp;

### 範例： 輸入 JSON 格式

```
{
    "columns": ["YEAR", "MONTH", "DAY", "HOUR", "OPTPWR", "ACV1", "ACV2", "ACCL1", "ACCL2", "ACF1", "IIT", "IHT", "DCVL1", "DCVL2", "IPA", "IPB"],
    "questions": [
        [2020, 10, 6, 15, 13.52, 230, 226, 20.1, 19.3, 60.1, 41, 42, 749, 750, 6.73, 6.81],
        [2020, 1, 25, 12, 3.91, 229, 226, 6.2, 5.6, 60.1, 36, 39, 770, 770, 1.93, 2.01],
        [2020, 10, 19, 12, 24.94, 233, 230, 36.0, 36.2, 60.5, 44, 49, 754, 738, 12.44, 12.52]
    ]
}
```

### 備註：
- columns 為欄位名稱
- questions 為需要預測之資料(每次筆數不會固定)

&nbsp;

### 範例： 回傳 JSON 格式

```
{
    "predictions": [1.0, 2.0, 3.0] 
}
```

### 備註：
- 回傳的 predictions 帶入模型後回傳的資料

&nbsp;
### 注意 
- 回傳的 **"predictions 的長度"** 要與 **"輸入的 questions 長度"** 相同

&nbsp;

## 上傳作業前請先確認格式是否正確
以下為測試方法
- 打開 test.py
- 將程式碼第六行 <Your restful api url> 取代成你的 api url
```
6.  url = '<Your restful api url>' # 取代成你的 api url
```
- 執行程式
```
>> python test.py
```
- 如果看到 **"基礎測試完成，可以教作業了"** 就可以教作業了

### 程式碼僅供基礎測試，若繳交作業失敗仍找不出原因，請 email 給老師
老師 Email: weikai.chen@tatung.com

&nbsp;

## 期末分數
### 實作(70%)
- 取最高的 R<sup>2</sup> score * 100
- R<sup>2</sup> score 低於 0 分時以 0 分計算

### 報告(30%)
- 每組 1-3 人
- 每組報告 5 - 10 分鐘
- 報告 Outlines
    - 組員及分工
    - 資料處理方式
    - 使用的訓練模型 (成功做出兩個或以上模型會加分，有機器學習與深度學習的比較更佳)
    - 最高分數 與 分析模型優點 (or 多個模型間的互相比較)
    - 過程中遇到的困難及如何解決 or 心得 or 這學期上課的收穫
    - 課程建議 (如果沒有建議可以不用)

### 報告順序
將在 12/30(三) 上課時抽出