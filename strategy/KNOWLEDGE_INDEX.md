# 知识领域快速入口

> 从知识需求定位题型、方法和验证重点。以下是通用导航；自动区只映射已审核经验卡，不从题名猜测。

| 领域 | 先问什么 | 常用知识/方法入口 | 重点风险与验证 |
|---|---|---|---|
| 概率统计 | 随机性来自采样、测量还是过程本身 | 分布、估计、置信区间、bootstrap、Monte Carlo | 独立同分布假设、样本量、区间覆盖 |
| 回归 | 输出连续且目标是解释还是预测 | 线性/非线性回归、正则化、树模型 | 共线性、异方差、残差、外推 |
| 假设检验 | 要检验的命题、零假设和效应量是什么 | 参数/非参数检验、多重比较 | p 值不等于效应大小，检验前提 |
| 时间序列 | 趋势、季节、自相关和结构变化是否存在 | ARIMA/ETS、状态空间、LSTM、滚动预测 | 未来泄漏、随机切分、漂移 |
| 图论 | 实体与关系能否表示为节点和边 | 最短路、网络流、匹配、中心性 | 图构造、边权含义、连通与动态性 |
| 运筹学 | 决策变量、资源、目标与约束是什么 | 规划、排队、调度、库存、网络优化 | 可行性、对偶/下界、现实约束遗漏 |
| 优化 | 数学性质允许精确方法还是近似搜索 | 线性/整数/非线性规划、启发式 | 局部/全局最优措辞、收敛、预算公平 |
| 微分方程 | 状态如何随时间/空间演化 | ODE/PDE、边初值、数值离散 | 稳定性、步长、边界、参数辨识 |
| 动力学 | 质量、能量、动量或状态转移规律是什么 | 牛顿/拉格朗日、状态空间、仿真 | 守恒、单位、初值、模型阶次 |
| 控制 | 要稳定、跟踪还是优化，观测与控制量是什么 | 反馈、PID、状态估计、最优/预测控制 | 可控可观、时延、饱和、闭环验证 |
| 信号处理 | 目标信息位于何种频带和时间尺度 | FFT、滤波、小波、时频分析 | 采样、混叠、窗、边界、下游有效性 |
| 机器学习 | 标签、样本独立性和决策代价是什么 | 树、SVM、集成、特征工程 | 泄漏、过拟合、校准、可解释性 |
| 深度学习 | 数据规模与结构是否支持表示学习 | CNN、RNN/LSTM、Transformer | 划分、算力、消融、多种子、伪特征 |
| 迁移学习 | 源域与目标域哪里相同、哪里不同 | 微调、域适配、特征对齐 | 负迁移、目标域证据、无迁移基线 |
| 空间统计 | 距离、邻接或区域尺度是否影响变量 | Kriging、空间回归、点过程 | 坐标系、空间泄漏、自相关、MAUP |
| GIS | 数据如何投影、叠加、缓冲和网络化 | 栅格/矢量、空间连接、地形与网络分析 | 投影单位、分辨率、拓扑、来源 |
| 多源融合 | 来源如何对齐、可靠性和相关误差如何处理 | 数据/特征/决策融合、Kalman、贝叶斯 | 时空同步、共同误差、缺源消融 |
| 不确定性 | 输入、参数、结构和场景哪些未知 | 区间、分布、bootstrap、Monte Carlo、情景 | 相关性、尾部、误差传播、覆盖 |
| 鲁棒优化 | 对哪些扰动必须保持可行或可接受 | 集合/分布鲁棒、机会约束、CVaR | 不确定集依据、保守性、样本外可行率 |
| 综合评价 | 抽象概念如何操作化并形成可审计指标 | AHP、熵权、TOPSIS、PCA/因子 | 指标代表性、重复、权重、排名敏感性 |

## 使用顺序

1. 在 [题型索引](PROBLEM_PATTERN_INDEX.md) 确认任务结构。
2. 在 [方法索引](METHOD_INDEX.md) 核对方法前提和误用。
3. 在 [验证指南](VALIDATION_GUIDE.md) 设计证据链。
4. 只有 [可追溯案例](EVIDENCE_CASES.md) 和已审核经验卡可作为具体论文证据。

<!-- AUTO-GENERATED START -->
## 已审核经验卡映射

