import argparse
import markdown

def convert_to_html(input_file, output_file):
    with open(input_file) as f:
        contents = f.read()

    # HTML変換時にテーブルと番号付きリストの処理を有効にするために、拡張機能を指定
    extensions = ["markdown.extensions.extra", "markdown.extensions.tables"]
    html_content = markdown.markdown(contents, extensions=extensions)

    with open(output_file, "w") as f:
        f.write(html_content)
    print("Markdown to HTML conversion done.")

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML.')
    parser.add_argument('mode', metavar='mode', type=str, help='Markdown to HTML conversion mode')
    parser.add_argument('input_file', metavar='input_file', type=str, help='Input Markdown file')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output HTML file')
    args = parser.parse_args()
    
    if args.mode != "markdown" or not args.input_file.endswith(".md") or not args.output_file.endswith(".html"):
        print("Error: Invalid input/output file format. Both files must have .md and .html extensions respectively.")
        return

    convert_to_html(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
