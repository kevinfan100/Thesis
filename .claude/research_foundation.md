# 六極電磁致動器控制系統——完整研究基礎

> **用途**：碩士論文撰寫的核心參考文件，整合系統物理理解與研究演進史。
> **維護方式**：透過 ralph-loop 迭代驗證，每節標注驗證狀態與來源論文。
> **作者**：范宏翌（Hung-Yi Fan），指導教授：Dr. Chia-Hsiang Menq（孟嘉祥）

---

## 驗證狀態總覽

| 節 | 主題 | 狀態 | 主要驗證來源 |
|----|------|------|-------------|
| A1 | 磁路物理 | [VERIFIED] | Zhang 2011 Section II-A/B + III-A |
| A2 | 力模型 | [VERIFIED] | Zhang 2011 Section III + Long 2022 Eq. 1-5 |
| A3 | 過驅動與最佳化 | [VERIFIED] | Long 2021 Section III + IV |
| A4 | 磁滯與 Hall Sensor | [VERIFIED] | Long 2022 Section II-C, III, IV |
| A5 | 離散化與 Ringing Zero | [VERIFIED] | Meng 2024 Section II-D + III-A |
| A6 | 內迴圈控制 | [VERIFIED] | Meng 2024 Section II-D + III-A; Meng 2023 待 A7 交叉驗證 |
| A7 | 粒子動力學 | [VERIFIED] | Meng 2023 Eq. 12-23, Sec III-D, IV-A |
| A8 | 系統整合 | [VERIFIED] | Meng 2023 Sec II-D + IV; Meng 2024 Sec III |
| B | 研究演進史 | [VERIFIED] | 全部論文交叉驗證 |
| C | Kevin 研究定位 | [VERIFIED - internal] | 教授報告 + 計劃文件（非論文驗證） |

---

# Part A：物理系統理解

> 以概念層組織，著重 Hall-sensor-based（磁通基）體系的物理意義。
> 每層回答「物理上為什麼」，而非只記錄「做了什麼」。

---

## A1. 磁路物理——電流如何變成工作空間中的磁場 [VERIFIED]

**驗證來源**：Zhang 2011 p1-4（hexapole design, magnetic circuit）

六極電磁致動器的本質是一個三維磁場產生器。要在三維空間中對磁性微珠施加任意方向的力，至少需要六個獨立的磁極——三對相對的磁極分別對應三個正交軸向的推拉。

**為什麼上三下三？** 最直覺的配置是把六個極放在三個正交軸上（±x, ±y, ±z），但這樣 z 軸上的兩個極會擋住倒置顯微鏡的光路。Zhang 2011 的解決方案是對整個六極配置施加一個座標旋轉，使六個極尖端落在兩個平行的水平面上——上三下三。旋轉不改變六極之間的對稱性，因此致動能力完全保留，但光路暢通無阻。旋轉矩陣 ${}^a_m R$（論文直接給出，列向量為 $[1/\sqrt{6}, 1/\sqrt{6}, 2/\sqrt{6}]$、$[-1/\sqrt{2}, 1/\sqrt{2}, 0]$、$[-1/\sqrt{3}, -1/\sqrt{3}, 1/\sqrt{3}]$）記錄了致動座標系（actuation frame）與量測座標系（measurement frame）之間的轉換。[Zhang 2011, Section II-A, Fig. 2]

**磁路分析：coil → yoke → pole → air gap → bead。** 線圈產生磁動勢 $\mathcal{F} = N_c I$，磁通沿著低磁阻路徑流動：先經磁軛（yoke，冷軋鋼），再進入磁極（pole），最後從尖端（tip）發散到空氣中的工作空間。關鍵物理洞見是：空氣的磁阻 $\mathcal{R}_a$ 遠大於磁軛 $\mathcal{R}_y$ 和磁極 $\mathcal{R}_p$ 的磁阻（因為空氣的磁導率只有鐵磁材料的幾千分之一）。這意味著磁通的分布幾乎完全由空氣磁阻決定，材料部分可以近似忽略。根據 Hopkinson 定律（磁路版的歐姆定律），六個通道的磁通分布由 6×6 矩陣 $K_I$ 描述：對角元素 5/6、非對角元素 -1/6。非對角項的物理意義是「互磁化」——當一個線圈通電時，它不只磁化自己的極，也透過共用的磁軛影響其他五個極。（**注**：Zhang 2011 印刷為 +1/6，但磁路 KCL 分析可推導得 -1/6 才能使 $\sum q_j = 0$ 對任意電流成立；原文的 +1/6 需搭配 $\sum I_j = 0$ 約束才滿足磁荷守恆。）[Zhang 2011, Section III-A, Eq. 2, Fig. 5]

**磁荷模型（magnetic charge model）。** 從工作空間中微珠的角度看，每個尖銳的極尖端產生的磁場看起來就像一個點磁荷。這是一個遠場近似：當觀察點離極尖端的距離遠大於尖端半徑（~40 μm）時，複雜的磁場分布可以用一個等效點源來代替。磁荷的定義類比於電荷：$q = \Phi/\mu_0$，其中 $\Phi$ 是流過該極的磁通量。六個點磁荷產生的總磁場就是簡單的疊加：$\mathbf{B} = \sum_{j=1}^{6} k_m q_j / r_j^2 \cdot \mathbf{u}_j$（Eq. 1）。磁荷與電流的關係由磁路得 $\mathbf{Q} = (N_c/\mu_0\mathcal{R}_a) K_I \mathbf{I}$（Eq. 2）。這個模型已透過有限元素分析驗證，在工作空間內精度很高。注意：磁荷總和永遠為零（$\sum q_j = 0$），這是磁場無源性（$\nabla \cdot \mathbf{B} = 0$）的直接推論——自然界不存在磁單極。[Zhang 2011, Section III-A, Eq. 1-2; FEA 驗證見 Long 2022, Fig. 1c]