> 下列映射直接来自 semantic_index.csv 中 complete/partial 条目；使用时仍应回看经验卡与 source_md。

### CSI

- 2025-B-003（partial）：[经验卡](../paper_notes/2025/B/2025-B-003.md) · [source_md](../knowledge_base/2025/B/B%E9%A2%98-%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E9%A9%B1%E5%8A%A8%E7%9A%84%E9%9D%A2%E5%90%91%20MIMO-OFDM%20%E7%9A%84%E9%93%BE%E8%B7%AF%E9%80%9F%E7%8E%87%E9%A2%84%E6%B5%8B.md)

### DAG

- 2025-A-001（partial）：[经验卡](../paper_notes/2025/A/2025-A-001.md) · [source_md](../knowledge_base/2025/A/A%E9%A2%98-1-%E9%80%9A%E7%94%A8%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%A4%84%E7%90%86%E5%99%A8%E4%B8%8B%E7%9A%84%E6%A0%B8%E5%86%85%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98.md)

### JRC

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### MIMO-OFDM

- 2025-B-003（partial）：[经验卡](../paper_notes/2025/B/2025-B-003.md) · [source_md](../knowledge_base/2025/B/B%E9%A2%98-%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E9%A9%B1%E5%8A%A8%E7%9A%84%E9%9D%A2%E5%90%91%20MIMO-OFDM%20%E7%9A%84%E9%93%BE%E8%B7%AF%E9%80%9F%E7%8E%87%E9%A2%84%E6%B5%8B.md)

### Pareto优化

- C24102890089（partial）：[经验卡](../paper_notes/2024/C/C24102890089.md) · [source_md](../knowledge_base/2024/C/C24102890089.md)

### Pareto前沿

- 2025-A-001（partial）：[经验卡](../paper_notes/2025/A/2025-A-001.md) · [source_md](../knowledge_base/2025/A/A%E9%A2%98-1-%E9%80%9A%E7%94%A8%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%A4%84%E7%90%86%E5%99%A8%E4%B8%8B%E7%9A%84%E6%A0%B8%E5%86%85%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98.md)
- A24103350007（partial）：[经验卡](../paper_notes/2024/A/A24103350007.md) · [source_md](../knowledge_base/2024/A/A24103350007.md)
- C24104220149（partial）：[经验卡](../paper_notes/2024/C/C24104220149.md) · [source_md](../knowledge_base/2024/C/C24104220149.md)

### RSSI/SINR

- B24102860287（partial）：[经验卡](../paper_notes/2024/B/B24102860287.md) · [source_md](../knowledge_base/2024/B/B24102860287.md)

### SINR

- 2025-B-003（partial）：[经验卡](../paper_notes/2025/B/2025-B-003.md) · [source_md](../knowledge_base/2025/B/B%E9%A2%98-%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E9%A9%B1%E5%8A%A8%E7%9A%84%E9%9D%A2%E5%90%91%20MIMO-OFDM%20%E7%9A%84%E9%93%BE%E8%B7%AF%E9%80%9F%E7%8E%87%E9%A2%84%E6%B5%8B.md)

### buffer生命周期

- 2025-A-001（partial）：[经验卡](../paper_notes/2025/A/2025-A-001.md) · [source_md](../knowledge_base/2025/A/A%E9%A2%98-1-%E9%80%9A%E7%94%A8%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%A4%84%E7%90%86%E5%99%A8%E4%B8%8B%E7%9A%84%E6%A0%B8%E5%86%85%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98.md)

### dBm换算

- B24102860287（partial）：[经验卡](../paper_notes/2024/B/B24102860287.md) · [source_md](../knowledge_base/2024/B/B24102860287.md)

### 不确定性

- 2025-B-003（partial）：[经验卡](../paper_notes/2025/B/2025-B-003.md) · [source_md](../knowledge_base/2025/B/B%E9%A2%98-%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E9%A9%B1%E5%8A%A8%E7%9A%84%E9%9D%A2%E5%90%91%20MIMO-OFDM%20%E7%9A%84%E9%93%BE%E8%B7%AF%E9%80%9F%E7%8E%87%E9%A2%84%E6%B5%8B.md)

### 不确定性分解

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### 主动勘探

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### 事件驱动仿真

