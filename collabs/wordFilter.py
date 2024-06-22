
BAD_WORDS = [
    "fuck", "ass", "nigger", "shit",
    "arse", "bith", "cock", "cunt", 
    "dick", "nigga", "nigra", "pussy",
    "slut", "twat", "whore", "scheiße",
    "arschloch", "fotze", "hurensohn",
    "wichser", "missgeburt", "dummkopf",
    "kanake", " drecksau", "schwuchtel",
    "kurwa", "dziwka", "suka", "chuj",
    "cwel", "debil", "jebać", "jebany",
    "jebana", "jebac", "ćipa", "cipa",
    "putain", "merde", "connard", "connasse",
    "con", "dégage", "gueule", "salope", 
    "salaud", "bâtard", "bâtarde",
    "niquer", "rape", "zgwałce", "zajebie",
    "zut", "pute", "puto", "retard", "mongol",
    "mongolic", "joder", "gilipollas", "mierda",
    "qué cabrón", "la concha de tu madre", "bould",
    "coño", "carjo", "puta", "conchesumare", 
    "baldracca", "bastardo", "cagare", "blowjob", "bocchino",
    "cazzo", "cazz", "coglione", "coglio", "cornuto",
    "culo", "fava", "fica", "figa", "frocio", "gnocca", "merda",
    "minchia", "mona", "puttana", "ricchione", "stronzo", "troia",
    "vaffanculio", "zoccola", "faggot", "fagot",
    ]  # Add your list of bad words here

def filter_bad_words(text):
    lower_text = text.lower()
    for bad_word in BAD_WORDS:
        lower_text = lower_text.replace(bad_word, "*" * len(bad_word))
    result_text = ""
    for original, lower in zip(text, lower_text):
        result_text += "*" if lower == "*" else original
    return result_text