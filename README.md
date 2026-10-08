<div align="center">
<p><b>简体中文</b> · <a href="README.en.md">English</a></p>
<img src="assets/logo.svg" alt="Creator Atlas logo" width="150">
<h1>Creator Atlas · 视频创作者方法论全景手册</h1>
<p><strong>一个中文优先、结构化的开源视频创作知识库。</strong> 从定位选题、脚本叙事、拍摄制作、剪辑后期，到包装分发、增长复盘与变现经营：把「做视频」拆成 <strong>7 大方法域</strong> 与 <strong>8 类制作方法</strong>，全部外链逐条核查，平台规则标注核实时点。</p>
<p><strong>在线阅读：<a href="https://huanmoovo.github.io/creator-atlas/">https://huanmoovo.github.io/creator-atlas/</a> （支持 简体中文 / English 切换 · GitHub Pages，由 CI 自动部署）</strong></p>
<p><a href="https://github.com/HuanMoovo/creator-atlas/actions/workflows/lint.yml"><img src="https://github.com/HuanMoovo/creator-atlas/actions/workflows/lint.yml/badge.svg" alt="Lint"></a> <a href="https://github.com/HuanMoovo/creator-atlas/actions/workflows/links.yml"><img src="https://github.com/HuanMoovo/creator-atlas/actions/workflows/links.yml/badge.svg" alt="Link Check"></a> <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY--SA%204.0%20%2B%20MIT-blue.svg" alt="License: CC BY-SA 4.0 + MIT"></a> <a href="https://github.com/HuanMoovo/creator-atlas/stargazers"><img src="https://img.shields.io/github/stars/HuanMoovo/creator-atlas?style=flat&label=Stars&color=8b5cf6" alt="Stars"></a></p>
</div>

## 前言

视频创作的方法论从来不缺单点技巧。缺的是把技巧组织起来的骨架，以及一条从「想做视频」到「靠内容稳定产出」的完整路线。这个仓库补上这根骨架：按真实的创作顺序摆放知识，每个环节给出方法、步骤与验收标准。完整缘起见[前言](docs/preface.md)。

## 这是什么

一套覆盖视频创作全流程的中文开源手册：

- **讲清楚「怎么做」和「为什么」**，不给空话；数据与平台规则给出区间、口径与核实时点。
- **外链逐条核查**（发布前逐条验证 + CI 每周自动复查）。
- **结构设计科学**：方法域与制作方法各司其职、互相引用不重复；目录与长期规划见 [关于本库](docs/meta/design.md)。

## 内容地图

### 入门（docs/start/）

| 页 | 说明 |
| --- | --- |
| [视频创作全景](docs/start/what-is-creation.md) | 创作链路全貌、四条关键问题与上手路径 |
| [品类与赛道选择](docs/start/niche-choice.md) | 怎么选方向：受众、竞争与自身条件的三角 |
| [第一个视频](docs/start/first-video.md) | 手机与免费工具，从 0 到发布第一条视频 |
| [学习路径](docs/start/learning-path.md) | 零基础 / 进阶 / 团队三条路线与达标线 |
| [角色与技能地图](docs/start/roles-skills.md) | 单人创作与团队分工的岗位、技能对照 |

### 方法域（docs/methods/）

| 手册 | 说明 |
| --- | --- |
| [定位与选题](docs/methods/positioning.md) | 赛道、受众模型、选题漏斗与对标分析 |
| [脚本与叙事](docs/methods/script.md) | 结构、钩子、口播稿与两栏脚本 |
| [拍摄与制作](docs/methods/production.md) | 画面、灯光、收音与出镜表现的执行清单 |
| [剪辑与后期](docs/methods/editing.md) | 节奏、声音设计、字幕与交付规格 |
| [包装与分发](docs/methods/packaging.md) | 标题、封面、平台机制与多平台分发 |
| [增长与复盘](docs/methods/growth.md) | 指标体系、留存曲线诊断与迭代流程 |
| [变现与经营](docs/methods/monetization.md) | 平台分成、商单、自有产品与团队化 |

### 制作方法（docs/genres/）

- [制作方法总览](docs/genres/README.md)：8 类制作方法，含适用类型详解与完整工作流，整合覆盖百余种内容形态。

### 资源、模板与元信息

- [资源与工具](resources/README.md)：设备、软件、开源工具、素材、AI 工具与数据平台的核查过入口。
- [清单与模板](templates/README.md)：选题库、脚本、分镜、发布检查与复盘的即用模板。
- [术语表](GLOSSARY.md)：创作与平台术语中英对照。
- [关于本库](docs/meta/design.md) · [内容路线图](docs/meta/roadmap.md)。

## 三条推荐阅读路线

- **从零开始**：[前言](docs/preface.md) → [视频创作全景](docs/start/what-is-creation.md) → [第一个视频](docs/start/first-video.md) → [定位与选题](docs/methods/positioning.md)
- **涨不动求解**：[增长与复盘](docs/methods/growth.md) → [包装与分发](docs/methods/packaging.md) → [定位与选题](docs/methods/positioning.md)
- **团队与机构**：[角色与技能地图](docs/start/roles-skills.md) → [拍摄与制作](docs/methods/production.md) → [清单与模板](templates/README.md) → [变现与经营](docs/methods/monetization.md)

## 仓库结构

```text
docs/           手册正文（入门 / 方法域 / 制作方法 / 元信息）
resources/      资源与工具
templates/      清单与模板
site/           阅读站构建（Material for MkDocs）
scripts/        维护脚本（链接核查）
```

## 链接与事实核查

- 发布前对全部外链逐条验证；CI 每周自动复检。
- 平台规则、费率与阈值类内容均标注核实时点；行动前请以官方最新文档为准。

## 参与贡献

勘误、新增内容、工程改进都欢迎，见 [CONTRIBUTING.md](CONTRIBUTING.md) 与[行为准则](CODE_OF_CONDUCT.md)。

## Star 趋势

[![Star History Chart](https://api.star-history.com/svg?repos=HuanMoovo%2Fcreator-atlas&type=Date)](https://star-history.com/#HuanMoovo/creator-atlas&Date)

## 许可

文档内容采用 [CC BY-SA 4.0](LICENSE)，代码采用 [MIT](LICENSE-CODE)。

## 说明

手册内容参考了大量公开资料、平台官方文档与创作者访谈，版权归各自作者；文中的数字与规则以行动时点的官方最新信息为准。
