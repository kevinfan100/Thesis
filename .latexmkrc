# 論文編譯設定：XeLaTeX + biber（biblatex, style=ieee）
# 入口為根目錄 main.tex，直接執行 `latexmk` 即可。

$pdf_mode = 5;                  # XeLaTeX
@default_files = ('main.tex');
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -shell-escape -file-line-error %O %S';

# biblatex 使用 biber，非 bibtex
$bibtex_use = 2;

# `latexmk -c` 額外清除的輔助檔
$clean_ext = 'synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk run tdo '
           . 'glo ist nlo nls ilg acn acr alg glg gls %R-blx.bib';

# 輔助檔集中到 build/，PDF 與 synctex 留在根目錄
# （PDF 路徑不變，外部工具與雙擊開啟都不受影響）
$aux_dir = 'build';