**材料演進。** Zhang 2011 的初代致動器：磁極用 Ni-Fe-Mo 合金薄片（178 μm thick），優點是高磁導率和極低磁滯損失，飽和磁感應強度 ~2.1 T；磁軛用冷軋鋼（cold-rolled steel，未指定鋼號）。但力太小（$k_{\hat{I}} = 0.53$ pN at $I_{max}$ = 1.2 A）。Long 2016 的新一代改用 1018 鋼棒（0.18% 碳鋼）作為磁極，飽和極限也超過 2 T，但能承載更大電流（3 A），極大提升了力生成能力。代價是 1018 鋼的磁滯更大——這直接催生了後來引入 Hall sensor 的需求（→ A4）。[Zhang 2011, Section II-B; Long 2016]

**關鍵尺寸。** 極間距 $\ell = 594$ μm（從工作空間中心到每個極尖端的距離）決定了力的大小：力增益 $g_\Phi$ 與 $\ell^{-5}$ 成正比（因為磁場梯度隨距離快速衰減）。極尖端半徑 ~40 μm 則決定了磁荷模型的有效範圍——工作空間半徑大約是歸一化距離 0.3 以內（即 $\Gamma > 0.1$），可以有效建立回饋控制。[Zhang 2011, Section III-B, Fig. 7-8]

→ **連結 A2**：磁路把電流轉換成磁通，磁通決定了工作空間中的磁場。但磁場本身不直接施力——是磁場的「梯度」才產生力。

---

## A2. 力模型——磁場梯度如何對微珠施力 [VERIFIED]

**驗證來源**：Zhang 2011 p4-7（force model）, Long 2022 p2-4（flux-based reformulation）

**超順磁性的物理意義。** 實驗中使用的磁性微珠（如 Dynal M280，直徑 2.8 μm）含有氧化鐵奈米粒子，但整顆珠的磁行為是「超順磁」的：在外加磁場存在時表現出磁性，磁場移除後磁性消失。物理上，這意味著微珠沒有固有的磁矩——它的磁矩完全由外部磁場「感應」出來。數學上：$\mathbf{m} = \frac{3V}{\mu_0}\frac{\mu - \mu_0}{\mu + 2\mu_0}\mathbf{B}$，磁矩與外部磁場成正比。這有兩個深遠的結果：(1) 因為磁矩永遠平行於磁場，所以磁力矩為零——不需要擔心微珠旋轉；(2) 力的方向不取決於磁場方向，而取決於磁場梯度方向。[Zhang 2011, Section III-A, Eq. 3 前之定義]

**為什麼是梯度力？** 對一個感應磁偶極，磁力為 $\mathbf{F} = \frac{1}{2}\nabla(\mathbf{m} \cdot \mathbf{B})$（Eq. 3）。直覺上：在均勻磁場中，磁偶極兩端受到的力大小相等、方向相反，淨力為零。只有當磁場不均勻（有梯度）時，兩端受力才有差異，產生淨力。又因為超順磁微珠的 $\mathbf{m} \propto \mathbf{B}$，代入得 $\mathbf{F} \propto \nabla(|\mathbf{B}|^2)$。所以力永遠指向磁場增強的方向——微珠總是被吸引向磁場最強的地方（最近的極尖端）。這也解釋了 Earnshaw 定理的推論：磁力場對微珠來說是本質不穩定的，必須用回饋控制才能穩定陷阱。[Zhang 2011, Section III-A, Eq. 3-4]

**二次型的物理必然性。** 因為 $\mathbf{m} \propto \mathbf{B}$ 且 $\mathbf{B} \propto \mathbf{q}$（磁荷，即 $\Phi/\mu_0$），力 $\propto \nabla(|\mathbf{B}|^2) \propto \nabla(\mathbf{q}^T \cdot \mathbf{q})$，自然是磁荷（或磁通）的二次型。這不是建模上的選擇，而是「感應磁矩 + 梯度力」這兩個物理事實的數學必然結果。寫成規範形式：

$$\mathbf{F}(\mathbf{p}, \boldsymbol{\Phi}) = g_\Phi \boldsymbol{\Phi}^T L(\hat{\mathbf{p}}) \boldsymbol{\Phi}$$

其中 $L$ 是 6×6×3 的梯度矩陣。[Long 2022, Section II, Eq. 1-5]

**$g_\Phi$ 和 $L$ 的物理內容。** 力增益 $g_\Phi = \frac{3V\chi}{2\mu_0(4\pi)^2 \ell^5}$ 包含了兩類資訊：微珠的性質（體積 $V$、磁化率 $\chi$）和系統的幾何尺寸（$\ell^5$）。一旦確定了微珠和致動器，$g_\Phi$ 就是一個常數。梯度矩陣 $L(\hat{\mathbf{p}})$ 則純粹是幾何的：它描述了六個磁荷在歸一化空間中的位置如何影響梯度力的方向和耦合。在工作空間中心，$L$ 有最高的對稱性；遠離中心時，$L$ 的各向異性增大。力包絡（force envelope）就是 $L$ 隨位置變化的幾何視覺化。（**注**：Zhang 2011 使用電流基歸一化形式 $\hat{F} = \hat{I}^T N(\hat{p}) \hat{I}$（Eq. 4），此處的 $g_\Phi$ 公式是 Long 2022 轉換到磁通基後的表述。）[Zhang 2011, Section III-B, Fig. 7-9; Long 2022, Eq. 1-5]

**力包絡的物理意義。** 在工作空間中心，力包絡對稱，最小力 $\hat{F}_{min}$ 最大，各向異性 $\Gamma = 0.58$（無約束情況，Section III-B, Fig. 8）。遠離中心時，包絡被拉向最近的極，$\Gamma$ 下降。Zhang 2011 定義了一個「退化邊界」：當使用逆模型約束後 $\Gamma < 0.04$ 時，某些方向的力無法產生，回饋控制失效（Section IV-B, Fig. 11）。[Zhang 2011, Section III-B + IV-B]

→ **連結 A3**：力模型是六輸入三輸出的過驅動系統——六個磁通產生三維力。多出的三個自由度如何利用？

---

## A3. 過驅動與最佳化——6 個輸入控制 3 個力分量 [VERIFIED]