- 2025-A-001（partial）：[经验卡](../paper_notes/2025/A/2025-A-001.md) · [source_md](../knowledge_base/2025/A/A%E9%A2%98-1-%E9%80%9A%E7%94%A8%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%A4%84%E7%90%86%E5%99%A8%E4%B8%8B%E7%9A%84%E6%A0%B8%E5%86%85%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98.md)

### 二维椭圆覆盖率

- D24103850092（partial）：[经验卡](../paper_notes/2024/D/D24103850092.md) · [source_md](../knowledge_base/2024/D/D24103850092.md)

### 交互与分组均值

- C24104220149（partial）：[经验卡](../paper_notes/2024/C/C24104220149.md) · [source_md](../knowledge_base/2024/C/C24104220149.md)

### 交互项

- C24103860012（partial）：[经验卡](../paper_notes/2024/C/C24103860012.md) · [source_md](../knowledge_base/2024/C/C24103860012.md)

### 交叉拟合

- B24103530099（partial）：[经验卡](../paper_notes/2024/B/B24103530099.md) · [source_md](../knowledge_base/2024/B/B24103530099.md)

### 交通流守恒

- E24102910005（partial）：[经验卡](../paper_notes/2024/E/E24102910005.md) · [source_md](../knowledge_base/2024/E/E24102910005.md)

### 代理标签

- 2025-D-002（partial）：[经验卡](../paper_notes/2025/D/2025-D-002.md) · [source_md](../knowledge_base/2025/D/D%E9%A2%98-%E5%9F%BA%E4%BA%8E%E5%A4%9A%E6%BA%90%E6%95%B0%E6%8D%AE%E8%9E%8D%E5%90%88%E7%9A%84%E4%BD%8E%E7%A9%BA%E6%B9%8D%E6%B5%81%E7%9B%91%E6%B5%8B%E4%B8%8E%E8%88%AA%E8%B7%AF%E4%BC%98%E5%8C%96.md)

### 代理量

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 全局约束

- A24103530117（partial）：[经验卡](../paper_notes/2024/A/A24103530117.md) · [source_md](../knowledge_base/2024/A/A24103530117.md)

### 公式还原

- C24106130096（partial）：[经验卡](../paper_notes/2024/C/C24106130096.md) · [source_md](../knowledge_base/2024/C/C24106130096.md)

### 冲击机理

- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 分组切分

- B24102860287（partial）：[经验卡](../paper_notes/2024/B/B24102860287.md) · [source_md](../knowledge_base/2024/B/B24102860287.md)

### 分组模型

- C24102890089（partial）：[经验卡](../paper_notes/2024/C/C24102890089.md) · [source_md](../knowledge_base/2024/C/C24102890089.md)

### 协变量混杂

- C24102890089（partial）：[经验卡](../paper_notes/2024/C/C24102890089.md) · [source_md](../knowledge_base/2024/C/C24102890089.md)

### 压力测试

- C24106130096（partial）：[经验卡](../paper_notes/2024/C/C24106130096.md) · [source_md](../knowledge_base/2024/C/C24106130096.md)

### 反事实

- E24102910005（partial）：[经验卡](../paper_notes/2024/E/E24102910005.md) · [source_md](../knowledge_base/2024/E/E24102910005.md)

### 变转速阶次

- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 可行性检查

- A24107120016（partial）：[经验卡](../paper_notes/2024/A/A24107120016.md) · [source_md](../knowledge_base/2024/A/A24107120016.md)

### 各向异性

- 2025-D-002（partial）：[经验卡](../paper_notes/2025/D/2025-D-002.md) · [source_md](../knowledge_base/2025/D/D%E9%A2%98-%E5%9F%BA%E4%BA%8E%E5%A4%9A%E6%BA%90%E6%95%B0%E6%8D%AE%E8%9E%8D%E5%90%88%E7%9A%84%E4%BD%8E%E7%A9%BA%E6%B9%8D%E6%B5%81%E7%9B%91%E6%B5%8B%E4%B8%8E%E8%88%AA%E8%B7%AF%E4%BC%98%E5%8C%96.md)

### 合法组合映射

- B24116640167（partial）：[经验卡](../paper_notes/2024/B/B24116640167.md) · [source_md](../knowledge_base/2024/B/B24116640167.md)

