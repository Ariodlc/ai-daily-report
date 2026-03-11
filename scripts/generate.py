#!/usr/bin/env python3
"""
日报生成脚本 - 使用Kimi生成结构化日报内容
"""

import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

def load_raw_data(date_str=None):
    """加载原始数据"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    raw_file = Path(f"data/raw/{date_str}.json")
    if raw_file.exists():
        with open(raw_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def kimi_generate_summary(field_name, search_results):
    """使用Kimi生成摘要"""
    # 构建提示词
    context = f"""请根据以下搜索结果，为"{field_name}"领域生成一份简洁的日报摘要。

要求：
1. 用3-5个要点总结最重要的信息
2. 每个要点控制在30字以内
3. 使用简洁的中文
4. 只输出要点，不要多余解释

搜索结果：
{json.dumps(search_results, ensure_ascii=False, indent=2)}

请输出："""
    
    try:
        # 这里可以通过subprocess或API调用Kimi生成内容
        # 暂时返回占位符
        return "（AI生成内容占位符 - 需要接入Kimi API）"
    except Exception as e:
        return f"生成失败: {str(e)}"

def generate_field_content(field_id, field_data):
    """生成单个领域的内容"""
    name = field_data["name"]
    results = field_data.get("results", [])
    
    # 提取搜索结果中的文本
    search_text = []
    for r in results:
        if "results" in r:
            search_text.append(r["results"])
    
    # 生成摘要
    summary = kimi_generate_summary(name, search_text)
    
    content = f"""### {name}

#### 📋 简洁摘要

1. （待AI生成）
2. （待AI生成）
3. （待AI生成）

<details>
<summary>🔍 点击查看深度分析</summary>

**详细解读**

（待AI生成深度分析内容）

**关键数据**
- 数据来源: AI自动收集
- 更新时间: {datetime.now().strftime("%H:%M")}

</details>

---
"""
    return content

def generate_daily_report(data):
    """生成完整日报"""
    date = data["date"]
    weekday = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    weekday_cn = {"Monday": "周一", "Tuesday": "周二", "Wednesday": "周三", 
                  "Thursday": "周四", "Friday": "周五", "Saturday": "周六", "Sunday": "周日"}.get(weekday, weekday)
    
    # 生成各领域内容
    fields_content = ""
    for field_id, field_data in data.get("fields", {}).items():
        fields_content += generate_field_content(field_id, field_data)
    
    content = f"""---
title: "AI智能日报 - {date}"
date: {date}
---

# 📰 AI智能日报

<div class="hero">
  <h1>{date} {weekday_cn}</h1>
  <p>每天自动收集AI、考研、材料、新能源、政策等领域最新信息</p>
</div>

---

## 📊 今日概览

| 领域 | 状态 | 关键信息 |
|:----:|:----:|:---------|
| 🤖 AI技术科技 | ✅ | 监控中 |
| 🎓 考研信息 | ✅ | 监控中 |
| 🧪 材料领域 | ✅ | 监控中 |
| ⚡ 新能源 | ✅ | 监控中 |
| 📜 十五五政策 | ✅ | 监控中 |

---

{fields_content}

---

## 📝 关于本日报

- **生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **数据来源**: AI自动搜索整理
- **更新时间**: 每天 8:00 (UTC+8)
- **免责声明**: 内容仅供参考，请以官方信息为准

---

<div class="actions">
  <a href="archive/" class="md-button">📚 查看历史归档</a>
</div>
"""
    
    return content

def save_report(content, date_str=None):
    """保存日报"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    # 确保目录存在
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)
    archive_dir = Path("docs/archive")
    archive_dir.mkdir(parents=True, exist_ok=True)
    
    # 保存首页
    with open(docs_dir / "index.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    # 保存归档
    with open(archive_dir / f"{date_str}.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ 日报已保存: docs/index.md 和 docs/archive/{date_str}.md")

def generate_archive_index():
    """生成归档索引"""
    archive_dir = Path("docs/archive")
    archive_dir.mkdir(exist_ok=True)
    
    files = sorted(archive_dir.glob("*.md"), reverse=True)
    
    content = """# 📚 历史归档

> 查看往期日报

---

"""
    
    for f in files:
        if f.name == "index.md":
            continue
        date = f.stem
        try:
            weekday = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
            weekday_cn = {"Monday": "周一", "Tuesday": "周二", "Wednesday": "周三", 
                          "Thursday": "周四", "Friday": "周五", "Saturday": "周六", "Sunday": "周日"}.get(weekday, weekday)
            content += f"- [{date} {weekday_cn}]({f.name})\n"
        except:
            content += f"- [{date}]({f.name})\n"
    
    with open(archive_dir / "index.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("✅ 归档索引已更新")

if __name__ == "__main__":
    print("=" * 50)
    print("🤖 正在生成日报...")
    print("=" * 50)
    
    # 加载数据
    data = load_raw_data()
    if data is None:
        print("⚠️ 未找到原始数据，使用模板生成")
        data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "fields": {
                "ai_tech": {"name": "AI技术科技", "results": []},
                "kaoyan": {"name": "考研信息", "results": []},
                "materials": {"name": "材料领域", "results": []},
                "new_energy": {"name": "新能源", "results": []},
                "policy": {"name": "十五五政策", "results": []}
            }
        }
    
    # 生成并保存
    report = generate_daily_report(data)
    save_report(report, data["date"])
    generate_archive_index()
    
    print("=" * 50)
    print("✅ 日报生成完成!")
    print("=" * 50)
