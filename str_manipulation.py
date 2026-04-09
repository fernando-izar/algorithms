def justify_words(words: list, width: int) -> list:
    # check if words is empty
    if not words:
        return []
    length = len(words)

    res = []
    tmp_str = ""

    for w in words:
        if len(w) + len(tmp_str) > width:
            if len(tmp_str.strip()) < width:
                # justify the string
                line = justify_str(tmp_str.strip().split(), width, False)
                res.append(line)
            else:
                res.append(tmp_str.strip())
            tmp_str = w + " "

        else:
            tmp_str = tmp_str + w + " "

    if tmp_str:
        if len(tmp_str.strip()) < width:
            # justify the sring
            line = justify_str(tmp_str.strip().split(), width, True)
            res.append(line)
        else:
            res.append(tmp_str.strip())
    return res


def justify_str(line_words: list[str], width: int, is_last: bool) -> str:
    n_words = len(line_words)
    if is_last or n_words == 1:
        return " ".join(line_words).ljust(width)

    n_gaps = n_words - 1
    spaces = (width - len("".join(line_words).strip())) // n_gaps
    extra_spaces_n_gaps = (width - len("".join(line_words).strip())) % n_gaps

    # spaces_list = []
    tmp_str = ""

    for n in range(n_gaps + 1):
        tmp_space = " " * spaces if n + 1 > extra_spaces_n_gaps else " " * spaces + " "
        tmp_str = tmp_str + line_words[n] + tmp_space

    return tmp_str.strip()


words = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer,",
    "art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
max_width = 20

print(justify_words(words, max_width))
