def generate_reply(intenet,sender_name):
    responses={
        "Query": f"Hi {sender_name},\nThanks for reaching out. I'll get back to you shortly with the details.",
        "Complaint": f"Hi {sender_name},\nI’m sorry to hear that. I’ll investigate the issue and follow up.",
        "Meeting Request": f"Hi {sender_name},\nI’m available this week. Please suggest a time that works for you.",
        "Spam": None,
        "Other": f"Hi {sender_name},\nThank you for your message. I’ll review and respond soon."
    }
    return responses.get(intent)