# 網頁公告自動爬蟲寄信

## 在 Windows 開機時自動執行

- 按 Win + R 打開「執行」對話框，輸入 taskschd.msc 並按下 Enter，打開「排程任務程式」。
- 在「排程任務程式」中，選擇「建立基本任務」。
- 在「建立基本任務嚮導」中，輸入任務名稱和描述，然後點擊「下一步」。
- 選擇「當我登入時」或「當電腦啟動時」，然後點擊「下一步」。
- 選擇「啟動程式」，然後點擊「下一步」。
- 點擊「瀏覽」，選擇 autostart.vbs，然後點擊「下一步」。
- 點擊「完成」來建立任務。

## vbs

``` vb
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Users\...\autostart.bat" & chr(34), 0
Set WshShell = Nothing
```

## bat

``` bat
@echo off
cd C:\Users\...\autostart
python index.py
```
