<div align="center">

  <h2 align="center">Awesome AI Video Prompts 🎬</h2>
  <p align="center"><strong>做 AI 视频 / 动漫 / 短剧 / 讲解片,来这里挑提示词就够了。</strong></p>
  <p align="center">Curated prompt resources for AI video, anime & short-drama production.</p>
  <p align="center">
    <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
    <img src="https://img.shields.io/badge/updated-2026--10--15-blue?style=flat-square" alt="Updated 2026-10-15" />
    <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License MIT" />
  </p>
</div>

---

收录标准:**实测可复用、活跃维护(2026-09 后有更新)、星数或质量达标**。星级用 shields.io 实时徽章,无需手动核对快照。

## 它帮你做什么

不用再全网翻提示词。按你要做的东西直接对号入座:

| 你想做的东西 | 直接去 |
|---|---|
| 知识讲解 / 科普动画(主攻方向) | [AI 科普 / 知识讲解视频](#ai-科普--知识讲解视频主攻方向) |
| 短剧 / 漫剧 / 动漫番剧 | [动漫 / 短剧 / 漫剧制作](#动漫--短剧--漫剧制作) |
| 用 Claude Opus 5.5 写代码生成视频 | [Opus 5.5 代码生成视频](#opus-55-代码生成视频) |
| 找整段可复制的提示词案例 | [通用视频提示词案例库](#通用视频提示词案例库) |
| 给 Claude Code 装视频提示词产线 | [Claude Code Skill 产线](#claude-code-skill-产线) |
| 广告片 / TVC / 口播视频 | [商业片 / TVC / 口播](#商业片--tvc--口播) |
| 跟进模型与论文演进 | [论文与研究清单](#论文与研究清单) |
| 在本机直接出片 | [本地工作流](#本地工作流) |

## Contents

- [🎬 AI 科普 / 知识讲解视频(主攻方向)](#ai-科普--知识讲解视频主攻方向) — 讲解动画赛道,当前天花板是 Opus 代码生成
- [🎭 动漫 / 短剧 / 漫剧制作](#动漫--短剧--漫剧制作) — 剧本→分镜→出片的全流程 skill 套件
- [⌨️ Opus 5.5 代码生成视频](#opus-55-代码生成视频) — 生成可编辑的程序再渲染成视频
- [📋 通用视频提示词案例库](#通用视频提示词案例库) — 整段可复制的完整案例
- [🛠 Claude Code Skill 产线](#claude-code-skill-产线) — 装进 Claude Code 的提示词产线
- [💰 商业片 / TVC / 口播](#商业片--tvc--口播) — 广告、带货、口播视频
- [📄 论文与研究清单](#论文与研究清单) — 文生视频模型演进
- [🏠 本地工作流](#本地工作流参考) — 本机出片的现成栈
- [✨ 本仓库功能](#本仓库功能) — 每周自动巡检与停滞预警
- [💡 使用小贴士](#使用小贴士)
- [🕘 最近更新](#最近更新)
- [🤝 收录与共建](#收录与共建)
- [🙏 Acknowledgements](#acknowledgements)

---

## AI 科普 / 知识讲解视频(主攻方向)

讲解动画(explainer)赛道。当前效果天花板是 **Claude Opus 5.5 代码生成**(HTML / Canvas / Three.js / Manim)——本质是"生成可编辑的程序再渲染成视频",不是传统文生视频。用其他模型复刻时,**提示词结构(分镜叙事 + 视觉锚点 + 反 AI 感约束)比模型本身更重要**。

| 仓库 | 说明 |
|---|---|
| [xianyu110/awesome-claude-opus-5.5](https://github.com/xianyu110/awesome-claude-opus-5.5) ![](https://img.shields.io/github/stars/xianyu110/awesome-claude-opus-5.5?style=social&label=star) | **首选**:讲解动画专类 17 案(AI 简史 3 分钟、Transformer 是什么、随机微分方程、诺贝尔经济学讲解等),`#prompts` 段附原帖提示词原文,直接可抄。1019 全清单见 [ALL_CASES.md](https://github.com/xianyu110/awesome-claude-opus-5.5/blob/main/ALL_CASES.md) |
| [iart-ai/explainer-video-skills](https://github.com/iart-ai/explainer-video-skills) ![](https://img.shields.io/github/stars/iart-ai/explainer-video-skills?style=social&label=star) | Claude Code 讲解视频 skill:脚本→分镜→渲染带配音的讲解片、年度回顾、动画图表,全流程 |
| [yokel1121/muyang-flat-animation](https://github.com/yokel1121/muyang-flat-animation) ![](https://img.shields.io/github/stars/yokel1121/muyang-flat-animation?style=social&label=star) | 中文观点→纸上钢笔线稿 + 彩铅风知识讲解动画素材,中文科普赛道 |
| [Atharva-Kanherkar/chalkboard](https://github.com/Atharva-Kanherkar/chalkboard) ![](https://img.shields.io/github/stars/Atharva-Kanherkar/chalkboard?style=social&label=star) | 开源白板讲解视频:prompt → mp4,自托管 MIT,本地渲染管线 |
| [joeseesun/opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) ![](https://img.shields.io/github/stars/joeseesun/opus-video-prompts?style=social&label=star) | 54 个代码生成视频案例含讲解类,提示词整段可复制 |

> **复刻要点(自用备忘)**:Opus 5.5 讲解片的提示词共性 = ①分镜逐段叙事 + ②每镜一个视觉隐喻锚点 + ③显式禁用模板化动效(bounce / 粒子 / 发光)+ ④要求"代码可编辑"而非一次性渲染。这些约束移植到 GLM / Kimi / Gemini 上同样有效,效果损失主要在动画代码的物理感,可加"分步插值"缓解。

## 动漫 / 短剧 / 漫剧制作

| 仓库 | 说明 |
|---|---|
| [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) ![](https://img.shields.io/github/stars/zenstory-ai/drama-skills?style=social&label=star) | 开源 AI 短剧/漫剧创作 skill 全家桶:剧本→角色资产→分镜→图片/视频提示词→审查,11 个 skill,适配 Claude Code 与 Codex。中英双语,MIT |
| [gaoren7716-lab/anime-prompt-library](https://github.com/gaoren7716-lab/anime-prompt-library) ![](https://img.shields.io/github/stars/gaoren7716-lab/anime-prompt-library?style=social&label=star) | 动漫风格系统化提示词库:412 条目、五模型适配、抽卡池、示例画廊、稳定编码体系 |
| [huntingrin/seedance-anime-prompt-library](https://github.com/huntingrin/seedance-anime-prompt-library) ![](https://img.shields.io/github/stars/huntingrin/seedance-anime-prompt-library?style=social&label=star) | 100 条 Seedance 2.0 动漫视频提示词,带验证过的参考图、原帖出处与示例视频 |

## Opus 5.5 代码生成视频

与讲解动画板块有重叠,这里偏全集视角(讲解类专挑见上一节):

| 仓库 | 说明 |
|---|---|
| [xianyu110/awesome-claude-opus-5.5](https://github.com/xianyu110/awesome-claude-opus-5.5) ![](https://img.shields.io/github/stars/xianyu110/awesome-claude-opus-5.5?style=social&label=star) | 302 精选 Opus 5.5 视频/可视化案例 + 1019 完整清单:游戏、3D 场景、动效、讲解动画、交互可视化,附原帖/作者/点赞与能找到的提示词。附 [GitHub Pages 画廊](https://xianyu110.github.io/awesome-claude-opus-5.5/) |
| [joeseesun/opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) ![](https://img.shields.io/github/stars/joeseesun/opus-video-prompts?style=social&label=star) | Claude Opus 5.5 用代码生成视频:全网案例 + 54 个可直接复制的提示词 |

## 通用视频提示词案例库

| 仓库 | 说明 |
|---|---|
| [songguoxs/awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts) ![](https://img.shields.io/github/stars/songguoxs/awesome-video-prompts?style=social&label=star) | 50+ 完整案例(Veo3 / Veo3.1 / 即梦 / 可灵 / 海螺 / 豆包),含动漫战斗、黏土、乐高等风格,提示词整段可复制 |
| [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) ![](https://img.shields.io/github/stars/ai-boost/awesome-prompts?style=social&label=star) | 顶级 GPT 提示词合集,含 `video_gen_prompting.txt`(视频生成提示词方法论) |

## Claude Code Skill 产线

| 仓库 | 说明 |
|---|---|
| [jnMetaCode/ai-shortfilm-prompts](https://github.com/jnMetaCode/ai-shortfilm-prompts) ![](https://img.shields.io/github/stars/jnMetaCode/ai-shortfilm-prompts?style=social&label=star) | Claude Code Skill:任意点子 → 电影级、模型就绪的视频提示词(Sora / Kling 等) |
| [rediumvex/ai-video-generator-claude](https://github.com/rediumvex/ai-video-generator-claude) ![](https://img.shields.io/github/stars/rediumvex/ai-video-generator-claude?style=social&label=star) | 10 个 Claude skill 生成影棚级 Seedance 2.0 视频提示词 |
| [zhouwei713/seedance-prompt](https://github.com/zhouwei713/seedance-prompt) ![](https://img.shields.io/github/stars/zhouwei713/seedance-prompt?style=social&label=star) | Hermes skill:写实 AI 视频提示词,适配 Seedance 与文生视频模型 |
| [Yuyyxz/kling-prompt-engineering](https://github.com/Yuyyxz/kling-prompt-engineering) ![](https://img.shields.io/github/stars/Yuyyxz/kling-prompt-engineering?style=social&label=star) | 导演式可灵提示词工程指南(中英) |

## 商业片 / TVC / 口播

| 仓库 | 说明 |
|---|---|
| [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) ![](https://img.shields.io/github/stars/kaomei/stickman-video-director?style=social&label=star) | 文案 → 一分钟 Gemini Omni Flash 火柴人视频提示词包,多语种 README + 风格画廊 |
| [kaomei/hand-drawn-video-prompts](https://github.com/kaomei/hand-drawn-video-prompts) ![](https://img.shields.io/github/stars/kaomei/hand-drawn-video-prompts?style=social&label=star) | 中文口播稿 → 9:16 Q 版手绘视频提示词,科技人物 Q 版化 |
| [nutllwhy/seedance-tvc-director](https://github.com/nutllwhy/seedance-tvc-director) ![](https://img.shields.io/github/stars/nutllwhy/seedance-tvc-director?style=social&label=star) | Seedance 2.5 TVC 导演 skill:15s / 30s / 自定义广告片提示词、分镜、配音路由 |
| [T8mars/minimax-h3-prompt-skill-T8](https://github.com/T8mars/minimax-h3-prompt-skill-T8) ![](https://img.shields.io/github/stars/T8mars/minimax-h3-prompt-skill-T8?style=social&label=star) | MiniMax H3 + Seedance 2.0 创意 DNA 提示词案例与可安装 Skill |

## 论文与研究清单

| 仓库 | 说明 |
|---|---|
| [jianzhnie/awesome-text-to-video](https://github.com/jianzhnie/awesome-text-to-video) ![](https://img.shields.io/github/stars/jianzhnie/awesome-text-to-video?style=social&label=star) | 文生视频生成/合成综述与论文清单,跟进模型演进 |

## 本地工作流参考

自用配置备忘,按需替换成你自己的栈:

- **视频生成**: 任意 OpenAI 兼容网关接入 Grok Imagine / Seedance / 即梦等视频模型(支持图生视频参考图)
- **界面**: grok2api 类 WebUI(传图 + 流式出片),或直接用各模型官方网页
- **剧本侧**: `comic-drama-script` 类结构化剧本 skill 负责叙事骨架,提示词层参考上表 drama-skills

## 使用小贴士

- 提示词先抄结构再改内容:分镜节奏、视觉锚点、反 AI 感约束这三样是骨架,题材文案是皮。
- 跨模型移植时优先保留"逐镜叙事 + 显式禁用模板化动效",模型差异用"分步插值"类指令补偿。
- 星级徽章是实时的;发现某仓库半年没更新,就从列表里降级或移除,别留死链。

## 最近更新

- **2026-10-15**:转公开——新增 GitHub Actions 每周巡检(停滞/归档预警 Issue)+ 本仓库功能介绍;清理内部环境细节;License 由 CC0 改为 MIT。
- **2026-10-15**:README 大改版——参考 ai-boost/awesome-prompts 与 stickman-video-director 的结构:新增快速路由表、使用小贴士、本更新区;星数改为 shields.io 实时徽章,免去快照核对。
- **2026-10-15**:新增 AI 科普/知识讲解板块,设为主攻方向。
- **2026-10-14**:初始清单:AI 视频/动漫/漫剧提示词仓库精选。

仓库地址:[github.com/Lxcardoza993/lynx-awesome-video-prompts](https://github.com/Lxcardoza993/lynx-awesome-video-prompts)

## 本仓库功能

不只是链接收藏夹,自带一套自动化维护机制:

- **🤖 每周自动巡检**:`.github/workflows/monitor.yml` 每周一 03:00 UTC 自动跑 `scripts/monitor.py`,逐个核对 README 里 19 个仓库的存活、归档、最后 push 时间
- **⏰ 停滞预警**:某仓库 180 天没 push 或已归档,自动开一条汇总 Issue 提醒人工降级/移除,不静默腐烂
- **✅ 星数零维护**:所有星数走 shields.io 实时徽章,不用手动核对快照;README 的 updated 徽章由巡检自动刷新
- **🎯 快速路由**:"它帮你做什么"表格 + 分类目录,按你要做的东西直接跳转,不用全篇翻

## 收录与共建

**收录要求**

- 仓库 2026 年内活跃、描述准确、与视频/动漫提示词直接相关
- 实测可用优先:能整段复制的提示词 > 空洞的链接聚合

**计划补充**(排期中,还没核实完)

- Sora / Veo 官方提示词指南与 cookbook
- Runway / Pika / Luma 案例库
- 更多中文源(即梦/可灵/海螺社区帖)

欢迎提 PR / Issue 补充条目,附上一句话"为什么值得收"即可。

## Acknowledgements

- README 结构与巡检思路参考:[ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) 与 [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)
- 感谢 [linux.do](https://linux.do) 与 [OpenClaw 中文社区](https://clawd.org.cn/forum) 的讨论与分享——清单里不少条目最早来自这两个社区的推荐
- 感谢清单里每一个仓库的作者——是你们的实测与开源,让这份清单有东西可收
- Star 徽章由 [shields.io](https://shields.io) 提供

## License

MIT — 本仓库的编排与文案;所链接各仓库遵循各自 License。
