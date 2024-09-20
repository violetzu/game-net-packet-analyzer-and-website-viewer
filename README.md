
網站網址 https://ranking.marimo.idv.tw/  

首先由wireshark截取各區的排行榜數據

```wireshark rawdata/```是wireshark導出的json檔的存放路徑

```main.py``` 將取得的資料整理後輸出分別依照關卡及戰力排序的兩個檔案 `date_main.json` 及 `date_power.json`

最後由`index.html`顯示