**驗證來源**：Long 2021 p2-6（Lagrange optimization, scalable property）

**過驅動的本質。** 六個磁通變數（$\Phi_1$ 到 $\Phi_6$）只需要滿足三個力方程式（$F_x, F_y, F_z$）。這意味著有無窮多組磁通組合可以產生同一個力向量——解空間是三維的。物理上，這些「多餘」的自由度決定了磁場的「形狀」而不只是力的方向。不同的磁通分配會產生相同的力，但磁場的空間分布不同，消耗的總磁通量也不同。

**為什麼最小化 $||\mathbf{I}||^2$（或等效地 $||\boldsymbol{\Phi}||^2$）？** Long 2021 的最佳化目標是最小化電流向量的二範數 $||\hat{I}||^2$（因為該文仍為 current-based 體系），物理上對應最小化磁路中的總磁能，這直接帶來三個好處：(1) 減少歐姆熱耗（電流與磁通正相關）；(2) 降低磁飽和風險（每個極承載的磁通更均勻）；(3) 擴大力包絡——相同的電流限制下能產生更大的力。[Long 2021, Section III-B, Eq. 7]

**常數約束 vs 最佳約束的巨大差異。** Zhang 2011 的逆模型引入了三個常數約束 $c = [\hat{I}_1 + \hat{I}_2, \hat{I}_3 + \hat{I}_4, \hat{I}_5 + \hat{I}_6]^T$，化簡出簡潔的線性逆模型。問題在於：常數約束意味著不管力的方向如何，都有一部分固定的「背景電流」在流動。這些背景電流不產生有用的力，純粹是浪費。Long 2021 的突破是讓約束隨力方向變化——$c(\phi, \theta)$ 是方向相關的最佳約束。最佳分配的電流幅度顯著小於常數約束，力包絡體積大幅擴張。[Long 2021, Fig. 3 + Fig. 7]

**Scalable property 的物理根源。** 因為力是電流（或磁通）的二次型（$\hat{F} \propto \hat{I}^T N \hat{I}$），力的大小 $||\hat{F}||$ 正比於 $||\hat{I}||^2$。這意味著：要產生方向為 $\hat{r}(\phi, \theta)$、大小為 $||\hat{F}_d||$ 的力，最佳電流 $\hat{I}_{opt}(\hat{F}_d, \hat{p}) = ||\hat{F}_d||^{1/2} \cdot \hat{I}^{unit}_{opt}(\hat{r}(\phi,\theta), \hat{p})$。力的大小只影響電流的「幅度」，方向和位置決定電流的「形狀」。這個性質使得逆模型可以預先計算好所有方向的單位力最佳電流 $\hat{I}^{unit}_{opt}$，存成查找表（LUT），實際運行時只需查表後乘以幅度因子。（磁通基等效形式：$\Phi_{opt} = \sqrt{||F_d||/g_\Phi} \cdot \hat{\Phi}_{opt}(\phi, \theta, \hat{p})$。）[Long 2021, Section III-B, Eq. 6]

**FPGA 即時實現。** Long 2021 的做法是：在 MATLAB 中用 Lagrange 乘子法在工作空間的預定位置（45 μm × 45 μm × 45 μm 的第一象限立方體內，Fig. 5）和所有方向上求數值解，然後用最小平方擬合構造解析的 4×4 逆模型矩陣 $D^{LS}_i(\phi, \theta)$（每個電流通道 $i=1,...,6$ 各一個）。實際運行時，FPGA 只需做矩陣乘法：$\hat{I}^{unit}_{opt}(\phi,\theta,\hat{p})_i \approx P^T D^{LS}_i(\phi,\theta) P$，其中 $P = [\hat{x}, \hat{y}, \hat{z}, 1]^T$，計算量很小。擬合的力生成誤差在工作空間內 < 5%（Fig. 6b）。[Long 2021, Section III-C, Eq. 12, Fig. 5-6]

→ **連結 A4**：無論用電流基還是磁通基模型，力模型都假設了 $I \rightarrow \Phi$ 是準靜態的線性關係。但實際上，磁滯效應會嚴重破壞這個假設。

---

## A4. 磁滯與 Hall Sensor——系統的根本問題與解法 [VERIFIED]

**驗證來源**：Long 2022 p5-12（Hall sensor integration, calibration, experimental results）

**磁滯的物理本質。** 鐵磁材料內部由磁疇（magnetic domain）組成。外加磁場時，磁疇壁移動，磁疇重新排列。問題在於磁疇壁的移動不是完全可逆的——材料中的缺陷和晶界會「釘住」磁疇壁，需要額外的能量才能跨越。移除外加磁場後，磁疇壁不會完全回到原位，留下殘餘磁化（remanent magnetization）。對六極系統來說，磁滯意味著相同的輸入電流不一定產生相同的磁通量——磁通量取決於電流的歷史。Long 2022 指出三層困難：(1) 材料的率相關磁滯（rate-dependent hysteresis）；(2) 瞬態磁化的 accommodation effect；(3) 六極之間的磁耦合放大問題複雜度。[Long 2022, Section II-C]

**磁滯對力預測的量化影響。** Long 2022 的實驗直接展示後果：使用電流基逆模型定位時，穩態定位誤差為 $\delta x = 64$ nm, $\delta y = -117$ nm, $\delta z = 358$ nm。六個磁極中有四個（P1, P2, P3, P5）的 Hall sensor 讀數顯示明顯的殘餘磁化偏移，而且偏移的大小和方向隨操作歷史改變——每次實驗的誤差都不同。[Long 2022, Fig. 7 + Fig. 8]

**電流基鏈條中磁滯破壞的是 $I \rightarrow \Phi$ 這一段。** 在 $I \rightarrow q \rightarrow \Phi \rightarrow B \rightarrow F$ 的鏈條中，$\Phi \rightarrow B \rightarrow F$ 由磁荷模型和梯度力公式決定（電磁學基本定律，不受磁滯影響）。磁滯影響的是 $I \rightarrow \Phi$ 映射——Hopkinson 定律假設線性準靜態關係，但磁滯使之變成非線性、率相關、且依賴歷史。

