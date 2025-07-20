def classify_image(metadata, agent):
    text = metadata.get("text", "").lower()
    filename = metadata.get("filename", "").lower()
    faces = metadata.get("faces", 0)

    junk_filename_keywords = ["trash", "junk", "meme", "ad"]
    if any(keyword in filename for keyword in junk_filename_keywords):
        return "Advertisement/Junk"

    work_filename_keywords = [
        "work", "invoice", "project", "report", "contract", "proposal",
        "budget", "memo", "doc", "financial", "business", "meeting", "task",
        "client", "statement", "plan", "brief", "agenda", "minutes", "tender",
        "payroll", "hr", "legal", "policy", "accounts"
    ]
    if any(keyword in filename for keyword in work_filename_keywords):
        return "Work-related"

    informational_filename_keywords = [
        "informational", "news", "article", "report", "journal", "study",
        "analysis", "guide", "manual", "data", "summary", "facts", "research"
    ]
    if any(keyword in filename for keyword in informational_filename_keywords):
        return "Informational"

    if faces > 0:
        return "Personal/memory"

    junk_text_keywords_fallback = [
        "sale", "discount", "offer", "promo", "free", "winner",
        "lottery", "coupon", "spam", "advertisement", "deal", "limited time",
        "click here", "subscribe now", "buy now", "unclaimed prize", "guaranteed",
        "exclusive offer", "download now", "viral", "shocking", "you won",
        "congratulations", "act fast", "final chance", "clickbait", "giveaway"
    ]
    if any(keyword in text for keyword in junk_text_keywords_fallback):
        return "Advertisement/Junk"

    return "Advertisement/Junk"