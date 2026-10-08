# Creator Atlas · 资源与工具 · 开源工具推荐

> 本页按创作流程收录值得使用的开源项目：从剪辑、字幕、音频到 AI 生成与素材管理，共 14 类、193 项。全部链接核实于 2026-10，CI 定期复检；商用与托管型工具见[软件与工具](software.md)与 [AI 工具](ai-tools.md)。
> 收录标准：持续维护、可获取源码、对创作流程有实际用途；同类收最主流的若干项。
> 许可提醒：各项目许可证不同（MIT、Apache-2.0、GPL、AGPL 等），商用前核对条款；AI 项目的模型权重许可常与代码许可分开，以官方说明为准。被收录不代表质量背书。

## 剪辑与后期

从入门剪辑到节点合成与矢量动画的主力选项。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Shotcut | 跨平台剪辑，格式兼容广 | [mltframework/shotcut](https://github.com/mltframework/shotcut) |
| Kdenlive | 功能全面的非线性剪辑 | [KDE/kdenlive](https://github.com/KDE/kdenlive) |
| OpenShot | 轻量剪辑，上手快 | [OpenShot/openshot-qt](https://github.com/OpenShot/openshot-qt) |
| Olive | 开发中的新一代剪辑器 | [olive-editor/olive](https://github.com/olive-editor/olive) |
| Flowblade | Linux 桌面剪辑 | [jliljebl/flowblade](https://github.com/jliljebl/flowblade) |
| Pitivi | GNOME 桌面剪辑 | [GNOME/pitivi](https://github.com/GNOME/pitivi) |
| Cinelerra-GG | Linux 老牌剪辑套件 | [cinelerra-gg.org](https://www.cinelerra-gg.org/) |
| Avidemux | 快速剪切与转换 | [avidemux.org](https://avidemux.org/) |
| LosslessCut | 无损剪切与去废片 | [mifi/lossless-cut](https://github.com/mifi/lossless-cut) |
| VidCutter | 无损分段的轻量工具 | [ozmartian/vidcutter](https://github.com/ozmartian/vidcutter) |
| Auto-Editor | 按静音自动粗剪 | [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) |
| FFmpeg | 转码与自动化的命令行核心 | [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) |
| MoviePy | Python 脚本化剪辑 | [Zulko/moviepy](https://github.com/Zulko/moviepy) |
| VapourSynth | 高级视频处理框架 | [vapoursynth/vapoursynth](https://github.com/vapoursynth/vapoursynth) |
| AviSynth+ | 脚本化处理老牌框架 | [AviSynth/AviSynthPlus](https://github.com/AviSynth/AviSynthPlus) |
| Natron | 节点式合成与抠像 | [NatronGitHub/Natron](https://github.com/NatronGitHub/Natron) |
| Blender | 三维动画，含序列编辑与追踪 | [blender/blender](https://github.com/blender/blender) |
| Friction | 矢量动效制作 | [friction2d/friction](https://github.com/friction2d/friction) |
| Synfig | 2D 矢量动画 | [synfig/synfig](https://github.com/synfig/synfig) |
| OpenToonz | 专业 2D 动画制作 | [opentoonz/opentoonz](https://github.com/opentoonz/opentoonz) |
| Tahoma2D | OpenToonz 的友好分支 | [Tahoma2D/Tahoma2D](https://github.com/Tahoma2D/Tahoma2D) |
| Pencil2D | 手绘逐帧动画 | [pencil2d/pencil](https://github.com/pencil2d/pencil) |
| Glaxnimate | 矢量动画，适合字幕动效 | [glaxnimate.mattbas.org](https://glaxnimate.mattbas.org/) |

## 字幕与转录

语音转文字、字幕编辑与多语翻译。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Whisper | 语音转文字基线模型 | [openai/whisper](https://github.com/openai/whisper) |
| whisper.cpp | 本地轻量转写引擎 | [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) |
| faster-whisper | 提速版推理实现 | [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) |
| WhisperX | 带词级时间轴的转写 | [m-bain/whisperX](https://github.com/m-bain/whisperX) |
| FunASR | 中文转写工具箱 | [modelscope/FunASR](https://github.com/modelscope/FunASR) |
| SenseVoice | 多语种语音理解 | [FunAudioLLM/SenseVoice](https://github.com/FunAudioLLM/SenseVoice) |
| Vosk | 离线轻量识别 | [alphacep/vosk-api](https://github.com/alphacep/vosk-api) |
| Buzz | 桌面转写应用 | [chidiwilliams/buzz](https://github.com/chidiwilliams/buzz) |
| Aegisub | 字幕时间轴编辑 | [Aegisub/Aegisub](https://github.com/Aegisub/Aegisub) |
| Subtitle Edit | 字幕编辑与翻译 | [SubtitleEdit/subtitleedit](https://github.com/SubtitleEdit/subtitleedit) |
| danmaku2ass | 弹幕转字幕文件 | [m13253/danmaku2ass](https://github.com/m13253/danmaku2ass) |
| LibreTranslate | 自建翻译服务 | [LibreTranslate/LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) |
| Argos Translate | 离线翻译库 | [argosopentech/argos-translate](https://github.com/argosopentech/argos-translate) |

## 音频

录音编辑、降噪、分轨与音乐制作。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Audacity | 录音编辑与降噪 | [audacity/audacity](https://github.com/audacity/audacity) |
| Ardour | 专业数字音频工作站 | [Ardour/ardour](https://github.com/Ardour/ardour) |
| LMMS | 音乐制作工作站 | [LMMS/lmms](https://github.com/LMMS/lmms) |
| Zrythm | 现代界面 DAW | [zrythm/zrythm](https://github.com/zrythm/zrythm) |
| MuseScore | 乐谱制作 | [musescore/MuseScore](https://github.com/musescore/MuseScore) |
| Hydrogen | 鼓机 | [hydrogen-music/hydrogen](https://github.com/hydrogen-music/hydrogen) |
| Surge XT | 开源合成器 | [surge-synthesizer/surge](https://github.com/surge-synthesizer/surge) |
| Vital | 频谱合成器 | [mtytel/vital](https://github.com/mtytel/vital) |
| Ultimate Vocal Remover | 人声与伴奏分离 | [Anjok07/ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui) |
| Demucs | 高质量音源分离 | [adefossez/demucs](https://github.com/adefossez/demucs) |
| DeepFilterNet | 深度语音降噪 | [Rikorose/DeepFilterNet](https://github.com/Rikorose/DeepFilterNet) |
| RNNoise | 实时降噪库 | [xiph/rnnoise](https://github.com/xiph/rnnoise) |
| NoiseTorch | 麦克风实时降噪 | [noisetorch/NoiseTorch](https://github.com/noisetorch/NoiseTorch) |
| Sonic Visualiser | 音频可视化分析 | [sonic-visualiser/sonic-visualiser](https://github.com/sonic-visualiser/sonic-visualiser) |

## 录屏、直播与截图

屏幕捕获、直播推流与截图标注。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| OBS Studio | 录屏与直播主力 | [obsproject/obs-studio](https://github.com/obsproject/obs-studio) |
| ShareX | Windows 截图与录屏 | [ShareX/ShareX](https://github.com/ShareX/ShareX) |
| ScreenToGif | 录制为 GIF 与视频 | [NickeManarin/ScreenToGif](https://github.com/NickeManarin/ScreenToGif) |
| Kap | macOS 录屏 | [wulkano/Kap](https://github.com/wulkano/Kap) |
| Screenity | 浏览器内录屏 | [alyssaxuu/screenity](https://github.com/alyssaxuu/screenity) |
| Cap | 开源版 Loom | [CapSoftware/Cap](https://github.com/CapSoftware/Cap) |
| vokoscreenNG | Linux 录屏 | [vkohaupt/vokoscreenNG](https://github.com/vkohaupt/vokoscreenNG) |
| Flameshot | 截图与标注 | [flameshot-org/flameshot](https://github.com/flameshot-org/flameshot) |
| Owncast | 自建直播站 | [owncast/owncast](https://github.com/owncast/owncast) |
| Restreamer | 自建多平台推流 | [datarhei/restreamer](https://github.com/datarhei/restreamer) |
| MediaMTX | 流媒体服务器 | [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) |
| BililiveRecorder | 直播录制（B 站） | [BililiveRecorder/BililiveRecorder](https://github.com/BililiveRecorder/BililiveRecorder) |
| Liquidsoap | 播客与电台音频流 | [savonet/liquidsoap](https://github.com/savonet/liquidsoap) |
| Move Transition | OBS 转场插件 | [exeldro/obs-move-transition](https://github.com/exeldro/obs-move-transition) |
| Background Removal | OBS 实时抠像（AI） | [royshil/obs-backgroundremoval](https://github.com/royshil/obs-backgroundremoval) |
| Advanced Scene Switcher | OBS 场景自动化 | [WarmUpTill/SceneSwitcher](https://github.com/WarmUpTill/SceneSwitcher) |

## 编码、封装与压制

上传前的转码、封装与媒体信息核对。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| HandBrake | 图形化转码压制 | [HandBrake/HandBrake](https://github.com/HandBrake/HandBrake) |
| MKVToolNix | 封装与轨道管理 | [mkvtoolnix.download](https://mkvtoolnix.download/) |
| SVT-AV1 | 高效率编码器 | [AOMediaCodec/SVT-AV1](https://github.com/AOMediaCodec/SVT-AV1) |

> 批量参数化压制直接用 FFmpeg（见上）；导出规格参考[《剪辑与后期》](../docs/methods/editing.md)。

## 下载与素材获取

素材收集、归档与直播流拉取。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| yt-dlp | 视频下载主力 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) |
| Seal | Android 下载前端 | [JunkFood02/Seal](https://github.com/JunkFood02/Seal) |
| Parabolic | GNOME 下载前端 | [NickvisionApps/Parabolic](https://github.com/NickvisionApps/Parabolic) |
| MeTube | 自建下载的网页界面 | [alexta69/metube](https://github.com/alexta69/metube) |
| Tartube | 桌面下载管理 | [axcore/tartube](https://github.com/axcore/tartube) |
| Streamlink | 直播流拉取 | [streamlink/streamlink](https://github.com/streamlink/streamlink) |
| gallery-dl | 图站批量下载 | [mikf/gallery-dl](https://github.com/mikf/gallery-dl) |
| you-get | 通用媒体下载 | [soimort/you-get](https://github.com/soimort/you-get) |
| lux | Go 实现的下载器 | [iawia002/lux](https://github.com/iawia002/lux) |
| Cobalt | 自建下载服务 | [imputnet/cobalt](https://github.com/imputnet/cobalt) |
| JDownloader | 网盘与批量下载 | [jdownloader.org](https://jdownloader.org/) |
| aria2 | 命令行下载核心 | [aria2/aria2](https://github.com/aria2/aria2) |
| Motrix | aria2 图形界面 | [agalwood/Motrix](https://github.com/agalwood/Motrix) |
| N_m3u8DL-RE | 流媒体分片下载 | [nilaoda/N_m3u8DL-RE](https://github.com/nilaoda/N_m3u8DL-RE) |
| BBDown | B 站视频下载 | [nilaoda/BBDown](https://github.com/nilaoda/BBDown) |

## 图像与设计

封面、缩略图与图形素材制作。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| GIMP | 图像编辑 | [gimp.org](https://www.gimp.org/) |
| Krita | 绘画与逐帧动画 | [KDE/krita](https://github.com/KDE/krita) |
| Inkscape | 矢量图形 | [inkscape.org](https://inkscape.org/) |
| Penpot | 在线协作设计 | [penpot/penpot](https://github.com/penpot/penpot) |
| Excalidraw | 手绘风示意图 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) |
| diagrams.net | 流程图与结构图 | [jgraph/drawio](https://github.com/jgraph/drawio) |
| Upscayl | 图片 AI 放大 | [upscayl/upscayl](https://github.com/upscayl/upscayl) |
| chaiNNer | 节点式图像处理 | [chaiNNer-org/chaiNNer](https://github.com/chaiNNer-org/chaiNNer) |

## 字体与图标

封面与字幕用到的开源字库、图标与表情资源。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Noto CJK | 多语种无衬线字库 | [notofonts/noto-cjk](https://github.com/notofonts/noto-cjk) |
| 思源黑体 | 黑体家族 | [adobe-fonts/source-han-sans](https://github.com/adobe-fonts/source-han-sans) |
| 思源宋体 | 衬线家族 | [adobe-fonts/source-han-serif](https://github.com/adobe-fonts/source-han-serif) |
| 霞鹜文楷 | 楷体风格中文 | [lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai) |
| 得意黑 | 标题风格字体 | [atelier-anchor/smiley-sans](https://github.com/atelier-anchor/smiley-sans) |
| Inter | 界面西文字体 | [rsms/inter](https://github.com/rsms/inter) |
| Fira Sans | Mozilla 西文字体 | [mozilla/Fira](https://github.com/mozilla/Fira) |
| JetBrains Mono | 代码等宽字体 | [JetBrains/JetBrainsMono](https://github.com/JetBrains/JetBrainsMono) |
| Lucide | 通用图标库 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide) |
| Tabler Icons | 图标集合 | [tabler/tabler-icons](https://github.com/tabler/tabler-icons) |
| Font Awesome | 老牌图标库 | [FortAwesome/Font-Awesome](https://github.com/FortAwesome/Font-Awesome) |
| Material Symbols | Material 图标 | [google/material-design-icons](https://github.com/google/material-design-icons) |
| Twemoji | 表情符号资源 | [jdecked/twemoji](https://github.com/jdecked/twemoji) |
| OpenMoji | 开源表情集 | [hfg-gmuend/openmoji](https://github.com/hfg-gmuend/openmoji) |

## AI 工具

生成、增强与修复方向的开源项目；商用 AI 服务见 [AI 工具](ai-tools.md)。

### 图像生成与处理

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Stable Diffusion WebUI | 经典生图界面 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) |
| ComfyUI | 节点式生成工作流 | [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) |
| Fooocus | 极简生图界面 | [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus) |
| InvokeAI | 团队向生成平台 | [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) |
| stable-diffusion.cpp | 本地轻量推理 | [leejet/stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) |
| rembg | 图片背景移除 | [danielgatis/rembg](https://github.com/danielgatis/rembg) |
| IOPaint | 图片擦除与重绘 | [Sanster/IOPaint](https://github.com/Sanster/IOPaint) |

### 视频生成

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Wan 2.2 | 开源视频生成 | [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) |
| HunyuanVideo | 混元视频生成 | [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) |
| LTX-Video | 实时级视频生成 | [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) |
| Mochi | 高质量视频生成 | [genmoai/mochi](https://github.com/genmoai/mochi) |
| CogVideoX | 智谱视频生成 | [THUDM/CogVideo](https://github.com/THUDM/CogVideo) |
| Open-Sora | 开源复现套件 | [hpcaitech/Open-Sora](https://github.com/hpcaitech/Open-Sora) |
| FramePack | 低显存长视频生成 | [lllyasviel/FramePack](https://github.com/lllyasviel/FramePack) |

### 语音与数字人

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| GPT-SoVITS | 少样本语音克隆 | [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) |
| Fish Speech | 多语种语音合成 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) |
| CosyVoice | 语音合成与克隆 | [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) |
| F5-TTS | 轻量语音克隆 | [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS) |
| ChatTTS | 对话式语音合成 | [2noise/ChatTTS](https://github.com/2noise/ChatTTS) |
| Coqui TTS | 语音合成工具箱 | [coqui-ai/TTS](https://github.com/coqui-ai/TTS) |
| Piper | 轻量离线合成 | [rhasspy/piper](https://github.com/rhasspy/piper) |
| RVC | 歌声与音色转换 | [RVC-Project/Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) |
| SadTalker | 图片生成说话视频 | [OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker) |
| Wav2Lip | 口型同步 | [Rudrabha/Wav2Lip](https://github.com/Rudrabha/Wav2Lip) |
| LivePortrait | 肖像驱动动画 | [KwaiVGI/LivePortrait](https://github.com/KwaiVGI/LivePortrait) |
| LatentSync | 高精度口型同步 | [bytedance/LatentSync](https://github.com/bytedance/LatentSync) |

### 音乐与音效生成

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| MusicGen | 文本生成音乐 | [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) |
| Stable Audio Open | 音频生成模型 | [Stability-AI/stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) |
| ACE-Step | 音乐生成基础模型 | [ace-step/ACE-Step](https://github.com/ace-step/ACE-Step) |
| DiffRhythm | 快速整曲生成 | [ASLP-lab/DiffRhythm](https://github.com/ASLP-lab/DiffRhythm) |
| MMAudio | 视频转音效 | [hkchengrex/MMAudio](https://github.com/hkchengrex/MMAudio) |
| HunyuanVideo-Foley | 视频音效生成 | [Tencent-Hunyuan/HunyuanVideo-Foley](https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley) |

### 修复与增强

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Real-ESRGAN | 通用超分 | [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) |
| GFPGAN | 人脸修复 | [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN) |
| CodeFormer | 人脸复原 | [sczhou/CodeFormer](https://github.com/sczhou/CodeFormer) |
| Practical-RIFE | 插帧补帧 | [hzwer/Practical-RIFE](https://github.com/hzwer/Practical-RIFE) |
| FILM | 大位移插帧 | [google-research/frame-interpolation](https://github.com/google-research/frame-interpolation) |
| Video2X | 视频放大套件 | [k4yt3x/video2x](https://github.com/k4yt3x/video2x) |
| Anime4K | 动画实时放大 | [bloc97/Anime4K](https://github.com/bloc97/Anime4K) |

> AI 生成内容按平台要求披露；模型权重许可常与代码许可分开，商用前以官方说明为准。

## 素材库、播放与管理

素材检索、审片与媒体资料管理。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Openverse | CC 素材搜索引擎 | [WordPress/openverse](https://github.com/WordPress/openverse) |
| VLC | 万能播放器 | [videolan/vlc](https://github.com/videolan/vlc) |
| mpv | 轻量高画质播放器 | [mpv-player/mpv](https://github.com/mpv-player/mpv) |
| IINA | macOS 播放器 | [iina/iina](https://github.com/iina/iina) |
| MediaInfo | 编码信息查看 | [MediaArea/MediaInfo](https://github.com/MediaArea/MediaInfo) |
| TagSpaces | 素材标注管理 | [tagspaces/tagspaces](https://github.com/tagspaces/tagspaces) |
| Allusion | 参考图管理 | [allusion-app/Allusion](https://github.com/allusion-app/Allusion) |
| Hydrus Network | 媒体标签库 | [hydrusnetwork/hydrus](https://github.com/hydrusnetwork/hydrus) |
| Immich | 自建照片与素材库 | [immich-app/immich](https://github.com/immich-app/immich) |

## 整理、备份与传输

重复文件清理、备份同步与跨设备传输。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Czkawka | 重复文件清理 | [qarmin/czkawka](https://github.com/qarmin/czkawka) |
| rclone | 云盘同步与备份 | [rclone/rclone](https://github.com/rclone/rclone) |
| Syncthing | 设备间持续同步 | [syncthing/syncthing](https://github.com/syncthing/syncthing) |
| LocalSend | 局域网快传 | [localsend/localsend](https://github.com/localsend/localsend) |
| croc | 命令行快传 | [schollz/croc](https://github.com/schollz/croc) |
| FileZilla | FTP 客户端 | [filezilla-project.org](https://filezilla-project.org/) |
| WinSCP | Windows 文件传输 | [winscp/winscp](https://github.com/winscp/winscp) |
| 7-Zip | 压缩打包 | [7-zip.org](https://www.7-zip.org/) |
| PeaZip | 跨平台压缩 | [peazip/PeaZip](https://github.com/peazip/PeaZip) |

## 笔记与内容管理

选题、脚本与知识库管理。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Logseq | 大纲式知识库 | [logseq/logseq](https://github.com/logseq/logseq) |
| Joplin | 跨端笔记 | [laurent22/joplin](https://github.com/laurent22/joplin) |
| TriliumNext | 层级知识库 | [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium) |
| 思源笔记 | 本地优先笔记 | [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) |
| AppFlowy | Notion 开源替代 | [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) |
| AFFiNE | 文档与白板 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) |
| Zettlr | 长文写作 | [Zettlr/Zettlr](https://github.com/Zettlr/Zettlr) |
| Manuskript | 剧本与长文撰写 | [olivierkes/manuskript](https://github.com/olivierkes/manuskript) |
| Vikunja | 任务与排期 | [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja) |
| HedgeDoc | 协作 Markdown | [hedgedoc/hedgedoc](https://github.com/hedgedoc/hedgedoc) |

## 发布、监测与自动化

多平台发布、竞品与热点监测、流程自动化。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Postiz | 社媒排期发布 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) |
| Mixpost | 自建发布面板 | [inovector/mixpost](https://github.com/inovector/mixpost) |
| n8n | 工作流自动化 | [n8n-io/n8n](https://github.com/n8n-io/n8n) |
| TubeArchivist | 自建视频归档 | [tubearchivist/tubearchivist](https://github.com/tubearchivist/tubearchivist) |
| Invidious | 轻量视频前端 | [iv-org/invidious](https://github.com/iv-org/invidious) |
| RSSHub | 把站点变成 RSS | [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub) |
| FreshRSS | 自建 RSS 阅读器 | [FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS) |
| changedetection.io | 页面变动监测 | [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) |

## 网站、文档与识别

个人站点、文档工具与文字识别。

| 工具 | 用途 | 入口 |
| --- | --- | --- |
| Astro | 内容站框架 | [withastro/astro](https://github.com/withastro/astro) |
| Hugo | 快速静态站 | [gohugoio/hugo](https://github.com/gohugoio/hugo) |
| Ghost | 博客与订阅 | [TryGhost/Ghost](https://github.com/TryGhost/Ghost) |
| WordPress | 建站系统 | [WordPress/WordPress](https://github.com/WordPress/WordPress) |
| MkDocs | 文档站框架（本站同源） | [mkdocs/mkdocs](https://github.com/mkdocs/mkdocs) |
| Material for MkDocs | 文档主题（本站所用） | [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material) |
| Pandoc | 文档格式转换 | [jgm/pandoc](https://github.com/jgm/pandoc) |
| Umami | 自建网站分析 | [umami-software/umami](https://github.com/umami-software/umami) |
| Listmonk | 自建邮件订阅 | [knadh/listmonk](https://github.com/knadh/listmonk) |
| Umi-OCR | 批量截图识别 | [hiroi-sora/Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) |
| Tesseract | OCR 引擎 | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) |
| PaddleOCR | 中文 OCR 工具箱 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |

## 收录说明

- 失效链接与值得收录的项目，欢迎提 Issue 勘误；同类出现更优选择时本页会替换更新。
- 完整资源版图见[资源与工具](README.md)总目录。