**Hall sensor 的解法：直接量測，繞過磁滯。** 與其試圖模型化磁滯（Preisach 模型等方法在六極系統上極難實施），不如直接量測磁通量。六個高頻寬 Hall sensor（Asahi Kasei EQ-730L，100 kHz）安裝在每個磁極上，直接讀取磁通。完全繞過了 $I \rightarrow \Phi$ 的不確定性——不管電流歷史如何，Hall sensor 告訴你「此刻」的磁通量。[Long 2022, Section III-A, Fig. 3]

**Surface-to-tip ratio 的穩定性。** Hall sensor 理想應放在極尖端，但尖端在 ~500 μm 的工作空間內，Hall sensor 晶片（4.1 mm × 3 mm）完全放不下。解決方案是把 sensor 放在磁極的表面。Long 2022 驗證了關鍵假設：表面量測 $v_s$ 和尖端量測 $v_t$ 的比值在 1000–3000 Hz 範圍幾乎恆定（~0.47，由 Fig. 5 估得），線性回歸 RMSE < 3%。無論自激或耦合激勵，比值均穩定。物理原因：在此頻率範圍，磁通在磁極中是準靜態分布——整個磁極近似均勻磁化，表面和尖端之間的比例只取決於幾何形狀。Meng 2024 進一步驗證到 4000 Hz。更高頻時渦電流（eddy current）和趨膚效應改變磁通分布，比值才會偏離。[Long 2022, Section III-B, Fig. 4-5; Meng 2024, Section III]

**$\hat{D}_H$ 矩陣的物理意義。** $\hat{D}_H = \text{diag}(0.444, 0.364, 0.445, 0.436, 0.353, 0.436)$ 是歸一化的電壓-磁通增益矩陣。對角矩陣的原因：每個 Hall sensor 只量測自己對應極的磁通——各通道在這個環節不存在耦合（耦合體現在磁路的 $K_I$ 中，但 Hall sensor 量的是耦合後的結果）。六個值不同，反映上層三極和下層三極的 Hall sensor 安裝位置差異。[Long 2022, Section IV-B]

**用 Stokes drag 校準力模型。** 微珠上的力無法直接量測（微珠 ~μm、力 ~pN）。間接方法：在低 Reynolds number 下 $F_{drag} = \gamma \dot{p}$，$\gamma$ 可從 Brownian motion 功率頻譜密度精確確定。控制微珠沿已知軌跡運動（xy、yz、xz 平面圓形軌跡），量測速度乘以 $\gamma$ 得到力。最小化 $J_H(g_H, \hat{D}_H) = \sum ||\gamma \dot{p}(j) - g_H \hat{F}_H(j)||^2$（Eq. 17），得到 $g_H = 4.741$ pN/V²。Hall-sensor-based 模型 RMSE = $\sigma = \sqrt{J_H/(3N)} = 0.087$ pN，遠優於 current-based 模型（Fig. 14 直方圖對比明顯）。[Long 2022, Section IV-B, Eq. 17, Fig. 9-14]

→ **連結 A5**：有了 Hall sensor，磁通量可以被直接量測和控制。但數位控制引入了 ZOH，離散化時產生接近 $z = -1$ 的零點。

---

## A5. 離散化與 Ringing Zero——ZOH 的物理後果 [VERIFIED]

**驗證來源**：Meng 2024 p2-5（exact discrete model, ZPETC prefilter design）

**ZOH 的物理動作。** 數位控制系統中，D/A 轉換器在每個取樣週期開始時更新輸出，然後保持不變直到下一個取樣點。這個「保持」動作看似無害，但它在連續系統前面串接了一個「脈衝寬度」等於取樣週期的矩形脈衝。在頻域中，ZOH 等效於一個 $\sinc$ 函數加上相位延遲——引入了額外的動態。

**Ringing zero 的數學來源。** 連續系統 $H(s)$ 是二階過阻尼系統（頻寬 ~200 Hz），所有零點在左半平面——minimum phase。ZOH 離散化（100 kHz 取樣率）的精確模型（Meng 2024）為：

$$H(z^{-1}) = z^{-1} \frac{7.2126 \times 10^{-4} (1 + 0.9731 z^{-1})}{(1 - 0.9733z^{-1})(1 - 0.9467z^{-1})} B$$

分子出現零點 $z = -0.9731$，非常接近 $z = -1$。這是 ZOH 離散化的「副產品」——Astrom 的理論：連續系統相對階次（極點數 - 零點數）≥ 2 時必然產生接近 $z = -1$ 的零點。二階系統無有限零點（相對階次 = 2），因此恰好產生一個。[Meng 2024, Section III-A, Eq. 8; 連續模型見 Section II-D, Eq. 7]

**時域行為：ringing。** $z = -0.97$ 零點意味著：若控制器試圖取消它（inverse-based control），控制信號中會出現接近 $(-0.97)^{-k}$ 的成分——每個 sample 幾乎正負交替，幅度緩慢增長。物理上 D/A 輸出的電壓每 10 μs 正負翻轉，遠超磁路頻寬。

**頻寬限制。** 零點位置 $z = -0.9731$ 對應頻率接近 Nyquist 頻率（50 kHz）。Meng 2023 刻意迴避此零點（使用近似離散模型），閉迴圈頻寬限在 1 kHz。Meng 2024 的突破是直接面對精確離散模型。[Meng 2023, Section III-A vs Meng 2024, Section III]

**ZPETC（Zero Phase Error Tracking Controller）。** 對非最小相位系統，不能直接取消 $z = -0.97$ 這個不穩定零點。ZPETC 的核心思想：把零點的逆因子用「零相位等效」替代——取零點的相位特性但不取消幅度。Meng 2024 的 prefilter（Eq. 20）經閉迴圈後，磁通響應為（Eq. 21）：

$$v_m[k+1] = \frac{1}{(1+b)^2}\{b \cdot v_d[k+d-1] + (1+b^2) v_d[k+d-2] + b \cdot v_d[k+d-3]\}$$

