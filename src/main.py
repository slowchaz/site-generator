from inline_markdown import extract_markdown_images, extract_markdown_links

def main():
    print("main")

    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text))

    print("complete")


main()
