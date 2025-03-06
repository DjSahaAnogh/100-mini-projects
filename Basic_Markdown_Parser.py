import re
def md_to_text(user_input: str) -> str:
    user_input = re.sub(r"#+\s+", " ", user_input)
    user_input = re.sub(r"\*\*(.*?)\*\*", r"\1", user_input)
    user_input = re.sub(r"\*(.*?)\*", r"\1", user_input)
    user_input = re.sub(r"~~(.*?)~~", r"\1", user_input)
    user_input = re.sub(r"^>+\s?", " ", user_input, flags=re.MULTILINE)
    user_input = re.sub(r"^- (.*?)$", r"\1", user_input, flags=re.MULTILINE)
    user_input = re.sub(r"```(.*?)```", r"\1", user_input)
    user_input = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", user_input)
    return user_input.strip()

if __name__ == "__main__":
    x: str = """
# Heading 1
## Heading 2
**Bold text** and *italic text*.
> This is a blockquote.
- List item 1
- List item 2
[Link text](https://example.com)
"""
    print(md_to_text(x))