[Meng 2024, Section III-A, Eq. 20（prefilter）, Eq. 21（閉迴圈響應）]

**d=2 步 preview 的物理意義。** 閉迴圈頻率響應：$[(1+2b\cos\theta + b^2)/(1+b)^2] \cdot e^{j(d-2)\theta}$，其中 $\theta = \omega \Delta t$，$\Delta t = 10^{-5}$ s。當 $d=2$ 時，相位項 $e^0 = 1$——零相位誤差。Preview 步數 = 系統延遲步數（一步 ZOH 延遲 + 一步計算延遲），物理上是「提前知道未來兩步的期望值」補償延遲。增益項在低頻趨近 1，20 kHz 處降到 0.707——ZPETC 頻寬極限。（**注**：Meng 2024 的 Bode 實驗使用 $d=0$（無 preview），仍達 >4 kHz；$d=2$ 可進一步消除相位延遲。）[Meng 2024, Section III-A, text following Eq. 21]

→ **連結 A6**：理解了離散化零點問題後，完整的三組件控制器如何在此約束下實現 >4 kHz 磁通控制。

---

## A6. 內迴圈控制——三組件各自補償的物理效應 [VERIFIED]

**驗證來源**：Meng 2024 p5-8（exact model controller）, Meng 2023 p3-6（approx model controller）

**B 矩陣的物理意義。** 6×6 系統模型 $v_m[k+1] = -a_1 v_m[k] - a_2 v_m[k-1] + kB\{u[k] + bu[k-1] + w[k]\}$（Eq. 9）中，B 描述多極耦合：驅動 P5 的線圈時，不只 P5 的 Hall sensor 有響應，其他五個也會（透過共用磁軛）。B 對角元素 0.23–0.28，非對角元素絕對值 0.005–0.08（不等，反映上下層幾何差異）。控制器中的 $B^{-1}$ 做解耦——數學地撤銷互耦，使各通道獨立控制。[Meng 2024, Section II-D, Eq. 7（完整 B 矩陣）]

**三組件控制律 $u[k] = u_{fb}[k] - \hat{w}[k]$（加上 prefilter）各自對付不同物理現象：**

1. **Prefilter（前饋/預濾波器）** 處理「已知的系統動態」——極點、零點位置、延遲。特別是 ringing zero 的相位補償（ZPETC, d=2 preview），使 $v_d$ 在進入回饋環之前做好預校正。

2. **Feedback（回饋控制律）** 處理「即時追蹤誤差」。期望誤差動態 $\delta v[k+1] = \lambda_c \delta v[k]$，$\lambda_c$ 越小追蹤越快但需更大控制信號。Meng 2024：$\lambda_c = 0.8179$（3200 Hz 等效頻寬），遠超 Meng 2023：$\lambda_c = 0.9391$（1000 Hz）。關鍵改進：回饋律將 ringing pole 從 $-b = -0.9731$ 移至 $-b_1$，其中 $b_1 = (1-\lambda_c)b/(1+b)$。Meng 2024（$\lambda_c = 0.8179$）：$b_1 \approx 0.090$，ringing 振幅衰減約 10 倍。Meng 2023（$\lambda_c = 0.9391$）：$b_1 \approx 0.030$，更小但控制頻寬也更低。[Meng 2024, Section III-A, Eq. 10-11]

3. **Disturbance Observer（擾動觀測器）** 處理「緩慢變化的未知干擾」——模型誤差 + 殘餘磁化。擾動模型：$w_1[k+1] = w_1[k] + \delta w[k]$, $\delta w[k+1] = \delta w[k]$（線性漂移模型），$\lambda_e$ 設定估測速度（四個特徵值皆設為 $\lambda_e$）。Meng 2024：$\lambda_e = 0.3659$（16000 Hz），遠快於控制頻寬。[Meng 2024, Section III-A, Eq. 14-17]

**2023 → 2024 技術躍進。** Meng 2023 使用近似離散模型，刻意迴避 ringing zero，閉迴圈 1 kHz，需「顯著降低增益才能穩定」（Meng 2024, Section I 明確指出此限制）。Meng 2024 使用精確 ZOH 離散模型（Eq. 8），重新推導三組件控制律，理論與實驗精確吻合，>4 kHz，**無需實驗調參**。[Meng 2024, Section I + Section III]

**為什麼可以把 6-D 耦合估測器解耦為 6 個 scalar 估測器？** 關鍵洞見：回饋律已含 $B^{-1}$ 解耦，且擾動 $w$ 經轉換 $w^*$（Eq. 12）後，誤差動態（Eq. 13-14）和擾動模型都是解耦的。因此增廣估測器可寫成六個獨立 scalar estimator（各 4 states：$\delta\hat{v}_i, \hat{w}_{1i}, \delta\hat{w}_i, \hat{w}_{2i}$，Eq. 15）。[Meng 2024, Section III-A, Eq. 12-15]

**閉迴圈結果。** 驅動 P5 時其他通道響應被壓制到接近零（Fig. 6）；三軸力頻率響應與理論預測精確吻合（Fig. 7）。六極磁通可獨立精確控制——磁滯、耦合、頻寬限制全被解決，且**無需實驗調參**。[Meng 2024, Section III-C/D, Fig. 6-7]

→ **連結 A7**：控制器讓致動器在工程上可用。但微珠在水溶液中的行為由粒子動力學支配。

---

## A7. 粒子動力學——水溶液中微珠的物理行為 [VERIFIED]

**驗證來源**：Meng 2023 p6-10（Langevin equation, variance control, wall effect）

**低 Reynolds number 的世界。** 直徑 4.5 μm 微珠在水中以 ~10 μm/s 運動，$Re = \rho v D / \eta \approx 10^{-5}$。黏滯力完全支配慣性力——微珠沒有「動量」的概念。推一下就動，停止推就立刻停（在微秒時間尺度內）。Langevin 方程的慣性項可忽略，簡化為一階：$\gamma \dot{p} = f_m + f_T$。[Meng 2023, Section IV-A]

