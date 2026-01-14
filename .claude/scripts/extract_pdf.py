#!/usr/bin/env python3
"""
PDF 文字提取腳本
用於處理 Claude Code 無法直接讀取的大型 PDF

使用方式：
    python extract_pdf.py <pdf_path> [--output <output_dir>] [--pages <start>-<end>]

範例：
    python extract_pdf.py paper.pdf
    python extract_pdf.py paper.pdf --output .temp/pdf_extracted/
    python extract_pdf.py paper.pdf --pages 1-10
"""

import sys
import os
import argparse

try:
    import fitz  # PyMuPDF
except ImportError:
    print("請先安裝 PyMuPDF: pip install pymupdf")
    sys.exit(1)


def extract_pdf(pdf_path, output_dir=None, page_range=None):
    """
    提取 PDF 文字內容

    Args:
        pdf_path: PDF 檔案路徑
        output_dir: 輸出目錄（預設：.temp/pdf_extracted/）
        page_range: 頁面範圍，格式 "start-end"（預設：全部）

    Returns:
        輸出檔案路徑
    """
    if not os.path.exists(pdf_path):
        print(f"錯誤：找不到檔案 {pdf_path}")
        sys.exit(1)

    # 設定輸出目錄
    if output_dir is None:
        output_dir = ".temp/pdf_extracted/"
    os.makedirs(output_dir, exist_ok=True)

    # 開啟 PDF
    doc = fitz.open(pdf_path)
    total_pages = len(doc)

    # 解析頁面範圍
    start_page = 0
    end_page = total_pages
    if page_range:
        try:
            parts = page_range.split("-")
            start_page = int(parts[0]) - 1  # 轉為 0-indexed
            end_page = int(parts[1]) if len(parts) > 1 else start_page + 1
        except (ValueError, IndexError):
            print(f"警告：無效的頁面範圍 '{page_range}'，將提取全部頁面")
            start_page = 0
            end_page = total_pages

    # 確保範圍有效
    start_page = max(0, min(start_page, total_pages - 1))
    end_page = max(start_page + 1, min(end_page, total_pages))

    # 提取文字
    text_parts = []
    for i in range(start_page, end_page):
        page_text = doc[i].get_text()
        text_parts.append(f"=== 第 {i + 1} 頁 / 共 {total_pages} 頁 ===\n{page_text}")

    text = "\n\n".join(text_parts)
    doc.close()

    # 生成輸出檔名
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    if page_range:
        output_file = f"{output_dir}/{base_name}_p{start_page + 1}-{end_page}.txt"
    else:
        output_file = f"{output_dir}/{base_name}_extracted.txt"

    # 寫入檔案
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"提取完成：{output_file}")
    print(f"頁面範圍：{start_page + 1} - {end_page} / {total_pages}")
    print(f"檔案大小：{os.path.getsize(output_file) / 1024:.1f} KB")

    return output_file


def split_pdf(pdf_path, output_dir=None, pages_per_chunk=20):
    """
    將大型 PDF 分割成多個文字檔

    Args:
        pdf_path: PDF 檔案路徑
        output_dir: 輸出目錄
        pages_per_chunk: 每個檔案的頁數
    """
    if output_dir is None:
        output_dir = ".temp/pdf_extracted/"
    os.makedirs(output_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    output_files = []
    for start in range(0, total_pages, pages_per_chunk):
        end = min(start + pages_per_chunk, total_pages)
        text = "\n\n".join(
            f"=== 第 {i + 1} 頁 ===\n{doc[i].get_text()}"
            for i in range(start, end)
        )

        chunk_file = f"{output_dir}/{base_name}_p{start + 1:03d}-{end:03d}.txt"
        with open(chunk_file, "w", encoding="utf-8") as f:
            f.write(text)
        output_files.append(chunk_file)
        print(f"已建立：{chunk_file}")

    doc.close()
    print(f"\n分割完成：共 {len(output_files)} 個檔案")
    return output_files


def main():
    parser = argparse.ArgumentParser(description="PDF 文字提取工具")
    parser.add_argument("pdf_path", help="PDF 檔案路徑")
    parser.add_argument("--output", "-o", help="輸出目錄", default=None)
    parser.add_argument("--pages", "-p", help="頁面範圍，格式：start-end")
    parser.add_argument("--split", "-s", action="store_true", help="分割模式")
    parser.add_argument("--chunk-size", "-c", type=int, default=20, help="每個分割檔案的頁數（預設：20）")

    args = parser.parse_args()

    if args.split:
        split_pdf(args.pdf_path, args.output, args.chunk_size)
    else:
        extract_pdf(args.pdf_path, args.output, args.pages)


if __name__ == "__main__":
    main()
