# 文字類型 Action

```python
msg = TemplateSendMessage(
    alt_text='Actions',
    template=ButtonsTemplate(
        title='Menu',
        text='Please Click',
        actions=[
            MessageAction(
                label='message',
                text='message text'
            )
        ]
    )
)
```

# 文件導讀
https://developers.line.biz/en/reference/messaging-api/#message-action