### 图文一致性

- B24104760033（partial）：[经验卡](../paper_notes/2024/B/B24104760033.md) · [source_md](../knowledge_base/2024/B/B24104760033.md)

### 在线疲劳损伤

- A24102940057（partial）：[经验卡](../paper_notes/2024/A/A24102940057.md) · [source_md](../knowledge_base/2024/A/A24102940057.md)

### 地址冲突

- 2025-A-001（partial）：[经验卡](../paper_notes/2025/A/2025-A-001.md) · [source_md](../knowledge_base/2025/A/A%E9%A2%98-1-%E9%80%9A%E7%94%A8%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%A4%84%E7%90%86%E5%99%A8%E4%B8%8B%E7%9A%84%E6%A0%B8%E5%86%85%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98.md)

### 坐标变换

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### 域偏移

- 2025-B-003（partial）：[经验卡](../paper_notes/2025/B/2025-B-003.md) · [source_md](../knowledge_base/2025/B/B%E9%A2%98-%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E9%A9%B1%E5%8A%A8%E7%9A%84%E9%9D%A2%E5%90%91%20MIMO-OFDM%20%E7%9A%84%E9%93%BE%E8%B7%AF%E9%80%9F%E7%8E%87%E9%A2%84%E6%B5%8B.md)
- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 复杂度触发

- C24106130096（partial）：[经验卡](../paper_notes/2024/C/C24106130096.md) · [source_md](../knowledge_base/2024/C/C24106130096.md)

### 外部基准

- F24910020063（partial）：[经验卡](../paper_notes/2024/F/F24910020063.md) · [source_md](../knowledge_base/2024/F/F24910020063.md)

### 外部效度

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 多基线比较

- B24104760033（partial）：[经验卡](../paper_notes/2024/B/B24104760033.md) · [source_md](../knowledge_base/2024/B/B24104760033.md)

### 多级缓存

- 2025-A-001（partial）：[经验卡](../paper_notes/2025/A/2025-A-001.md) · [source_md](../knowledge_base/2025/A/A%E9%A2%98-1-%E9%80%9A%E7%94%A8%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%A4%84%E7%90%86%E5%99%A8%E4%B8%8B%E7%9A%84%E6%A0%B8%E5%86%85%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98.md)

### 多重比较

- C24106130096（partial）：[经验卡](../paper_notes/2024/C/C24106130096.md) · [source_md](../knowledge_base/2024/C/C24106130096.md)

### 安全硬约束

- E24102910005（partial）：[经验卡](../paper_notes/2024/E/E24102910005.md) · [source_md](../knowledge_base/2024/E/E24102910005.md)

### 安全约束

- A24102940057（partial）：[经验卡](../paper_notes/2024/A/A24102940057.md) · [source_md](../knowledge_base/2024/A/A24102940057.md)

### 序列结构

- B24116640167（partial）：[经验卡](../paper_notes/2024/B/B24116640167.md) · [source_md](../knowledge_base/2024/B/B24116640167.md)

### 开合序列

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 开集拒识

- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 形状先验

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### 指标一致性

- B24116640167（partial）：[经验卡](../paper_notes/2024/B/B24116640167.md) · [source_md](../knowledge_base/2024/B/B24116640167.md)

### 故障特征频率

- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 数值稳定性

- F24910020063（partial）：[经验卡](../paper_notes/2024/F/F24910020063.md) · [source_md](../knowledge_base/2024/F/F24910020063.md)

### 数据同化

- 2025-D-002（partial）：[经验卡](../paper_notes/2025/D/2025-D-002.md) · [source_md](../knowledge_base/2025/D/D%E9%A2%98-%E5%9F%BA%E4%BA%8E%E5%A4%9A%E6%BA%90%E6%95%B0%E6%8D%AE%E8%9E%8D%E5%90%88%E7%9A%84%E4%BD%8E%E7%A9%BA%E6%B9%8D%E6%B5%81%E7%9B%91%E6%B5%8B%E4%B8%8E%E8%88%AA%E8%B7%AF%E4%BC%98%E5%8C%96.md)

### 时序泄漏

- E24102910005（partial）：[经验卡](../paper_notes/2024/E/E24102910005.md) · [source_md](../knowledge_base/2024/E/E24102910005.md)

