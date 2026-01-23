#!/usr/bin/env python3
import os
from pathlib import Path

def get_title_from_filename(filename):
    name = filename.replace('.kql', '').replace('-', ' ').replace('_', ' ').replace('&', 'and')
    return name

def convert_kql_to_md(content, filename):
    title = get_title_from_filename(filename)
    lines = content.split('\n')
    result = [f"# {title}\n"]
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('//'):
            comment = line.strip()[2:].strip()
            if comment:
                result.append(f"\n## {comment}\n")
            i += 1
            query_lines = []
            while i < len(lines) and not lines[i].strip().startswith('//'):
                query_lines.append(lines[i])
                i += 1
            while query_lines and not query_lines[-1].strip():
                query_lines.pop()
            if any(line.strip() for line in query_lines):
                result.append("```kql")
                result.extend(query_lines)
                result.append("```\n")
        else:
            if line.strip():
                query_lines = []
                while i < len(lines) and not lines[i].strip().startswith('//'):
                    query_lines.append(lines[i])
                    i += 1
                while query_lines and not query_lines[-1].strip():
                    query_lines.pop()
                if any(line.strip() for line in query_lines):
                    result.append("```kql")
                    result.extend(query_lines)
                    result.append("```\n")
            else:
                i += 1
    return '\n'.join(result)

def main():
    import sys
    base = Path(__file__).parent
    kql_files = list(base.rglob('*.kql'))
    print(f"Found {len(kql_files)} files\n")
    converted = []
    for kql_file in sorted(kql_files):
        try:
            content = kql_file.read_text(encoding='utf-8')
            md_content = convert_kql_to_md(content, kql_file.name)
            md_file = kql_file.with_suffix('.md')
            md_file.write_text(md_content, encoding='utf-8')
            print(f"✓ {kql_file.name}")
            converted.append(kql_file)
        except Exception as e:
            print(f"✗ {kql_file.name}: {e}")
    print(f"\nConverted: {len(converted)}/{len(kql_files)}\n")
    if '--delete' in sys.argv:
        for f in converted:
            f.unlink()
            print(f"Deleted: {f.name}")

if __name__ == '__main__':
    main()
