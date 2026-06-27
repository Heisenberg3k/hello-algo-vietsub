import os
import re

LANGS = {
    'python': ('Python', '.py', 'python'),
    'cpp': ('C++', '.cpp', 'cpp'),
    'java': ('Java', '.java', 'java'),
    'csharp': ('C#', '.cs', 'csharp'),
    'go': ('Go', '.go', 'go'),
    'swift': ('Swift', '.swift', 'swift'),
    'javascript': ('JS', '.js', 'javascript'),
    'typescript': ('TS', '.ts', 'typescript'),
    'dart': ('Dart', '.dart', 'dart'),
    'rust': ('Rust', '.rs', 'rust'),
    'c': ('C', '.c', 'c'),
    'kotlin': ('Kotlin', '.kt', 'kotlin'),
    'ruby': ('Ruby', '.rb', 'ruby'),
}

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def to_pascal_case(snake_str):
    return ''.join(x.title() for x in snake_str.split('_'))

def extract_code(filepath, target_class, target_func, ext):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    if not target_class and not target_func:
        return "".join(lines).strip()
        
    start_idx = -1
    
    # Generate possible names
    func_names = [target_func, to_camel_case(target_func), to_pascal_case(target_func)] if target_func else []
    class_names = [target_class, to_pascal_case(target_class), to_camel_case(target_class)] if target_class else []
    
    targets = func_names if target_func else class_names
    
    # Try to find the declaration
    for i, line in enumerate(lines):
        for target in targets:
            if target and target in line and ('def ' in line or 'class ' in line or 'func ' in line or 'void ' in line or 'int ' in line or target + '(' in line or 'fn ' in line or 'struct ' in line):
                start_idx = i
                break
        if start_idx != -1:
            break
            
    if start_idx == -1:
        # Fallback to simple substring match
        for i, line in enumerate(lines):
            for target in targets:
                if target and target in line:
                    start_idx = i
                    break
            if start_idx != -1:
                break
                
    if start_idx == -1:
        return ""
        
    # Include previous lines if they are comments or decorators
    while start_idx > 0:
        prev = lines[start_idx-1].strip()
        if prev.startswith('//') or prev.startswith('#') or prev.startswith('@'):
            start_idx -= 1
        else:
            break

    extracted = []
    if ext in ['.py', '.rb']:
        # Indentation based
        # Find the base indent of the actual definition (skip comments/decorators)
        def_idx = start_idx
        while def_idx < len(lines) and (lines[def_idx].strip().startswith('#') or lines[def_idx].strip().startswith('@') or lines[def_idx].strip().startswith('//')):
            def_idx += 1
        if def_idx >= len(lines):
            def_idx = start_idx
            
        base_indent = len(lines[def_idx]) - len(lines[def_idx].lstrip())
        
        for line in lines[start_idx:]:
            if line.strip() == "":
                extracted.append(line)
                continue
            indent = len(line) - len(line.lstrip())
            is_comment_or_dec = line.strip().startswith('#') or line.strip().startswith('@')
            if len(extracted) > (def_idx - start_idx) and indent <= base_indent and not is_comment_or_dec:
                break
            extracted.append(line)
    else:
        # Brace based
        brace_count = 0
        found_brace = False
        for line in lines[start_idx:]:
            extracted.append(line)
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if '{' in line:
                found_brace = True
            if found_brace and brace_count <= 0:
                break
                
    # Clean up trailing blank lines
    while extracted and extracted[-1].strip() == "":
        extracted.pop()
        
    return "".join(extracted).strip()

def process_markdown(md_path, codes_dir):
    chapter = os.path.basename(os.path.dirname(md_path))
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Regex to match ```src ... ```
    pattern = re.compile(r"```src\s*\n\s*\[file\]\{([^}]*)\}-\[class\]\{([^}]*)\}-\[func\]\{([^}]*)\}\s*\n\s*```", re.MULTILINE)
    
    def replacer(match):
        file_name = match.group(1)
        target_class = match.group(2)
        target_func = match.group(3)
        
        replacement = []
        for lang, (tab_name, ext, md_lang) in LANGS.items():
            filepath = os.path.join(codes_dir, lang, chapter, file_name + ext)
            code = extract_code(filepath, target_class, target_func, ext)
            if code:
                replacement.append(f'=== "{tab_name}"\n')
                replacement.append(f'    ```{md_lang} title="{file_name}{ext}"\n')
                for line in code.split('\n'):
                    replacement.append(f'    {line}\n' if line else '    \n')
                replacement.append('    ```\n')
        
        if not replacement:
            return match.group(0) # Keep original if not found
            
        return "".join(replacement)
        
    new_content = pattern.sub(replacer, content)
    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == "__main__":
    docs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs'))
    codes_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'codes'))
    
    count = 0
    for root, dirs, files in os.walk(docs_dir):
        for f in files:
            if f.endswith('.md'):
                md_path = os.path.join(root, f)
                if process_markdown(md_path, codes_dir):
                    count += 1
    print(f"Processed and updated {count} markdown files.")