**一階動力學對控制的根本影響。** 沒有慣性 = 沒有振盪、沒有共振——系統本質是積分器（$\dot{p} \propto F$）。穩定條件 $K_p < 0.618 \gamma / T$（Jury 準則），非常簡潔。但代價：常數擾動 $\Delta F$ 導致穩態偏移 $e_{ss} = -\Delta F / K_p$——力預測精度直接決定定位精度。[Long 2021, Section IV]

**Brownian motion 的物理來源。** 微珠每秒被水分子撞擊約 $10^{13}$ 次，總效果是零均值隨機力 $f_T(t)$。漲落耗散定理（fluctuation-dissipation theorem）：$f_T$ 的統計完全由溫度和阻尼決定，功率頻譜密度是白噪聲，$\sigma^2_{f_T} = 4 k_B T \gamma / \Delta t$。$\sigma^2_{f_T} \propto \gamma$——阻尼越大、噪聲力越大，但位移反而越小：$\sigma^2_{\delta x_T} = 4k_B T \Delta t / \gamma$。[Meng 2023, Section IV-B, Eq. 19-20]

**Stokes drag 和壁效應。** Stokes 定律 $\gamma = 6\pi\eta R$ 在無窮流體中精確成立。靠近蓋玻片時流體動力學改變：no-slip 邊界使水層變薄，有效阻尼增大。修正函數 $C_\perp(h/R)$, $C_\parallel(h/R)$（垂直和平行壁面）。$h/R \rightarrow 1$ 時 $C_\perp \rightarrow \infty$——垂直方向被「鎖死」。Meng 2023 用 Brownian motion 變異數校準位置相關阻尼，控制律使用 $\gamma(p)$。[Meng 2023, Section IV-C]

**追蹤誤差的理論極限。** 追蹤誤差變異數（Meng 2023, Eq. 22）：

$$\sigma^2_{\delta x} = \left(2 + \frac{1}{1-\lambda_c^2}\right) \sigma^2_{\delta x_T} + \left(\frac{1-\lambda_c}{1+\lambda_c}\right) \sigma^2_{n_x}$$

是熱力位移和量測噪聲的線性疊加，$\lambda_c$ 控制權衡。存在最佳 $\lambda_c$（Eq. 23）使變異數最小。理論預測 STD ~30 nm，Meng 2023 實驗精確驗證。這不是控制器缺陷，而是**熱力學基本極限**——降低它唯一的方法是提高取樣率。[Meng 2023, Eq. 22-23, Fig. 9]

→ **連結 A8**：粒子動力學決定外迴圈基本限制。三層架構如何整合所有物理。

---

## A8. 系統整合——三層架構的物理邏輯 [VERIFIED]

**驗證來源**：Meng 2023 + Meng 2024 綜合

**三層架構總覽。**

| 層 | 取樣率 | 職責 | 輸入 → 輸出 |
|---|--------|------|-------------|
| 內迴圈（磁通控制）| 100 kHz | 消除磁滯、解耦、提升頻寬 | $v_d \rightarrow v_m$ |
| 力生成（逆模型 + 分配）| 1.6 kHz | 非線性逆模型、位置相關最佳分配 | $F_d, p \rightarrow v_d$ |
| 外迴圈（運動控制）| 1.6 kHz | 穩定、追蹤、Brownian motion 控制 | $p_d \rightarrow F_d$ |

**取樣率設計邏輯。**
- **100 kHz 內迴圈**：閉迴圈頻寬 4 kHz × 25 倍。Hall sensor 100 kHz，ADC（ADS8365）200 kHz（Nyquist 準則：200 kHz ADC 才能不失真量測接近 100 kHz 的信號）。
- **FPGA 100 MHz / 100 kHz = 1000 cycles/period**：ADC 讀取 + $B^{-1}$ 矩陣乘法 + 回饋律 + 估測器 + prefilter + DAC 輸出。FP32 浮點 pipeline 架構。R-Controller pipeline 255 cycles——綽綽有餘。
- **1.6 kHz 外迴圈**：CMOS camera 512×512 @ 1606 fps。粒子動力學時間常數 $\tau = \gamma/K_p \approx 0.42$ s——取樣率遠快於動態。

**頻寬的「傳遞」邏輯。** 內迴圈 >4 kHz → 對外迴圈（1.6 kHz）幾乎「瞬時」。力生成層無動態（代數計算）→ 頻寬等於內迴圈。外迴圈等效頻寬由 $\lambda_c$ 和粒子動力學決定。

**內迴圈品質決定系統上限。** 若內迴圈有殘餘磁滯或頻寬不足 → 力偏差 $\Delta F$ → 穩態定位偏差 $e_{ss} = -\Delta F / K_p$。Meng 2023 Fig. 12：不用磁通控制 → 確定性誤差；用了磁通控制 → 只剩隨機誤差（熱力 + 噪聲）。[Meng 2023, Fig. 12]

**分層設計哲學。** 從內到外，每層解決上層「遺留」的問題：(1) 內迴圈消除電磁缺陷（磁滯、耦合、頻寬）；(2) 力生成層消除數學複雜度（冗餘、非線性、位置依賴）；(3) 外迴圈處理環境隨機性（Brownian motion、壁效應）。每層讓下一層設計更簡單——分層控制架構的精髓。

---

# Part B：研究演進史 [VERIFIED]

## 技術演進時間線

```
2009  Zhang: 四極磁性鉗夾 (2D，前身系統)
  │
2011  Zhang: 六極設計 + 集總參數力模型 (3D)
  │      └── 限制：常數約束逆模型，未考慮磁滯
  │
2013  Zhang/Long: 3D 視覺伺服控制
  │
2016  Long: 硬體升級 (1018 steel, 3A) + 主動控制 + 博士論文
  │      └── 完整系統架構建立
  │
2021  Long: 最佳電流分配 (Lagrange multiplier)
  │      ├── 力包絡體積大幅提升
  │      └── 限制：current-based model，磁滯瓶頸
  │
2022  Long: Hall-Sensor-Based 力建模
  │      ├── 磁通基力模型（根本解決磁滯）
  │      ├── 首次引入內迴圈 (100 kHz PI, ADC @ 200 kHz)
  │      └── 定位精度改善 ~13 倍
  │
2023  Meng: 超精密高速無繫繩操控
  │      ├── 三組件控制器 (FF + FB + DOB)
  │      ├── 磁通頻寬 = 1 kHz（用近似模型迴避 ringing zero）
  │      └── 完整三層架構 + 運動控制
  │
2024  Meng: 皮牛頓力控制
       ├── 正面處理 ringing zero（精確模型 + ZPETC）
       ├── 磁通頻寬 > 4 kHz，無需實驗調參
       ├── 解耦擾動估測器
       └── 7-state Kalman filter 力控制
```

