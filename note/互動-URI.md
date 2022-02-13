# 網址類型 Action

```python
msg = TemplateSendMessage(
    alt_text='Actions',
    template=ButtonsTemplate(
        title='Menu',
        text='Please Click',
        actions=[
            URIAction(
                    label='google',
                    uri='https://www.google.com.tw/'
            )
        ]
    )
)
```

> 用手機瀏覽器開
```
https://www.google.com.tw?openExternalBrowser=1
```


# 文件導讀
https://developers.line.biz/en/reference/messaging-api/#uri-action