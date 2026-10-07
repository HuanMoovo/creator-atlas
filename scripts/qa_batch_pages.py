#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量内容页质检（知识库「页面工厂」回收工序）。

用法（在仓库根目录运行）：
    python qa_batch_pages.py "docs/genres/**/README.md"
    python qa_batch_pages.py --sections 7 --title "Creator Atlas" "docs/methods/*.md"
    python qa_batch_pages.py --sections 4 --min-lines 40 "docs/genres/*/README.md"
    python qa_batch_pages.py --marker "第 34 轮" "docs/genres/**/README.md"
    python qa_batch_pages.py --lint "docs/genres/**/README.md"

检查项：文件存在、行数、标题标记、编号小节数（--sections 按本批模板实际节数传：
方法域 7、制作方法 4，不要硬编码）、「延伸阅读」小节、破折号「——」数量、
外链 http(s) 数量、模板连接词（命中先人工看上下文，是启发式）、emoji、占位词
（TODO/TBD/待补，启发式）、批次标记（--marker 传期望子串，如「第 34 轮」）、
站内相对链接可解析（从文件所在目录解析，跳过 http/mailto/#）。

退出码：0 = 全部通过；1 = 有缺陷或文件缺失。
"""
import argparse
import glob as globmod
import os
import re
import subprocess
import sys

EMOJI_RE = re.compile(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]')
SECTION_RE = re.compile(r'^## (\d+)\.', re.M)
LINK_RE = re.compile(r'\]\(([^)]+)\)')
CLICHE_WORDS = ['首先', '其次', '综上所述', '总而言之']
PLACEHOLDER_WORDS = ['TODO', 'TBD', '待补', '（略）', '[待']


def expand(paths):
    out = []
    for p in paths:
        if any(c in p for c in '*?['):
            out.extend(globmod.glob(p, recursive=True))
        elif os.path.isdir(p):
            for dp, _, fs in os.walk(p):
                out.extend(os.path.join(dp, f) for f in fs if f.endswith('.md'))
        else:
            out.append(p)
    return sorted(set(out))


def check(path, args):
    flags = []
    if not os.path.exists(path):
        return ['文件不存在']
    text = open(path, encoding='utf-8').read()
    lines = text.count('\n')
    if lines < args.min_lines:
        flags.append('line=%d' % lines)
    if args.title and args.title not in text:
        flags.append('缺标题标记')
    if args.sections:
        nums = sorted({int(m.group(1)) for m in SECTION_RE.finditer(text)})
        if nums != list(range(1, args.sections + 1)):
            flags.append('sections=%s(期望 1..%d)' % (nums, args.sections))
    if args.ext_heading and ('## ' + args.ext_heading) not in text:
        flags.append('缺%s' % args.ext_heading)
    dash = text.count('——')
    if dash > args.dash_max:
        flags.append('dash=%d' % dash)
    http = len(re.findall(r'https?://', text))
    if http and not args.allow_http:
        flags.append('http=%d' % http)
    for w in CLICHE_WORDS:
        if w in text:
            flags.append('连接词:%s' % w)
    emoji = len(EMOJI_RE.findall(text))
    if emoji:
        flags.append('emoji=%d' % emoji)
    for w in PLACEHOLDER_WORDS:
        if w in text:
            flags.append('占位词:%s' % w)
    if args.marker and args.marker not in text:
        flags.append('缺标记:%s' % args.marker)
    for m in LINK_RE.finditer(text):
        link = m.group(1).split('#')[0].strip()
        if not link or link.startswith(('http', 'mailto')):
            continue
        target = os.path.normpath(os.path.join(os.path.dirname(path), link))
        if not os.path.exists(target):
            flags.append('坏链:%s' % link)
    return flags


def main():
    ap = argparse.ArgumentParser(description='批量内容页质检')
    ap.add_argument('paths', nargs='+', help='文件 / 目录 / glob 模式')
    ap.add_argument('--sections', type=int, default=0, help='期望编号小节数（按本批模板传）')
    ap.add_argument('--min-lines', type=int, default=60, help='最少行数（默认 60）')
    ap.add_argument('--dash-max', type=int, default=2, help='破折号上限（默认 2）')
    ap.add_argument('--title', default='Creator Atlas', help='标题需包含的标记（传空串跳过）')
    ap.add_argument('--ext-heading', default='延伸阅读', help='需存在的二级标题（传空串跳过）')
    ap.add_argument('--marker', default='', help='需包含的批次标记子串，如 "第 34 轮"（传空串跳过）')
    ap.add_argument('--allow-http', action='store_true', help='允许外链（默认不允许）')
    ap.add_argument('--lint', action='store_true', help='追加运行 markdownlint-cli2')
    args = ap.parse_args()

    files = expand(args.paths)
    if not files:
        print('没有匹配到文件')
        sys.exit(1)
    failed = []
    for f in files:
        flags = check(f, args)
        mark = 'PASS' if not flags else 'FAIL: ' + '; '.join(flags)
        print('%-70s %s' % (f, mark))
        if flags:
            failed.append(f)
    print('\n%d/%d 通过' % (len(files) - len(failed), len(files)))

    if args.lint:
        cmd = 'npx --yes markdownlint-cli2 ' + ' '.join('"%s"' % f for f in files)
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        tail = (r.stdout or r.stderr).strip().split('\n')[-1] if (r.stdout or r.stderr) else ''
        print('markdownlint:', tail)
        if r.returncode != 0:
            failed.append('lint')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
