#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
依赖: pip install Pillow
功能：基于 inline-size 模拟换行，精确计算 y 坐标，生成 Inkscape 兼容的 Flow Text SVG。
"""
import xml.etree.ElementTree as ET
from PIL import ImageFont
import os
import sys
import re

def get_text_width(text, font):
	if hasattr(font, "getlength"):
		return font.getlength(text)
	bbox = font.getbbox(text)
	return bbox[2] - bbox[0] if bbox else 0

def parse_bold_segments(text):
    # 仅用于生成 <tspan>，不参与宽度计算
    pattern = r'_([^_]+)_|\*\*([^*]+)\*\*'
    segments = []
    last_end = 0
    for m in re.finditer(pattern, text):
        start, end = m.span()
        if start > last_end:
            segments.append((text[last_end:start], False))
        bold_str = m.group(1) or m.group(2)
        segments.append((bold_str, True))
        last_end = end
    if last_end < len(text):
        segments.append((text[last_end:], False))
    return segments

def measure_segments_width(segments, font, bold_factor=1.0):
	total = 0.0
	for txt, is_bold in segments:
		total += get_text_width(txt, font) # * (bold_factor if is_bold else 1.0)
	return total

def wrap_by_px_with_bold(text, max_width_px, font, bold_factor=1.00):
	lines = []
	current = ""
	for char in text:
		test = current + char
		segs = parse_bold_segments(test)
		if measure_segments_width(segs, font, bold_factor) <= max_width_px or not current:
			current = test
		else:
			lines.append(current)
			current = char
	if current:
		lines.append(current)
	return len(lines)

def count_wrapped_lines(text, max_width_px, font):
    # 剔除标记符号，仅按可见字符模拟换行
    clean_text = re.sub(r'_|\*\*', '', text)
    if not clean_text.strip():
        return 1

    line_count = 1
    current_w = 0.0
    for ch in clean_text:
        w = get_text_width(ch, font)
        if current_w + w > max_width_px and current_w > 0:
            line_count += 1
            current_w = w  # 新行从当前字符开始
        else:
            current_w += w
    return line_count

def generate_flow_bullets(text_input, output="flow_bullets.svg",
						  font_path="Arial.ttf", font_size_pt=14, font_size=18.6667,
						  inline_size_px=380, bullet="🔾",
						  margin_left=60, indent_px=25,
						  line_spacing=1.4, item_gap=12):
	if not os.path.exists(font_path):
		sys.exit(f"❌ 字体文件不存在: {font_path}")
	
	font = ImageFont.truetype(font_path, font_size)
	# font_name = os.path.splitext(os.path.basename(font_path))[0]
	font_name = "Alibaba PuHuiTi"
	
	lines = [l.strip() for l in text_input.strip().split('\n') if l.strip()]
	if not lines:
		sys.exit("❌ 未检测到有效文本行。")

	# SVG 2.0 声明 + 基础样式
	svg = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", version="2.0")
	base_style = f"font-family:'{font_name}'; font-weight: 300; font-size:{font_size_pt}pt; fill:#000000;"
	
	current_y = 0.0
	for i, raw_text in enumerate(lines):
		line_text = raw_text.lstrip("* ")
		print(line_text)
		# 🔑 核心：模拟 Inkscape 换行，获取实际行数
		num_lines = count_wrapped_lines(line_text, inline_size_px, font)
		block_height = num_lines * font_size_pt * line_spacing

		group = ET.SubElement(svg, "g", id=f"item_{i}")

		x_bullet = margin_left
		x_text   = margin_left + indent_px
		
		# Bullet（固定位置）
		b = ET.SubElement(group, "text", id=f"b_{i}", x=str(x_bullet), y=str(current_y))
		b.set("style", base_style)
		b.text = bullet
		
		# Flow Text 正文
		t = ET.SubElement(group, "text", id=f"t_{i}", x=str(x_text), y=str(current_y))
		t.set("style", f"{base_style}; inline-size: {inline_size_px}px;")

		# 新增：生成 <tspan> 实现局部粗体
		# t.text = line_text  # 保持原始段落，交由 Inkscape 动态重排
		segments = parse_bold_segments(line_text)
		for chunk, is_bold in segments:
			tspan = ET.SubElement(t, "tspan")
			if is_bold:
				tspan.set("font-weight", "normal")
			tspan.text = chunk
		
		# 精确累加 Y：当前块高度 + 段落间距
		current_y += block_height + item_gap

	svg.set("width", "800px")
	svg.set("height", f"{current_y}px")
	svg.set("viewBox", f"0 0 800 {current_y}")
	ET.indent(svg, space="  ")
	ET.ElementTree(svg).write(output, encoding="utf-8", xml_declaration=True)
	print(f"✅ 已生成: {output} | inline-size: {inline_size_px}px | 预计算 Y 偏移完成")

# ================= 使用示例 =================
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: gen_bullets in-file")
		exit(0)
	with open(sys.argv[1], "r") as file:
		sample = file.read()

	generate_flow_bullets(
		text_input=sample,
		font_path="/usr/share/fonts/truetype/Alibaba PuHuiTi/Alibaba_PuHuiTi_Light.ttf",
		font_size_pt=14,
		font_size=18.6667,
		inline_size_px=457,      # 预设流式宽度
		indent_px=26,
		margin_left=65,
		line_spacing=1.5,
		item_gap=16              # 段落间额外留白
	)