### 时标与参考系

- F24910020063（partial）：[经验卡](../paper_notes/2024/F/F24910020063.md) · [source_md](../knowledge_base/2024/F/F24910020063.md)

### 时空对齐

- 2025-D-002（partial）：[经验卡](../paper_notes/2025/D/2025-D-002.md) · [source_md](../knowledge_base/2025/D/D%E9%A2%98-%E5%9F%BA%E4%BA%8E%E5%A4%9A%E6%BA%90%E6%95%B0%E6%8D%AE%E8%9E%8D%E5%90%88%E7%9A%84%E4%BD%8E%E7%A9%BA%E6%B9%8D%E6%B5%81%E7%9B%91%E6%B5%8B%E4%B8%8E%E8%88%AA%E8%B7%AF%E4%BC%98%E5%8C%96.md)

### 时空尺度

- D24103850092（partial）：[经验卡](../paper_notes/2024/D/D24103850092.md) · [source_md](../knowledge_base/2024/D/D24103850092.md)

### 时间切分

- A24103350007（partial）：[经验卡](../paper_notes/2024/A/A24103350007.md) · [source_md](../knowledge_base/2024/A/A24103350007.md)

### 有序标签

- 2025-B-003（partial）：[经验卡](../paper_notes/2025/B/2025-B-003.md) · [source_md](../knowledge_base/2025/B/B%E9%A2%98-%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E9%A9%B1%E5%8A%A8%E7%9A%84%E9%9D%A2%E5%90%91%20MIMO-OFDM%20%E7%9A%84%E9%93%BE%E8%B7%AF%E9%80%9F%E7%8E%87%E9%A2%84%E6%B5%8B.md)

### 机理派生特征

- C24103860012（partial）：[经验卡](../paper_notes/2024/C/C24103860012.md) · [source_md](../knowledge_base/2024/C/C24103860012.md)

### 权重

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 构念效度

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 概念操作化

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 欠定逆问题

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### 步长收敛

- F24910020063（partial）：[经验卡](../paper_notes/2024/F/F24910020063.md) · [source_md](../knowledge_base/2024/F/F24910020063.md)

### 残差修正

- A24107120016（partial）：[经验卡](../paper_notes/2024/A/A24107120016.md) · [source_md](../knowledge_base/2024/A/A24107120016.md)

### 滑动窗口

- A24103350007（partial）：[经验卡](../paper_notes/2024/A/A24103350007.md) · [source_md](../knowledge_base/2024/A/A24103350007.md)

### 滚动优化

- A24103530117（partial）：[经验卡](../paper_notes/2024/A/A24103530117.md) · [source_md](../knowledge_base/2024/A/A24103530117.md)

### 滚动预报

- 2025-D-002（partial）：[经验卡](../paper_notes/2025/D/2025-D-002.md) · [source_md](../knowledge_base/2025/D/D%E9%A2%98-%E5%9F%BA%E4%BA%8E%E5%A4%9A%E6%BA%90%E6%95%B0%E6%8D%AE%E8%9E%8D%E5%90%88%E7%9A%84%E4%BD%8E%E7%A9%BA%E6%B9%8D%E6%B5%81%E7%9B%91%E6%B5%8B%E4%B8%8E%E8%88%AA%E8%B7%AF%E4%BC%98%E5%8C%96.md)

### 滞后特征

- A24102940057（partial）：[经验卡](../paper_notes/2024/A/A24102940057.md) · [source_md](../knowledge_base/2024/A/A24102940057.md)

### 物理层抽象

- 2025-B-003（partial）：[经验卡](../paper_notes/2025/B/2025-B-003.md) · [source_md](../knowledge_base/2025/B/B%E9%A2%98-%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E9%A9%B1%E5%8A%A8%E7%9A%84%E9%9D%A2%E5%90%91%20MIMO-OFDM%20%E7%9A%84%E9%93%BE%E8%B7%AF%E9%80%9F%E7%8E%87%E9%A2%84%E6%B5%8B.md)

### 特征选择泄漏

- C24104220149（partial）：[经验卡](../paper_notes/2024/C/C24104220149.md) · [source_md](../knowledge_base/2024/C/C24104220149.md)

### 目标泄漏

