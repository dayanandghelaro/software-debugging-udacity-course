html_text = """
    <h1> Hello, World! </h1>
"""
def extract_text(html_text):
    tag_mode = False
    text = ""
    for char in html_text:
        if char == "<":
            tag_mode = True
        elif char == ">":
            tag_mode = False
        elif not tag_mode:
            text += char
    return text


print(extract_text(html_text))