## 論文詳細記錄

### Zhang & Menq 2011 — 六極致動器設計與建模

- **期刊**: IEEE/ASME Trans. Mechatronics, 16(3), 421–430
- **核心**：六極幾何配置 + 磁荷模型 + 歸一化二次型力模型 $\hat{F} = \hat{I}^T N(\hat{p}) \hat{I}$ + 常數約束逆模型
- **硬體**：Ni-Fe-Mo 合金，50 匝 AWG-24，$I_{max}$ = 1.2 A
- **結果**：$k_f \approx 0.53$ pN；3D grid trajectory，Brownian STD ±210 nm
- **限制**：常數約束犧牲力包絡、未考慮磁滯、完全 current-based
- **物理理解對應**：→ A1（磁路）, A2（力模型）

### Long et al. 2021 — 最佳電流分配

- **期刊**: IEEE/ASME Trans. Mechatronics, 26(5), 2408–2417
- **核心**：方向相關最佳約束（Lagrange multiplier）、scalable optimal inverse、LS fitting 預計算
- **結果**：Brownian STD (57.8, 43.8, 42.0 nm) vs 常數約束 (123.1, 63.1, 109.8 nm)；逆模型誤差 < 5%
- **限制**：current-based model，磁滯為定位精度瓶頸
- **物理理解對應**：→ A3（過驅動）

### Long et al. 2022 — Hall-Sensor-Based 力建模

- **期刊**: IEEE/ASME Trans. Mechatronics, 27(5), 2806–2817
- **核心**：直接量測磁通（EQ-730L）、flux-based 力模型、surface-to-tip ratio 驗證、Stokes drag 校準
- **結果**：$g_H = 4.741$ pN/V²；RMSE 0.087 pN；z 定位改善 13 倍（358 → 27 nm）
- **內迴圈**：首次引入 PI 內迴圈 @ 100 kHz（各極獨立，未解耦；ADC 取樣 @ 200 kHz）
- **物理理解對應**：→ A4（Hall sensor）

### Meng & Menq 2023 — 超精密高速操控

- **期刊**: IEEE/ASME Trans. Mechatronics, 28(1), 280–291
- **核心**：完整三層架構、三組件控制器（FF+FB+DOB）、近似離散模型、variance control
- **設計參數**：$\lambda_c = 0.9391$（1 kHz），$\lambda_e = 0.7304$（5 kHz）
- **結果**：磁通 BW 1 kHz、追蹤 STD ~32 nm、raster scan 40×16 μm in 2 s
- **物理理解對應**：→ A6（控制器 2023 版）, A7（粒子動力學）, A8（系統整合）

### Meng & Menq 2024 — 皮牛頓力控制

- **期刊**: IEEE/ASME Trans. Mechatronics, 29(1), 400–411
- **核心**：精確 ZOH 離散模型、ZPETC prefilter、解耦 scalar 估測器、7-state Kalman 力控制
- **設計參數**：$\lambda_c = 0.8179$（3.2 kHz），$\lambda_e = 0.3659$（16 kHz）
- **結果**：磁通 BW >4 kHz、無需調參、力控制 STD ~0.1 pN
- **物理理解對應**：→ A5（離散化）, A6（控制器 2024 版）

### 補充論文

| 論文 | 年份 | 核心貢獻 |
|------|------|---------|
| Zhang, Huang & Menq — Quadrupole Magnetic Tweezers | 2009 | 四極前身系統 (2D) |
| Zhang, Long & Menq — 3D Visual Servo Control | 2013 | 視覺伺服框架 |
| Long, Matsuura & Menq — Actively Controlled Hexapole | 2016 | 硬體升級 + 主動控制 |
| Long Dissertation | 2016 | 完整系統建立 |
| Meng Dissertation | 2023 | 全技術整合 |
| Meng, Long & Menq — Near-Wall Motion Control | 2024 | 壁效應處理 |

## 核心技術轉變：Current-based → Flux-based

| | Current-based | Flux-based |
|---|-------------|-----------|
| 力模型 | $F(p, I) = g_I I^T K_I^T L K_I I$ | $F(p, \Phi) = g_\Phi \Phi^T L \Phi$ |
| 控制 | 直接電流控制 | Hall sensor 內迴圈 |
| 磁滯 | 嚴重問題 | 根本解決 |
| 精度 | 受 remanent magnetization 限制 | 接近熱力噪聲極限 |

## 控制架構演進

| 時期 | 內迴圈 | 外迴圈 | 磁通頻寬 |
|------|--------|--------|----------|
| 2011 Zhang | 無 | P @ 200 Hz | — |
| 2016 Long | 無 | PI @ 1.6 kHz | — |
| 2022 Long | PI @ 100 kHz | PI @ 1.6 kHz | ~200 Hz |
| 2023 Meng | 三組件 @ 100 kHz | Model-based @ 1.6 kHz | 1 kHz |
| 2024 Meng | 三組件+ZPETC @ 100 kHz | Kalman @ 1.6 kHz | >4 kHz |

---

# Part C：Kevin 的研究定位 [VERIFIED - internal consistency]

## 核心價值

**Meng 回答「能做到什麼」（Capability）→ Kevin 回答「怎麼系統化地設計」（Methodology）**

教授結案報告明確使用的四個關鍵詞：**自動化、簡化、泛化、參數化**。

## 四大關鍵詞對應的研究缺口