- D24103850092（partial）：[经验卡](../paper_notes/2024/D/D24103850092.md) · [source_md](../knowledge_base/2024/D/D24103850092.md)

### 目标退化

- A24107120016（partial）：[经验卡](../paper_notes/2024/A/A24107120016.md) · [source_md](../knowledge_base/2024/A/A24107120016.md)

### 相关与因果

- B24116640167（partial）：[经验卡](../paper_notes/2024/B/B24116640167.md) · [source_md](../knowledge_base/2024/B/B24116640167.md)

### 空间泄漏

- D24103850092（partial）：[经验卡](../paper_notes/2024/D/D24103850092.md) · [source_md](../knowledge_base/2024/D/D24103850092.md)

### 空间相邻

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 窗口代理

- A24107120016（partial）：[经验卡](../paper_notes/2024/A/A24107120016.md) · [source_md](../knowledge_base/2024/A/A24107120016.md)

### 简单基线

- C24103860012（partial）：[经验卡](../paper_notes/2024/C/C24103860012.md) · [source_md](../knowledge_base/2024/C/C24103860012.md)

### 类别不均衡

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### 类别不平衡

- B24103530099（partial）：[经验卡](../paper_notes/2024/B/B24103530099.md) · [source_md](../knowledge_base/2024/B/B24103530099.md)
- B24104760033（partial）：[经验卡](../paper_notes/2024/B/B24104760033.md) · [source_md](../knowledge_base/2024/B/B24104760033.md)

### 类条件对齐

- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 级联误差传播

- B24103530099（partial）：[经验卡](../paper_notes/2024/B/B24103530099.md) · [source_md](../knowledge_base/2024/B/B24103530099.md)

### 组间泛化

- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 细长目标分割

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### 经验式残差

- C24102890089（partial）：[经验卡](../paper_notes/2024/C/C24102890089.md) · [source_md](../knowledge_base/2024/C/C24102890089.md)

### 结构化输出

- B24102860287（partial）：[经验卡](../paper_notes/2024/B/B24102860287.md) · [source_md](../knowledge_base/2024/B/B24102860287.md)

### 统计前提

- C24106130096（partial）：[经验卡](../paper_notes/2024/C/C24106130096.md) · [source_md](../knowledge_base/2024/C/C24106130096.md)

### 综合指数

- D24103850092（partial）：[经验卡](../paper_notes/2024/D/D24103850092.md) · [source_md](../knowledge_base/2024/D/D24103850092.md)

### 缺失与延迟

- A24103350007（partial）：[经验卡](../paper_notes/2024/A/A24103350007.md) · [source_md](../knowledge_base/2024/A/A24103350007.md)

### 联合输出

- B24104760033（partial）：[经验卡](../paper_notes/2024/B/B24104760033.md) · [source_md](../knowledge_base/2024/B/B24104760033.md)

### 自适应窗口

- A24103530117（partial）：[经验卡](../paper_notes/2024/A/A24103530117.md) · [source_md](../knowledge_base/2024/A/A24103530117.md)

### 虚拟传感器

- 2025-D-002（partial）：[经验卡](../paper_notes/2025/D/2025-D-002.md) · [source_md](../knowledge_base/2025/D/D%E9%A2%98-%E5%9F%BA%E4%BA%8E%E5%A4%9A%E6%BA%90%E6%95%B0%E6%8D%AE%E8%9E%8D%E5%90%88%E7%9A%84%E4%BD%8E%E7%A9%BA%E6%B9%8D%E6%B5%81%E7%9B%91%E6%B5%8B%E4%B8%8E%E8%88%AA%E8%B7%AF%E4%BC%98%E5%8C%96.md)

### 观测算子

- 2025-D-002（partial）：[经验卡](../paper_notes/2025/D/2025-D-002.md) · [source_md](../knowledge_base/2025/D/D%E9%A2%98-%E5%9F%BA%E4%BA%8E%E5%A4%9A%E6%BA%90%E6%95%B0%E6%8D%AE%E8%9E%8D%E5%90%88%E7%9A%84%E4%BD%8E%E7%A9%BA%E6%B9%8D%E6%B5%81%E7%9B%91%E6%B5%8B%E4%B8%8E%E8%88%AA%E8%B7%AF%E4%BC%98%E5%8C%96.md)

### 视频标定

