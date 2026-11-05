#!/usr/bin/env python3
"""Gera o index.html a partir de src/posts.py e src/template.html.
Uso: python3 build.py
"""
import json, pathlib, runpy

raiz = pathlib.Path(__file__).resolve().parent
dados = runpy.run_path(str(raiz / "src" / "posts.py"))
posts = dados["posts"]

for p in posts:
    for caminho in (f"vid/{p['video']}.mp4", f"img/{p['video']}.jpg"):
        if not (raiz / caminho).exists():
            print("AVISO: arquivo não encontrado:", caminho)
    p["mb"] = round((raiz / f"vid/{p['video']}.mp4").stat().st_size / 1e6)
    p["cred"] = p["id"] != "chamada" and p.get("aba", "fabrica") == "fabrica"
    for k in ("A", "B"):
        if k in p:
            if len(p[k]["tags"]) > 5:
                print("AVISO: mais de 5 hashtags em", p["id"], k)
            if len(p[k]["titulo"]) > 100:
                print("AVISO: título do YouTube acima de 100 caracteres em", p["id"], k)

js = json.dumps({"posts": posts, "cred": dados["CRED"], "abas": dados["ABAS"]}, ensure_ascii=False).replace("</", "<\\/")
tpl = (raiz / "src" / "template.html").read_text(encoding="utf-8")
(raiz / "index.html").write_text(tpl.replace("__DATA__", js), encoding="utf-8")
print("index.html gerado com", len(posts), "posts")
