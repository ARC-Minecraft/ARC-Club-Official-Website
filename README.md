# ARC 游戏俱乐部 · 官方站点 v2.0

> **弧光游戏俱乐部 / ARC Game Club** 的官方静态站点，2015 年成立，从 -SDT- 一路走到 ARC，十年沉淀。

🌐 **在线地址**：https://8vab0z0dve6c8.space.mcode.cn

---

## 项目简介

v2.0 是对 v1（Flask 后端）全面重构后的纯静态站点，零后端依赖，部署到任意静态托管平台（mcode / GitHub Pages / Netlify / Cloudflare Pages 等）即可。

站点覆盖：
- **8 个自建游戏服务器**：我的世界基岩 5 端口 + 幻兽帕鲁 + 泰拉瑞亚
- **9 个俱乐部分部**：WoTB 亚服 / 国服 / 皇室战争 / APEX / 荒野乱斗 / CoDM / 守望先锋 / Valorant / GTA V / 无人深空
- **弧光摄影间**：微电影 / 宣传片 / 比赛录像
- **弧光技术部**：ARC-Minecraft GitHub 组织（23 个 EndStone + Bedrock Addon 仓库 + WoTB 历史项目）
- **成员介绍**：9 位核心成员档案

---

## 目录结构

```
arc-club-website-v2/
├── index.html              # 主页（Hero / 简介 / 时间线 / 服务器 / 分部 / 摄影间入口 / 加入我们）
├── bedrock.html            # 我的世界基岩总览（5 端口 + 宣传片 + 群）
├── bedrock-19132.html      # MC 基岩 5 个端口子页（冒险 / 创造 / 枪战 / 末世 / 无限制）
├── bedrock-19134.html
├── bedrock-19142.html
├── bedrock-19152.html
├── bedrock-19172.html
├── palworld.html           # 幻兽帕鲁服务器
├── terraria.html           # 泰拉瑞亚服务器
├── dont_starve.html        # 饥荒（暂停）
├── forest.html             # 森林（暂停）
├── wind_quest.html         # 风启之旅（暂停）
├── wind_island.html        # 风屿奇航（暂停）
├── icefire.html            # 冰封之焰（暂停）
├── wotb.html               # WoTB 分部（主服 / 亚服 / 国服）
├── wotb-asia.html          # WoTB 亚服（群 707492942）
├── wotb-cn.html            # WoTB 国服（群 754149012）
├── clash_royale.html       # 皇室战争分部
├── apex.html               # APEX 英雄分部
├── brawl_stars.html        # 荒野乱斗分部
├── codm.html               # 使命召唤手游分部
├── overwatch.html          # 守望先锋分部
├── valorant.html           # Valorant 分部
├── gta5.html               # GTA V 分部（含 Social Club Crew）
├── nms.html                # 无人深空分部
├── divisions.html          # 全部 9 个分部总览
├── studio.html             # 弧光摄影间（4 段 B 站视频 + 7 段视频集锦）
├── tech.html               # 弧光技术部（23 个 GitHub 仓库 + 两板块）
├── members.html            # 9 位核心成员介绍
├── servers.html            # 旧版服务器总览（保留不在导航）
└── assets/
    ├── style.css           # 共享设计系统（CSS 变量 + 浅色主题 + 紫红渐变）
    ├── icon.png            # ARC 俱乐部图标
    ├── img/
    │   ├── games/          # 15 个游戏 banner JPG
    │   ├── members/        # 9 个成员头像 JPG
    │   └── games/originals/  # 原始图备份（gitignored）
└── .gitignore
```

---

## 技术栈

- **纯静态**：HTML + CSS（无构建工具、无 JS 框架）
- **设计**：CSS 变量 / 浅色主题 / 紫红渐变（`#e91e63` → `#4a148c`）/ 卡片 + 渐变 + 真图
- **懒加载**：B 站视频用封面 + 点击注入 iframe
- **响应式**：CSS Grid 自适应（grid-2 / grid-3 / grid-4）
- **图标**：SVG / emoji（少量）
- **游戏图源**：Steam CDN / 官网 og:image / Activision / 玩家上传

---

## 本地预览

不需要构建，直接用任何静态服务器即可：

```bash
# Python 内置 HTTP server
python -m http.server 8000

# 或 Node.js
npx serve .

# 然后浏览器打开 http://localhost:8000
```

直接双击 `index.html` 用浏览器打开也能跑（视频依赖网络的 lazy-load iframe 也能工作）。

---

## 部署

本站部署在 **mcode 静态托管**（`space.mcode.cn`）：

```bash
# 在项目根目录
website_deploy --node_id 438741679345924
```

也可以部署到任何静态托管（GitHub Pages / Netlify / Vercel / Cloudflare Pages），把整个项目根目录上传即可。

---

## 页面设计

- **首页**（`index.html`）：Hero + 简介 + 时间线 + 8 服务器卡 + 9 分部卡 + 摄影间入口 + 加入我们
- **服务器 / 分部卡片**：banner 上图 + 下文字（gradient + real image，比例严格 16:9）
- **视频卡**：懒加载（默认封面 + 元数据，点击才加载 B 站 iframe）
- **顶部 nav**：首页 / 服务器 / 俱乐部分部（带状态点） / 弧光摄影间 / 弧光技术部 / 成员介绍
- **底部 footer**：创始于 2015 · 游戏热爱者聚集地 + QQ / Discord / oopz 三个官方入口

---

## 主要技术细节

### Banner 比例保证
所有 15 个 game banner 严格 16:9（1200×675）：
- 原图先按 16:9 center crop（保留中心主体）
- 再 resize 到 1200×675
- 永不直接 `resize()` 拉伸（避免畸变）

### Nav 高亮
每个页面根据 URL 自动给当前页加 `.active` class：
```js
document.querySelectorAll('.nav-links > a').forEach(a => {
  if (a.getAttribute('href').toLowerCase() === location.pathname.split('/').pop()) {
    a.classList.add('active');
  }
});
```

### B 站视频懒加载
默认显示封面 + 元数据（标题 / UP / 播放 / 赞 / 弹幕 / 简介 / BV 号），点击封面才注入 iframe：
```js
cover.addEventListener('click', () => {
  cover.innerHTML = '<iframe src="...' + cover.getAttribute('data-src') + '..." />';
});
```

---

## 官方联系方式

- **QQ 官方群**：[1138387946](https://qm.qq.com/q/zZkzvJWrZI)
- **Discord**：https://discord.gg/qcRaH2XYA
- **oopz**：https://oopz.cn/i/1XF5G2
- **服务器**：`arcclub.top:19132`（基岩主服）/ `:8211`（幻兽帕鲁）/ `:7777`（泰拉瑞亚）

---

## 关联项目

- **基岩生态开发**：[github.com/ARC-Minecraft](https://github.com/ARC-Minecraft) — 23 个 EndStone 基岩服插件 + Bedrock Addon 工具
- **游戏服务器**：开服 8 年（2018 至今），5 端口 MCBE / 帕鲁 / 泰拉

---

## 版权

© ARC Game Club. All rights reserved.

俱乐部是玩家自治组织，所有游戏、商标归各自发行商所有（Mojang / Microsoft / Pocketpair / Re-Logic / Klei / Endnight / Supergiant / Blizzard / Riot / Rockstar / Hello Games / 等）。
