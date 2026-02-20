# Evidence Inventory by Chapter (Draft)

## Purpose

把「章節敘事」直接對到你現有開發資產，避免後續寫作時找不到可引用證據。

## Ch.3 System Identification

### Primary repos

1. `/Users/kevin/Code/Openloop_Cali`
2. `/Users/kevin/Code/PT3D_SW`

### Candidate evidence artifacts

1. `Openloop_Cali/results/*/diagnostics/Raw_Bode_Data.csv`
2. `Openloop_Cali/results/*/fitting_results/fit_results.mat`
3. `Openloop_Cali/results/*/Comparison_*.png`
4. PT3D_SW 掃頻與資料品質檢查相關 commit（2026-02-09 ~ 2026-02-12）

### Suggested tables/figures

1. 多配置 Bode 疊圖（single/pair/tip-surface）
2. fitting residual 對照圖
3. 穩態偵測與 super-period FFT 示意

## Ch.4 Flux Control

### Primary repos

1. `/Users/kevin/Code/r_controller_package`
2. `/Users/kevin/Code/PT3D_HW2_imc2c16`

### Candidate evidence artifacts

1. `r_controller_package/test_script/inner_loop/*`
2. `r_controller_package/test_script/utils/fft_analysis.m`
3. FPGA 同步與 debug commits（2026-01-14, 2026-01-13）
4. R-controller 相關修正紀錄（例如 `delta_v_hat` 調整）

### Suggested tables/figures

1. PI vs model-based closed-loop Bode
2. component ablation（FF/FB/DOB）對照圖
3. 參數敏感度（`fB_c, fB_e, fB_f`）掃描圖

## Ch.5 Force Generation

### Primary repo

1. `/Users/kevin/Code/r_controller_package`

### Candidate evidence artifacts

1. `test_script/force_generation/run_force_generation_test.m`
2. `test_script/force_generation/run_force_bode.m`
3. VD LPF / 排程比較相關 commit（2026-02-03 ~ 2026-02-10）

### Suggested tables/figures

1. 不同 Vd 排程法之 time-domain force response
2. harmonic content（input Vm / output force）比較
3. force bandwidth bottleneck 分解圖

## Ch.6 FPGA + Experiment

### Primary repos

1. `/Users/kevin/Code/PT3D_HW2_imc2c16`
2. `/Users/kevin/Code/PT3D_SW`

### Candidate evidence artifacts

1. 100kHz sync verification logs
2. InvModel test debug captures
3. 上位機量測流程與資料穩定性檢查

### Suggested tables/figures

1. control pipeline latency / timing budget
2. sim-vs-hardware bode overlay
3. cross-channel behavior in hardware

## Ch.1 + Abstract consistency check

目前 `NTHU_template` 的 `34dc6fb` 已有 layer-by-layer narrative，可直接作為母稿。  
建議先以上述各章 evidence 清單補齊，再做最小改動精修。
