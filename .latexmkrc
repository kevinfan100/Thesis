# 使用 XeLaTeX
$pdf_mode = 5;
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -shell-escape -file-line-error %O %S';

# BibTeX 設定
$bibtex_use = 2;

# 清理額外的輔助檔案
$clean_ext = 'synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk run tdo %R-blx.bib';
