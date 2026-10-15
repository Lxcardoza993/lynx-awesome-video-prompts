# Awesome AI Video Prompts

> 精选 AI 视频/动漫/短剧提示词资源库 —— GitHub 仓库、Skill 套件与案例库,持续更新。
> Curated prompt resources for AI video, anime & short-drama production.

收录标准:活跃维护(2026-09 后有更新)、内容实测可复用、星数或质量达标。星数为 2026-10-15 快照。

## Contents

- [动漫 / 短剧 / 漫剧制作](#动漫--短剧--漫剧制作)
- [Opus 5.5 代码生成视频](#opus-55-代码生成视频)
- [通用视频提示词案例库](#通用视频提示词案例库)
- [Claude Code Skill 产线](#claude-code-skill-产线)
- [商业片 / TVC / 口播](#商业片--tvc--口播)
- [论文与研究清单](#论文与研究清单)
- [本地工作流](#本地工作流)

## 动漫 / 短剧 / 漫剧制作

| 仓库 | ⭐ | 说明 |
|---|---|---|
| [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) | 2887 | 开源 AI 短剧/漫剧创作 skill 全家桶:剧本→角色资产→分镜→图片/视频提示词→审查,11 个 skill,适配 Claude Code 与 Codex。中英双语,MIT |
| [gaoren7716-lab/anime-prompt-library](https://github.com/gaoren7716-lab/anime-prompt-library) | 1 | 动漫风格系统化提示词库:412 条目、五模型适配、抽卡池、示例画廊、稳定编码体系 |
| [huntingrin/seedance-anime-prompt-library](https://github.com/huntingrin/seedance-anime-prompt-library) | 1 | 100 条 Seedance 2.0 动漫视频提示词,带验证过的参考图、原帖出处与示例视频 |

## Opus 5.5 代码生成视频

| 仓库 | ⭐ | 说明 |
|---|---|---|
| [xianyu110/awesome-claude-opus-5.5](https://github.com/xianyu110/awesome-claude-opus-5.5) | 52 | 302 精选 Claude Opus 5.5 视频/可视化案例 + 1019 完整清单:游戏、3D 场景、动效、讲解动画、交互可视化,附原帖/作者/点赞与能找到的提示词。附 [GitHub Pages 画廊](https://xianyu110.github.io/awesome-claude-opus-5.5/) |
| [joeseesun/opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) | 342 | Claude Opus 5.5 用代码生成视频:全网案例 + 54 个可直接复制的提示词 |

## 通用视频提示词案例库

| 仓库 | ⭐ | 说明 |
|---|---|---|
| [songguoxs/awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts) | 588 | 50+ 完整案例(Veo3/Veo3.1/即梦/可灵/海螺/豆包),含动漫战斗、黏土、乐高等风格,提示词整段可复制 |
| [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 9066 | 顶级 GPT 提示词合集,含 `video_gen_prompting.txt`(视频生成提示词方法论) |

## Claude Code Skill 产线

| 仓库 | ⭐ | 说明 |
|---|---|---|
| [jnMetaCode/ai-shortfilm-prompts](https://github.com/jnMetaCode/ai-shortfilm-prompts) | 474 | Claude Code Skill:任意点子 → 电影级、模型就绪的视频提示词(Sora/Kling 等) |
| [rediumvex/ai-video-generator-claude](https://github.com/rediumvex/ai-video-generator-claude) | 418 | 10 个 Claude skill 生成影棚级 Seedance 2.0 视频提示词 |
| [zhouwei713/seedance-prompt](https://github.com/zhouwei713/seedance-prompt) | 327 | Hermes skill:写实 AI 视频提示词,适配 Seedance 与文生视频模型 |
| [Yuyyxz/kling-prompt-engineering](https://github.com/Yuyyxz/kling-prompt-engineering) | 4 | 导演式可灵提示词工程指南(中英) |

## 商业片 / TVC / 口播

| 仓库 | ⭐ | 说明 |
|---|---|---|
| [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) | 2073 | 文案 → 一分钟 Gemini Omni Flash 火柴人视频提示词包 |
| [kaomei/hand-drawn-video-prompts](https://github.com/kaomei/hand-drawn-video-prompts) | 265 | 中文口播稿 → 9:16 Q 版手绘视频提示词,科技人物 Q 版化 |
| [nutllwhy/seedance-tvc-director](https://github.com/nutllwhy/seedance-tvc-director) | 310 | Seedance 2.5 TVC 导演 skill:15s/30s/自定义广告片提示词、分镜、配音路由 |
| [T8mars/minimax-h3-prompt-skill-T8](https://github.com/T8mars/minimax-h3-prompt-skill-T8) | 290 | MiniMax H3 + Seedance 2.0 创意 DNA 提示词案例与可安装 Skill |

## 论文与研究清单

| 仓库 | ⭐ | 说明 |
|---|---|---|
| [jianzhnie/awesome-text-to-video](https://github.com/jianzhnie/awesome-text-to-video) | 746 | 文生视频生成/合成综述与论文清单,跟进模型演进 |

## 本地工作流

不装新服务,复用现有栈:

- **视频生成**: `grok-imagine-video`(jiujiu,8005,支持图生视频参考图)
- **界面**: jiujiu WebUI `http://127.0.0.1:8005/webui/chat`(传图 + 流式出片)
- **网关**: CPA(8317)统一入口,任何 OpenAI 兼容客户端可用
- **剧本侧**: 本地 `comic-drama-script` skill 负责结构,提示词层参考上表 drama-skills

## Contribute

- 新增条目要求:仓库 2026 年内活跃、描述准确、与视频/动漫提示词直接相关
- 星数与"最后更新"在每次维护时重新核对
- 私库,不对外

## License

CC0-1.0 (链接聚合)
