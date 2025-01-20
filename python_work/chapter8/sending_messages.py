def send_messages(messages):
    sent_messages = []

    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)

    print(f"messages: {messages}")
    print(f"sent_messages: {sent_messages}")

messages = ['Hi!', 'Hello.', 'How are you?', 'Never been better!']

send_messages(messages)