- E24102910005（partial）：[经验卡](../paper_notes/2024/E/E24102910005.md) · [source_md](../knowledge_base/2024/E/E24102910005.md)

### 解释忠实度

- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 误差传播

- D24103850092（partial）：[经验卡](../paper_notes/2024/D/D24103850092.md) · [source_md](../knowledge_base/2024/D/D24103850092.md)

### 误差量级

- F24910020063（partial）：[经验卡](../paper_notes/2024/F/F24910020063.md) · [source_md](../knowledge_base/2024/F/F24910020063.md)

### 趋势-残差分解

- 2025-C-005（partial）：[经验卡](../paper_notes/2025/C/2025-C-005.md) · [source_md](../knowledge_base/2025/C/C%E9%A2%98-%E5%9F%BA%E4%BA%8E%E9%92%BB%E5%AD%94%E8%A3%82%E9%9A%99%E6%99%BA%E8%83%BD%E8%AF%86%E5%88%AB%E7%9A%84%E5%B2%A9%E4%BD%93%E7%BB%93%E6%9E%84%E9%9D%A2%E7%BD%91%E7%BB%9C%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E5%8C%BA%E7%A0%94%E7%A9%B6.md)

### 跨窗循环

- A24103530117（partial）：[经验卡](../paper_notes/2024/A/A24103530117.md) · [source_md](../knowledge_base/2024/A/A24103530117.md)

### 过采样泄漏

- B24103530099（partial）：[经验卡](../paper_notes/2024/B/B24103530099.md) · [source_md](../knowledge_base/2024/B/B24103530099.md)

### 适宜度

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 选择泄漏

- C24103860012（partial）：[经验卡](../paper_notes/2024/C/C24103860012.md) · [source_md](../knowledge_base/2024/C/C24103860012.md)

### 选模偏差

- C24104220149（partial）：[经验卡](../paper_notes/2024/C/C24104220149.md) · [source_md](../knowledge_base/2024/C/C24104220149.md)

### 重叠滑窗

- 2025-E-003（partial）：[经验卡](../paper_notes/2025/E/2025-E-003.md) · [source_md](../knowledge_base/2025/E/E%E9%A2%98-%E9%AB%98%E9%80%9F%E5%88%97%E8%BD%A6%E8%BD%B4%E6%89%BF%E6%99%BA%E8%83%BD%E6%95%85%E9%9A%9C%E8%AF%8A%E6%96%AD%E9%97%AE%E9%A2%98.md)

### 量纲

- F24910020063（partial）：[经验卡](../paper_notes/2024/F/F24910020063.md) · [source_md](../knowledge_base/2024/F/F24910020063.md)

### 阈值过拟合

- E24102910005（partial）：[经验卡](../paper_notes/2024/E/E24102910005.md) · [source_md](../knowledge_base/2024/E/E24102910005.md)

### 非补偿性

- 2025-F-004（partial）：[经验卡](../paper_notes/2025/F/2025-F-004.md) · [source_md](../knowledge_base/2025/F/F%E9%A2%98-%E6%B1%9F%E5%8D%97%E5%8F%A4%E5%85%B8%E5%9B%AD%E6%9E%97%E7%BE%8E%E5%AD%A6%E7%89%B9%E5%BE%81%E7%9A%84%E9%87%8F%E5%8C%96%E5%BB%BA%E6%A8%A1%E4%B8%8E%E5%88%86%E6%9E%90.md)

### 鲁棒调度

- A24102940057（partial）：[经验卡](../paper_notes/2024/A/A24102940057.md) · [source_md](../knowledge_base/2024/A/A24102940057.md)

### 鲁棒路径规划

- 2025-D-002（partial）：[经验卡](../paper_notes/2025/D/2025-D-002.md) · [source_md](../knowledge_base/2025/D/D%E9%A2%98-%E5%9F%BA%E4%BA%8E%E5%A4%9A%E6%BA%90%E6%95%B0%E6%8D%AE%E8%9E%8D%E5%90%88%E7%9A%84%E4%BD%8E%E7%A9%BA%E6%B9%8D%E6%B5%81%E7%9B%91%E6%B5%8B%E4%B8%8E%E8%88%AA%E8%B7%AF%E4%BC%98%E5%8C%96.md)

<!-- AUTO-GENERATED END -->
