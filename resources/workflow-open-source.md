# Creator Atlas · 资源与工具 · 开源工具工作流

> 定位：同一条制作链路的零订阅走法：12 个环节全部用开源（或免费开源优先）工具搭起来，附许可说明与短板对策；适合预算敏感、重视数据自主与可控性的创作者。
> 配套：《付费工具工作流》是同一条链路的付费走法，两页环节一一对应可混搭；深挖用[《开源工具推荐》](open-source.md)全清单。
> 声明：许可与版本信息核实于 2026-10，以各官方仓库最新信息为准；自托管工具的服务器成本另计。

## 选型原则

- 全开源可以跑完全流程：剪辑、音频、字幕、图形、录屏、直播、存储都有成熟方案，例外见文末「短板与对策」。
- 许可先看清：GPL 系改代码需开源衍生；MPL 折中；MIT / Apache / BSD 宽松；素材看 CC0 / CC-BY / CC-BY-NC 逐条授权。
- 涉及自托管的（Nextcloud、Owncast 等），按自己的运维能力选；没有运维精力就用桌面工具方案。
- 免费但闭源的工具（DaVinci Resolve 免费版、ocenaudio）可作过渡，但不算开源，本页单独标注。

## 工作流总览

| 环节 | 推荐起点 | 许可 |
| --- | --- | --- |
| 1 策划与写作 | Freeplane / Manuskript | GPL-2.0+ / GPL-3.0 |
| 2 拍摄辅助 | [QPrompt](https://qprompt.app/) | GPL-3.0 |
| 3 剪辑 | [Kdenlive](https://kdenlive.org/) | GPL-3.0 |
| 4 音频 | Audacity / Ardour | GPL-3.0 / GPL-2.0+ |
| 5 调色与视觉特效 | Natron / Blender | GPL-2.0+ / GPL |
| 6 动画与动效 | Synfig / Blender | GPL-3.0 / GPL |
| 7 字幕与转录 | Subtitle Edit / whisper.cpp | MIT |
| 8 图形与缩略图 | GIMP / Inkscape | GPL-3.0+ / GPL-2.0+ |
| 9 录屏与直播 | [OBS Studio](https://obsproject.com/) | GPL-2.0 |
| 10 素材获取 | Poly Haven / Freesound | CC0 / 逐条 CC |
| 11 存储与备份 | Syncthing / Kopia | MPL-2.0 / Apache-2.0 |
| 12 发布与数据 | yt-dlp / FreshRSS | Unlicense / AGPL-3.0 |

## 1. 策划与写作

把想法变成可执行方案：选题库、脚本、排期与结构梳理。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [Freeplane](https://www.freeplane.org/) | 思维导图与结构梳理 | Win / mac / Linux | GPL-2.0-or-later | 对 Xmind；FreeMind 分支，支持脚本扩展 |
| [Manuskript](https://www.theologeek.ch/manuskript/) | 写作与剧本大纲管理 | Win / mac / Linux | GPL-3.0 | 对 Scrivener；维护活跃 |
| [KIT Scenarist](https://kitscenarist.ru/en/) | 专业剧本写作 | 全平台（含移动端） | GPL-3.0 | 对 Final Draft；社区版基本停更，介意者用 Manuskript |

## 2. 拍摄辅助

手机或相机边的第二块屏：监看、提词与投屏录制。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [QPrompt](https://qprompt.app/) | 提词器（播报与录制辅助） | Win / mac / Linux | GPL-3.0 | 对提词 App；支持遥控、镜像与多种输入 |
| [Open Camera](https://opencamera.org.uk/) | Android 拍摄 App | Android | GPL-3.0+ | 对 FiLMiC Pro（轻量需求）；手动控制丰富 |
| [scrcpy](https://github.com/Genymobile/scrcpy) | 安卓投屏与录制 | 主机端全平台 | Apache-2.0 | 把手机画面接进电脑（对监看设备） |

> 场记与排期可用本库[《分镜表模板》](../templates/storyboard.md)与表格工具自建。

## 3. 剪辑

主力时间黑洞；开源剪辑已能覆盖从粗剪到精剪的完整流程。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [Kdenlive](https://kdenlive.org/) | 主力开源非线性剪辑 | Win / mac / Linux / BSD | GPL-3.0 | 对 Premiere Pro；多轨、代理与内置字幕工具完善 |
| [Shotcut](https://www.shotcut.org/) | 轻量开源剪辑 | Win / mac / Linux | GPL-3.0 | 对 CapCut 桌面版；格式兼容广 |
| [OpenShot](https://www.openshot.org/) | 入门级剪辑 | Win / mac / Linux | GPL-3.0-or-later | 对剪映免费档；功能较基础 |
| [LosslessCut](https://github.com/mifi/lossless-cut) | 无损切割与粗剪 | Win / mac / Linux | GPL-2.0 | 快速裁切不转码，素材整理利器 |
| [Avidemux](https://avidemux.sourceforge.net/) | 轻量线性编辑与滤镜 | Win / mac / Linux / BSD | GPL-2.0 | 简单任务顺手；更新节奏慢 |
| [HandBrake](https://handbrake.fr/) | 转码与压制 | Win / mac / Linux | GPL-2.0 | 对 Compressor、Media Encoder |
| [FFmpeg](https://ffmpeg.org/) | 命令行编解码与批处理 | 跨平台 | LGPL-2.1+ / GPL-2.0+（随构建） | 自动化流水线的底层工具 |
| [Blender（VSE）](https://www.blender.org/) | 3D 套件内置视频序列编辑器 | Win / mac / Linux | GPL | 会 Blender 的顺手可剪；专业剪辑仍需 NLE |

> DaVinci Resolve 免费版（免费但闭源）功能接近 Studio，是开源之外常用的免费过渡方案。

## 4. 音频

修复、降噪、混音与响度统一；深度修复是开源短板，见文末对策。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [Audacity](https://www.audacityteam.org/) | 多轨录音、编辑与降噪 | Win / mac / Linux | GPL-3.0 | 对 Audition（轻量场景） |
| [Ardour](https://ardour.org/) | 专业数字音频工作站 | Win / mac / Linux | GPL-2.0-or-later | 对 Pro Tools、Logic |
| [LMMS](https://lmms.io/) | 音乐制作与编曲 | Win / mac / Linux | GPL-2.0-or-later | 对 FL Studio |

> 例外说明：ocenaudio 免费但闭源，常被提及；坚持全开源请用 Audacity。

## 5. 调色与视觉特效

画面质感层：校正、合成与跟踪。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [Natron](https://natrongithub.github.io/) | 节点式合成与 VFX | Win / mac / Linux | GPL-2.0-or-later | 对 Nuke；社区维护，更新较慢 |
| [Blender](https://www.blender.org/) | 3D、合成与跟踪 | Win / mac / Linux | GPL | 对 Cinema 4D、Maya |

> 专业调色的开源对标有限；DaVinci Resolve 免费版（闭源免费）提供免费可用的调色与 Fusion，属过渡优选。

## 6. 动画与动效

把拍不到的东西画出来：2D 动画、逐帧与 3D。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [Synfig Studio](https://www.synfig.org/) | 2D 矢量动画（补间与骨骼） | Win / mac / Linux | GPL-3.0 | 对 After Effects 的轻量场景 |
| [OpenToonz](https://opentoonz.github.io/) | 专业 2D 动画制作 | Win / mac / Linux | BSD-3-Clause | 吉卜力工作流的开源版 |
| [Pencil2D](https://www.pencil2d.org/) | 逐帧手绘动画 | Win / mac / Linux / BSD | GPL-2.0 | 入门逐帧，界面简单 |
| [Krita](https://krita.org/) | 绘画与 2D 帧动画 | Win / mac / Linux / Android | GPL-3.0 | 对 Procreate、Photoshop 的绘画场景 |
| [Blender](https://www.blender.org/) | 3D 动画与动效 | Win / mac / Linux | GPL | 对 Cinema 4D、Maya |

## 7. 字幕与转录

可访问性与二次分发的基础设施；本地转录零成本且隐私好。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit) | 字幕编辑（时间轴、300+ 格式、转录集成） | Win / mac / Linux | MIT | 对 Rev 等字幕服务；5.x 起跨平台 |
| [Aegisub](https://aegisub.org/) | 高级字幕（ASS 特效与打轴） | Win / mac / Linux | BSD-3-Clause | 字幕特效；2026 年恢复维护 |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | 本地语音转文字推理 | 跨平台 | MIT | 对云端转录；离线、零成本 |
| [Buzz](https://github.com/chidiwilliams/buzz) | Whisper 图形界面转录工具 | Win / mac / Linux | MIT | 不想碰命令行的本地方案 |
| [FFmpeg](https://ffmpeg.org/) | 字幕抽取、烧录与批量处理 | 跨平台 | LGPL-2.1+ / GPL-2.0+（随构建） | 流水线自动化 |

## 8. 图形与缩略图

点击率的第一道门：封面、排版与素材图。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [GIMP](https://www.gimp.org/) | 位图编辑与合成 | Win / mac / Linux | GPL-3.0-or-later | 对 Photoshop |
| [Inkscape](https://inkscape.org/) | 矢量图形编辑（SVG 原生） | Win / mac / Linux | GPL-2.0-or-later | 对 Illustrator |
| [Scribus](https://www.scribus.net/) | 排版与 PDF 输出 | Win / mac / Linux | GPL-2.0-or-later | 对 InDesign |
| [Penpot](https://penpot.app/) | 设计与原型协作（可自托管） | Web / 自托管 | MPL-2.0 | 对 Figma |
| [draw.io 桌面版](https://github.com/jgraph/drawio-desktop) | 图表与流程图 | Win / mac / Linux | GPL-3.0 | 对图表类工具；内核为 Apache-2.0 |
| [FontForge](https://fontforge.org/) | 字体设计与编辑 | Win / mac / Linux | GPL-3.0+ / 部分 BSD | 字体定制与格式转换 |

## 9. 录屏与直播

教程、游戏与直播的技术底座；画面清晰度与稳定性优先。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [OBS Studio](https://obsproject.com/) | 录屏与多平台推流 | Win / mac / Linux | GPL-2.0 | 对 Camtasia、StreamYard 的推流场景 |
| [ShareX](https://getsharex.com/) | Windows 截图、录屏与自动化 | Win | GPL-3.0 | 对 Snagit（轻量场景） |
| [ScreenToGif](https://github.com/NickeManarin/ScreenToGif) | 屏幕录制为 GIF 与短片段 | Win | MS-PL | 教程动图；开发者另有继任项目 N-Studio |
| [Owncast](https://owncast.online/) | 自托管直播服务器 | Linux / macOS / Docker | MIT | 对 Twitch 自建直播；观看端全平台浏览器 |

> 多机位导播接近 vMix 的开源方案仍缺位，混搭时此处可用付费项。

## 10. 素材获取

库存素材、开放素材与字体：把版权风险前置解决。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [Poly Haven](https://polyhaven.com/) | HDRI、PBR 贴图与 3D 模型 | Web | CC0 | 场景与 3D 素材，可商用 |
| [ambientCG](https://ambientcg.com/) | 材质与贴图库 | Web | CC0 | 无缝贴图与 HDRI |
| [Freesound](https://freesound.org/) | 社区音效库 | Web | CC0 / CC-BY / CC-BY-NC（逐条） | 音效；注意 NC 不可商用 |
| [Openverse](https://openverse.org/) | 开放素材聚合搜索 | Web / API | 平台 MIT；素材各类 CC | 一处搜全网开放素材 |
| [Google Fonts](https://fonts.google.com/) | 开源字体库 | Web / 全平台下载 | OFL-1.1 为主 | 商用免费字体 |

> Pexels、Unsplash 等免费授权库不是开源项目，清单见[《素材与版权》](assets-rights.md)。

## 11. 存储、传输与备份

按 3-2-1 备份原则：本地一份、设备一份、异地一份。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [Syncthing](https://syncthing.net/) | 设备间点对点同步 | 全平台 | MPL-2.0 | 对 Dropbox（数据自控） |
| [Rclone](https://rclone.org/) | 云存储命令行同步 | 全平台 | MIT | 对接 70+ 存储后端 |
| [Nextcloud](https://nextcloud.com/) | 自托管网盘与协作 | 服务器 + 全端客户端 | AGPL-3.0 | 对 Google Drive、企业网盘 |
| [Seafile](https://www.seafile.com/) | 团队资料库网盘 | 服务器 + 客户端 | AGPL-3.0（组件混合） | 对 Dropbox 团队场景 |
| [LocalSend](https://localsend.org/) | 局域网跨平台互传 | 全平台 | Apache-2.0 | 对 AirDrop 的跨平台替代 |
| [Kopia](https://kopia.io/) | 加密增量备份 | Win / mac / Linux | Apache-2.0 | 快照与去重；目标可本地可云端 |
| [Duplicati](https://duplicati.com/) | 加密备份客户端 | Win / mac / Linux | MIT | 图形化备份，上手快 |
| [darktable](https://www.darktable.org/) | RAW 管理与显影 | Win / mac / Linux | GPL-3.0 | 对 Lightroom（显影流程） |
| [digiKam](https://www.digikam.org/) | 照片管理与整理 | Linux / Win / mac | GPL-2.0-or-later | 对 Lightroom（图库管理） |

## 12. 发布与数据

发布、监测与复盘的数据回路；平台侧数据以各创作后台为准。

| 工具 | 用途 | 平台 | 许可 | 选型提示（含付费对应） |
| --- | --- | --- | --- | --- |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | 视频下载与归档 | 跨平台 | Unlicense | 素材归档与备份（注意版权与平台条款） |
| [streamlink](https://streamlink.github.io/) | 直播流提取与转播 | Win / mac / Linux | BSD-2-Clause | 合规前提下录制直播流 |
| [FreshRSS](https://freshrss.org/) | RSS 阅读与新闻聚合 | 自托管（PHP） | AGPL-3.0 | 选题情报源 |
| [n8n](https://n8n.io/) | 工作流自动化 | 自托管 | fair-code（Sustainable Use License，非 OSI 开源） | 对 Zapier；商用前先读许可 |
| [Uptime Kuma](https://uptime.kuma.pet/) | 服务可用性监控 | 自托管 | MIT | 监控自己的站点与发布链路 |
| [changedetection.io](https://changedetection.io/) | 网页变更检测 | 自托管 | Apache-2.0 | 盯价格与页面更新 |
| [Matomo](https://matomo.org/) | 网站分析（隐私优先） | 自托管 | GPL-3.0 | 对 Google Analytics |
| [Umami](https://umami.is/) | 轻量网站分析 | 自托管 | MIT | 对 GA 的轻量场景 |

> 第三方数据工具（如飞瓜数据）多为付费，可比对[《付费工具工作流》](workflow-paid.md)与[《数据与平台》](data-platforms.md)。

## 短板与对策（开源弱项怎么补）

| 环节 | 短板 | 对策 |
| --- | --- | --- |
| 音频深度修复 | 去混响与行业级降噪无完全对标 | 录音端解决（见[《拍摄与制作》](../docs/methods/production.md)）；必要时买断 RX Elements（$99） |
| 动效模板生态 | AE 模板级资源少 | 用 Blender、Synfig 自制，或素材站免费模板（非开源） |
| 正版音乐库 | 开源项目不产出音乐 | 用 CC0 与免费授权音乐，或单曲授权付费曲目 |
| 多机位导播 | 对标 vMix 的成熟开源方案缺位 | OBS 插件可做基础多机位；专业导播保留付费项 |
| 专业调色 | 开源调色工具深度有限 | DaVinci Resolve 免费版（闭源免费）过渡 |

## 组合示例

| 组合 | 适合谁 | 工具搭配 | 成本 |
| --- | --- | --- | --- |
| 全开源 | 预算敏感、数据自控 | Freeplane + Kdenlive + Audacity + Subtitle Edit + whisper.cpp + GIMP + OBS + Syncthing + Kopia | 0 订阅（自托管服务器除外） |
| 混合 | 想省订阅又保关键环节 | Resolve 免费版（剪辑调色）+ 开源字幕（whisper.cpp）+ 付费素材库按需 | 素材订阅之外为 0 |
| 迁移组合 | 从 Adobe 全家桶迁出 | Kdenlive + GIMP + Inkscape + Audacity + Natron + Synfig | 0 订阅 |

## 延伸阅读

- [《付费工具工作流》](workflow-paid.md)：同一条链路的付费方案。
- [《开源工具推荐》](open-source.md)：14 类 193 项开源工具全清单（按工具类别深挖用）。
- [《拍摄设备》](gear.md) · [《素材与版权》](assets-rights.md) · [《AI 工具》](ai-tools.md) · [《数据与平台》](data-platforms.md)。
- 相关方法域：[《剪辑与后期》](../docs/methods/editing.md) · [《包装与分发》](../docs/methods/packaging.md)。
