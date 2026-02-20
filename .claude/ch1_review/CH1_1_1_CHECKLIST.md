# Ch1 1.1 Review Readiness Checklist

## Verify Git/worktree state
```bash
git -C /Users/kevin/Code/NTHU_template worktree list
git -C /Users/kevin/Code/NTHU_template branch --show-current
git -C /Users/kevin/Code/worktrees/ch1-worktree branch --show-current
```

Expected:
- main repo branch is `main`
- worktree branch is `codex/thesis-foundation-map-v1`

## Files to inspect first
- Chinese current draft: `/Users/kevin/Code/worktrees/ch1-worktree/01_introduction.tex`
- English rebuild draft: `/Users/kevin/Code/worktrees/ch1-worktree/NTHU_Thesis_template_in_English_with_Chines_title_pages_compiled_with_pdfLaTeX_2025/contents/chapter01.tex`
- Segment review pack: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/CH1_1_1_REBUILD_REVIEW.md`

## Compile and open PDF
```bash
cd /Users/kevin/Code/worktrees/ch1-worktree/NTHU_Thesis_template_in_English_with_Chines_title_pages_compiled_with_pdfLaTeX_2025
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
open main.pdf
```

## Live review order
1. Segment 1
2. Segment 2
3. Segment 3
4. Segment 4
5. Segment 5
6. Segment 6

Each segment confirms:
- final EN paragraph
- final ZH paragraph
- one terminology/wording decision (if needed)
