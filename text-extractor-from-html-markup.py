html_text = """
    <h1> Hello, World! </h1>
    <a href= ">"> Hello, World! </a>
"""
def extract_text(html_text):
    tag_mode = False
    quote_mode = False
    text = ""
    for char in html_text:
        if not tag_mode and char == "<":
            tag_mode = True
        elif char == "\"":
            quote_mode = not quote_mode
        elif not quote_mode and char == ">":
            tag_mode = False
        elif not tag_mode and not quote_mode:
            text += char
    return text


print(extract_text(html_text))