| 關鍵詞 | 前人不足 | Kevin 的貢獻方向 |
|--------|---------|-----------------|
| **自動化** | 系統鑑別手動，模型參數靠個別實驗校準 | 6×6 MIMO 自動鑑別 pipeline + 自動化分析軟體 |
| **簡化** | 控制律推導路徑複雜（大量方程式和設計參數） | R-Controller 統一框架：同功能、更簡潔推導、更少參數 |
| **泛化** | 設計參數與特定系統綁定（$a_1, a_2, b, k$ 等） | 以頻寬參數取代系統特定參數，泛化至任意對稱六極致動器 |
| **參數化** | 缺乏預先評估設計效能的工具 | 參數化模擬軟體模組（MATLAB/Simulink），可評估精度、響應、力度 |

## Kevin 與前人的技術對比

| 物理問題 | Meng 的做法 | Kevin 的做法 | 對比指標 |
|---------|------------|-------------|---------|
| 磁滯效應 | 閉迴圈磁通控制 | 建立在 Meng 基礎上 | 開/閉迴圈 Bode |
| 6×6 耦合 | B matrix 解耦 | + 完整 MIMO 鑑別方法論 | 耦合通道頻率響應 |
| Ringing zero (z≈-0.97) | ZPETC prefilter (2024) | R-Controller 框架內統一處理 | 相位響應 |
| 頻寬不足 (~200 Hz) | 三組件控制器 | R-Controller（同功能、簡化推導）| 閉迴圈 Bode |
| 擾動/模型誤差 | 二階擾動估測器 | 簡化擾動觀測器推導 | 穩態誤差 |
| 2-sample 延遲 | ZPETC preview (d=2) | 框架內參數化處理 | 相位量測 |

## 前人程式碼未留存的意義

Meng 的實驗驗證了系統能力，但程式碼未以可重現形式留存、設計過程高度依賴經驗（特別是參數選擇）。這恰好證明了**精簡、通用、可重現框架**的必要性——Kevin 的論文要回答「如何讓任何人都能系統化地完成這個設計」。

---

# Part D：完整引用清單

## 團隊核心論文（已在 thesis.bib 中）

| # | 引用 Key | 論文 | 年份 | 期刊 |
|---|---------|------|------|------|
| 1 | `zhang2011design` | Zhang & Menq — Design and Modeling of a 3-D Magnetic Actuator | 2011 | T-Mech 16(3) |
| 2 | `long2021optimal` | Long et al. — Optimal Current Allocation | 2021 | T-Mech 26(5) |
| 3 | `long2022hallsensor` | Long et al. — Hall-Sensor-Based Modeling | 2022 | T-Mech 27(5) |
| 4 | `meng2023ultraprecise` | Meng & Menq — Ultra-Precise Manipulation | 2023 | T-Mech 28(1) |
| 5 | `meng2024piconewton` | Meng & Menq — Piconewton Force Control | 2024 | T-Mech 29(1) |

## 待補充引用

| 引用 Key | 論文 | 重要性 |
|----------|------|--------|
| `zhang2009quadrupole` | Zhang, Huang & Menq — Quadrupole Tweezers (2009) | 前身系統 |
| `zhang2013visual` | Zhang, Long & Menq — 3D Visual Servo (2013) | 視覺伺服 |
| `long2016actively` | Long, Matsuura & Menq — Actively Controlled Hexapole (2016) | 硬體升級 |
| `meng2024nearwall` | Meng, Long & Menq — Near-Wall Control (2024) | 壁效應 |
| `tomizuka1987zpetc` | Tomizuka — Zero Phase Error Tracking (1987) | ZPETC 原始 |
| `xia1995precision` | Xia & Menq — Precision Tracking NMP Systems (1995) | ZPETC 延伸 |
| 背景文獻 | 光學鉗夾、AFM 等（Step 1 Perplexity 搜尋） | 研究背景 |

---

# 附錄

## 關鍵方程式速查

| 方程 | 物理意義 | 來源 |
|------|---------|------|
| $\mathbf{B} = \sum k_m q_j/r_j^2 \cdot \mathbf{u}_j$ | 磁荷模型磁場 | Zhang 2011 |
| $\mathbf{Q} = (N_c/\mu_0\mathcal{R}_a) K_I I$ | 磁荷-電流關係 | Zhang 2011 |
| $\mathbf{F} = g_\Phi \Phi^T L(\hat{p}) \Phi$ | 磁通基二次型力模型 | Long 2022 |
| $\Phi_{opt} = \sqrt{\|F_d\|/g_\Phi} \cdot \hat{\Phi}_{opt}(\phi,\theta,\hat{p})$ | Scalable optimal allocation | Long 2021 |
| $H(z^{-1}) = z^{-1}\frac{b_0(1+bz^{-1})}{(1-a_1z^{-1})(1-a_2z^{-1})}B$ | 精確離散模型 | Meng 2024 |
| $u = u_{fb} - \hat{w}$ | 三組件控制律 | Meng 2024 |
| $\gamma \dot{p} = f_m + f_T$ | Langevin 方程 | Meng 2023 |
| $\sigma^2_{\delta x} = (2+\frac{1}{1-\lambda_c^2})\sigma^2_T + (\frac{1-\lambda_c}{1+\lambda_c})\sigma^2_n$ | 追蹤誤差變異數 | Meng 2023 |

## 2023 vs 2024 控制器設計參數對比

| 參數 | Meng 2023 | Meng 2024 | 物理意義 |
|------|-----------|-----------|---------|
| 離散模型 | 近似（迴避 ringing zero）| 精確（正面處理）| 模型精度 |
| $\lambda_c$ | 0.9391 (1 kHz) | 0.8179 (3.2 kHz) | 回饋頻寬 |
| $\lambda_e$ | 0.7304 (5 kHz) | 0.3659 (16 kHz) | 估測器速度 |
| Prefilter | One-step FF | ZPETC (d=2) | 相位補償 |
| 估測器 | 6-D coupled | 6 scalar decoupled | 計算複雜度 |
| 實驗調參 | 需要 | **不需要** | 實用性 |
| 磁通頻寬 | 1 kHz | >4 kHz | 性能 |
