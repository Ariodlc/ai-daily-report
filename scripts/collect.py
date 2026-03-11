#!/usr/bin/env python3
"""
信息收集脚本 - 使用Kimi Search API收集各领域最新信息
"""

import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

# 配置各领域搜索关键词
CONFIG = {
    "fields": {
        "ai_tech": {
            "name": "AI技术科技",
            "queries": [
                "AI人工智能最新动态 今天",
                "大模型技术突破 2026",
                "ChatGPT Claude Gemini 新功能"
            ]
        },
        "kaoyan": {
            "name": "考研信息",
            "queries": [
                "080500材料科学与工程 考研复试线 2026",
                "2026考研调剂信息 材料专业",
                "材料考研最新政策"
            ]
        },
        "materials": {
            "name": "材料领域",
            "queries": [
                "新材料研究突破 最新",
                "纳米材料 电池材料 进展",
                "材料科学前沿动态"
            ]
        },
        "new_energy": {
            "name": "新能源",
            "queries": [
                "固态电池 锂电池 最新进展",
                "光伏储能 新能源政策",
                "电动车 动力电池 技术突破"
            ]
        },
        "policy": {
            "name": "十五五政策",
            "queries": [
                "十五五规划 最新政策",
                "国家产业政策 新材料 新能源",
                "2026年政策解读"
            ]
        }
    }
}

def kimi_search(query, limit=5):
    """使用kimi-search命令搜索"""
    try:
        # 通过subprocess调用kimi-search
        result = subprocess.run(
            ['kimi-search', query, '--limit', str(limit)],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            # 解析结果
            return {"query": query, "results": result.stdout}
        return {"query": query, "error": result.stderr}
    except Exception as e:
        return {"query": query, "error": str(e)}

def collect_field(field_id, field_config):
    """收集单个领域的信息"""
    print(f"\n🔍 正在收集: {field_config['name']}...")
    
    results = []
    for query in field_config['queries']:
        print(f"  搜索: {query}")
        result = kimi_search(query, limit=3)
        results.append(result)
    
    return {
        "name": field_config['name'],
        "queries": field_config['queries'],
        "results": results,
        "collected_at": datetime.now().isoformat()
    }

def collect_all():
    """收集所有领域的信息"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    print(f"=" * 50)
    print(f"🤖 AI Daily Report - 信息收集")
    print(f"📅 日期: {today}")
    print(f"=" * 50)
    
    data = {
        "date": today,
        "created_at": datetime.now().isoformat(),
        "fields": {}
    }
    
    for field_id, field_config in CONFIG["fields"].items():
        data["fields"][field_id] = collect_field(field_id, field_config)
    
    # 保存原始数据
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = raw_dir / f"{today}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 数据已保存: {output_file}")
    return data

if __name__ == "__main__":
    collect_all()
