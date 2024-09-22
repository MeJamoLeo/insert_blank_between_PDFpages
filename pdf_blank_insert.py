import argparse
from PyPDF2 import PdfReader, PdfWriter, PageObject

def insert_blank_pages(input_path, output_path):
    # PDFリーダーとライターを作成
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # 各ページに対して処理
    for page in reader.pages:
        # 元のページを追加
        writer.add_page(page)
        
        # 同じサイズの空白ページを作成して追加
        width = page.mediabox.width
        height = page.mediabox.height
        blank_page = PageObject.create_blank_page(width=width, height=height)
        writer.add_page(blank_page)

    # 出力ファイルに書き込み
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"{output_path} にオリジナルと空白ページが交互に追加されました。")

def main():
    # コマンドライン引数のパーサーを作成
    parser = argparse.ArgumentParser(description="PDFの各ページの間に空白ページを追加するスクリプト")
    parser.add_argument("input_path", help="入力PDFファイルのパス")
    parser.add_argument("output_path", help="出力PDFファイルのパス")

    # 引数を解析
    args = parser.parse_args()

    # 空白ページの挿入処理を実行
    insert_blank_pages(args.input_path, args.output_path)

if __name__ == "__main__":
    main()
