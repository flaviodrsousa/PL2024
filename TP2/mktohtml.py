import re
import sys

def converter_linhas(linhas):
    n_linha = 0
    linhas_resultado = []
    while n_linha < len(linhas):
        if linhas[n_linha].startswith("\n"):

            if len(linhas[n_linha].strip()) == 0:
                linhas_resultado.append("")
            n_linha += 1

        elif linhas[n_linha] == "":
            linhas_resultado.append("")
            n_linha+=1

        elif linhas[n_linha].startswith("#"):
            level = linhas[n_linha].count('#')
            informacao = linhas[n_linha][level+1:].strip()
            linhas_resultado.append(f"<h{level}>{informacao}</h{level}>\n")
            n_linha += 1
        
        elif linhas[n_linha].startswith("> "):
            informacao = linhas[n_linha][2:].strip()
            linhas_resultado.append(f"<blockquote>\n<p>{informacao}</p>\n</blockquote>\n")
            n_linha += 1
        
        elif linhas[n_linha].startswith("---"):
            linhas_resultado.append("<hr>\n")
            n_linha += 1
        
        elif re.match(r'^\s*\d+\.', linhas[n_linha]):
            linhas_resultado.append("<ol>\n")
            while n_linha < len(linhas) and re.match(r'^\s*\d+\.', linhas[n_linha]):
                items = [item.strip() for item in re.split(r'\s*\d+\.\s*', linhas[n_linha])[1:] if item]
                linhas_resultado.extend([f'<li>{item}</li>\n' for item in items])
                n_linha += 1
            linhas_resultado.append("</ol>\n")
        
        elif linhas[n_linha].startswith("  - "):
            linhas_resultado.append("<ul>\n")
            while n_linha < len(linhas) and linhas[n_linha].startswith("  - "):
                informacao = linhas[n_linha][4:].strip()
                linhas_resultado.append(f"<li>{informacao}</li>\n")
                n_linha += 1
            linhas_resultado.append("</ul>\n")

        else:
            linhas[n_linha] = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linhas[n_linha])
            linhas[n_linha] = re.sub(r'\*(.*?)\*', r'<n_linha>\1</n_linha>', linhas[n_linha])
            linhas[n_linha] = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', linhas[n_linha])
            linhas[n_linha] = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', linhas[n_linha])
            linhas[n_linha] = re.sub(r'`([^`]+)`', r'<code>\1</code>', linhas[n_linha])
            linhas_resultado.append(f"<p>{linhas[n_linha]}</p>\n")
            n_linha += 1

    return linhas_resultado

def mdHTML(inp):
    with open(inp, "r", encoding='utf-8') as file:
        content = file.read()

    linhas = content.split("\n")
    linhas_resultado = converter_linhas(linhas)
    out = inp.replace(".md", ".html")

    with open(out, 'w') as html_file:
        for converted_line in linhas_resultado:
            html_file.write(converted_line)

def main(inp):
    mdHTML(inp[1])

if __name__ == "__main__":
    main(sys.argv)