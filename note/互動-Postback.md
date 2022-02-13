# Postback類型 Action

```python
msg = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='Menu',
            text='Please Click',
            actions=[
                PostbackAction(label="test", data="1")
            ]
        )
)
```

# 文件導讀
https://developers.line.biz/en/reference/messaging-api/#uri-action