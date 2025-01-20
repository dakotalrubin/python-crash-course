def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        sent_messages.append(message)
        print(message)

messages = ['Hi!', 'Hello.', 'How are you?', 'Never been better!']
sent_messages = []

send_messages(messages[:], sent_messages)

print(f"messages: {messages}")
print(f"sent_messages: {sent_messages}")