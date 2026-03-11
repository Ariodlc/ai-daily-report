# 🤖 AI智能日报

> 每天8点自动收集AI、考研、材料、新能源、政策等领域最新信息

---

## 🌐 网站预览

<div align="center">

**今日日报** → [查看网站](https://yourusername.github.io/ai-daily-report/)

📅 **更新时间**: 每天 8:00 (UTC+8)

</div>

---

## 📊 覆盖领域

| 领域 | 内容方向 |
|------|----------|
| 🤖 AI技术科技 | 大模型、AI应用、技术突破 |
| 🎓 考研信息 | 材料专业(080500)复试线、招生动态 |
| 🧪 材料领域 | 新材料研究、行业动态 |
| ⚡ 新能源 | 电池、光伏、储能、电动车 |
| 📜 十五五政策 | 国家规划、产业政策解读 |

---

## 🚀 快速开始

### 1.  Fork 本项目

点击右上角的 **Fork** 按钮，将项目复制到你的 GitHub 账号

### 2. 配置 GitHub Pages

1. 进入你 Fork 的仓库
2. 点击 **Settings** → **Pages**
3. Source 选择 **GitHub Actions**

### 3. 设置 API 密钥

1. 进入 **Settings** → **Secrets and variables** → **Actions**
2. 点击 **New repository secret**
3. 添加密钥:
   - Name: `KIMI_API_KEY`
   - Value: 你的 Kimi API Key

### 4. 手动触发测试

1. 进入 **Actions** 标签
2. 选择 **Daily Report** 工作流
3. 点击 **Run workflow** 手动运行

### 5. 访问网站

等待几分钟后访问:
```
https://yourusername.github.io/ai-daily-report/
```

---

## 📁 项目结构

```
ai-daily-report/
├── .github/
│   └── workflows/
│       └── daily-report.yml      # 自动工作流
├── docs/                          # 日报内容
│   ├── index.md                   # 今日日报首页
│   └── archive/                   # 历史归档
├── scripts/
│   ├── collect.py                 # 信息收集
│   └── generate.py                # 日报生成
├── mkdocs.yml                     # 网站配置
└── requirements.txt               # Python依赖
```

---

## 🛠️ 本地开发

```bash
# 克隆项目
git clone https://github.com/yourusername/ai-daily-report.git
cd ai-daily-report

# 安装依赖
pip install -r requirements.txt

# 生成日报
python scripts/generate.py

# 本地预览
mkdocs serve
```

---

## ⚙️ 自定义配置

### 修改搜索关键词

编辑 `scripts/collect.py` 中的 `CONFIG` 配置:

```python
CONFIG = {
    "fields": {
        "ai_tech": {
            "name": "AI技术科技",
            "queries": [
                "你的自定义关键词1",
                "你的自定义关键词2"
            ]
        }
    }
}
```

### 修改网站信息

编辑 `mkdocs.yml`:

```yaml
site_name: 你的网站名称
site_url: https://yourusername.github.io/ai-daily-report/
```

---

## 📜 许可证

MIT License

---

<div align="center">
Made with ❤️ by AI
</div>
