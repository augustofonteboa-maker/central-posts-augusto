# Dados da central. Edite aqui e rode: python3 build.py
CRED = "Adaptação livre de O Pequeno Príncipe, de Antoine de Saint-Exupéry."
WPP = "https://chat.whatsapp.com/CfXGFhBWUxP6ktNB1f453d"
AULA = "[LINK DA AULA]"

EPS = [
    ("O Desenho do Carneiro", "🐑",
     "Um aviador cai no deserto. Ao amanhecer, uma voz pequena pede: desenha-me um carneiro.",
     "Ele Caiu no Deserto e um Menino Pediu Algo Estranho",
     "No meio do nada, ao amanhecer, uma voz pequena pediu: desenha-me um carneiro. Nenhum desenho servia… até o último."),
    ("O Adeus à Rosa", "🌹",
     "Ele cuidava de uma rosa orgulhosa. Antes de partir, limpou os vulcões e a protegeu.",
     "Ele Foi Embora Sem Saber o Quanto a Amava",
     "Ela era orgulhosa. Ele não soube entender. Na hora de partir, só restou um adeus baixinho."),
    ("O Rei", "👑",
     "No primeiro planeta, um rei que mandava em tudo. Até nos bocejos. Mas estava sozinho.",
     "O Rei Que Mandava em Tudo, Menos na Solidão",
     "Ele dava ordens até para os bocejos. Mas não tinha ninguém para governar."),
    ("O Acendedor de Lampiões", "🏮",
     "O menor planeta de todos, onde cada dia dura um minuto. E um homem que nunca para.",
     "Um Planeta Onde o Dia Dura 1 Minuto",
     "Acende, apaga, acende, apaga. Ele nunca descansava. E foi o único que o menino admirou."),
    ("O Jardim de Rosas", "💔",
     "Ele chega à Terra e encontra milhares de rosas iguais à sua. A dele não era única?",
     "Ele Descobriu Que Sua Rosa Não Era Única",
     "Milhares de rosas iguais à dele. Sentado à beira do trigal, ele chorou sozinho… até que algo se mexeu."),
    ("A Raposa e a Rosa", "🦊",
     "Uma raposa pede: cativa-me. E conta o segredo: só se vê bem com o coração.",
     "A Raposa Contou o Segredo Que Mudou Tudo",
     "\"Cativa-me\", ela pediu. Dia após dia, ficaram mais perto. E então ela contou: só se vê bem com o coração."),
    ("O Poço no Deserto", "✨",
     "Sem água, os dois caminham pela noite. O deserto é belo porque esconde um poço.",
     "O Que o Deserto Esconde",
     "Sem água, caminhando pela noite. O menino disse que o deserto era belo. E tinha razão."),
    ("A Volta para Casa", "🌟",
     "O avião está consertado. O menino precisa voltar para a sua rosa. O final da história.",
     "A Despedida Mais Bonita Que Você Vai Ver",
     "O avião está pronto. O menino precisa voltar. E quando você olhar as estrelas, vai lembrar dele."),
]

TAGS_A = ["#opequenoprincipe", "#animacaoia", "#googleflow", "#claude", "#massinha"]
TAGS_B = ["#opequenoprincipe", "#historia", "#animacao", "#massinha", "#historiasparadormir"]

posts = [{
    "id": "chamada", "video": "00-chamada-fabrica-de-historias", "num": "00",
    "nome": "Chamada da aula · Fábrica de Histórias", "dur": "25 s",
    "onde": "Instagram · TikTok · YouTube Shorts",
    "dica": "Poste primeiro: é o vídeo que chama para a aula.",
    "A": {
        "social": "Essa novelinha não teve roteirista, desenhista nem dublador.\n\nEu fiz um pedido. O Claude entrou no Google Flow e fez o roteiro, os personagens, os character sheets, a animação e o narrador.\n\nServe para novelinha no TikTok, vídeo de história e canal dark.\n\nComenta HISTÓRIA que eu te mando a aula completa.",
        "tags": ["#claude", "#googleflow", "#animacaoia", "#novelinha", "#canaldark"],
        "titulo": "Fábrica de Histórias: o Claude Fez a Novelinha Inteira",
        "desc": f"Roteiro, personagens, character sheets, animação e narrador: tudo com o Claude no Google Flow.\n\n🎓 Aula completa: {AULA}\n\n#shorts #claude #googleflow #animacaoia",
    },
}]

posts.append({
    "id": "filme", "video": "01-filme-completo", "num": "01",
    "nome": "O Pequeno Príncipe · Filme completo", "dur": "4 min",
    "onde": "YouTube (vídeo normal) · TikTok",
    "dica": "No YouTube entra como vídeo normal (passa de 3 min). No Instagram, o Reel pode ser cortado: prefira as partes.",
    "A": {
        "social": "Do deserto ao asteroide da rosa: O Pequeno Príncipe inteiro, em 4 minutos, em massinha.\n\nEu fiz o pedido. O Claude e o Google Flow fizeram roteiro, personagens, animação e narração.\n\nComenta HISTÓRIA que eu te mando a aula.",
        "tags": TAGS_A,
        "titulo": "O Pequeno Príncipe em Massinha: Filme Completo Feito com IA",
        "desc": ("Do deserto ao asteroide da rosa: a história inteira do Pequeno Príncipe, contada em 4 minutos, em massinha.\n\n"
                 "Este filme foi feito com o Claude e o Google Flow: roteiro, personagens, character sheets, animação e narração. Eu fiz o pedido, a IA fez o resto.\n\n"
                 f"🎓 Aula completa, do pedido ao vídeo pronto: {AULA}\n👇 Entre no grupo do WhatsApp para receber as próximas aulas:\n{WPP}\n\n"
                 "Episódios:\n" + "\n".join(f"{i}. {e[0]}" for i, e in enumerate(EPS, 1)) +
                 f"\n\n{CRED}\n\n#OPequenoPrincipe #AnimacaoIA #GoogleFlow #Claude #Massinha"),
    },
    "B": {
        "social": "Um aviador perdido no deserto. Um menino que veio de um asteroide do tamanho de uma casa. E uma rosa, lá longe, esperando por ele.\n\nA história completa, em 4 minutos. Assista até o fim.",
        "tags": TAGS_B,
        "titulo": "Ele Veio de Outro Planeta Só Para Entender o Amor | O Pequeno Príncipe",
        "desc": ("Um aviador perdido no deserto. Um menino de cabelo dourado que veio de um asteroide do tamanho de uma casa. E uma rosa, lá longe, esperando por ele.\n\n"
                 "No caminho, ele conheceu um rei sem ninguém para governar, um homem que acendia um lampião a cada minuto, um jardim com milhares de rosas iguais à sua… e uma raposa que lhe ensinou o segredo mais simples do mundo.\n\n"
                 f"Esta é a história completa, em 4 minutos. Assista até o fim.\n\n{CRED}\n#OPequenoPrincipe #Historia #Animacao #Massinha"),
    },
})

for i, (nome, emo, resumo, tit_b, hist_b) in enumerate(EPS, 1):
    prox = f"Continua na parte {i+1} 👉" if i < 8 else "Fim. Assista à história completa no canal 👉"
    prox_social = f"Parte {i} de 8. Segue para ver a parte {i+1}." if i < 8 else "Parte 8 de 8. Fim. A história completa está no perfil."
    posts.append({
        "id": f"parte-{i}", "video": f"parte-{i}", "num": f"P{i}",
        "nome": f"Parte {i} · {nome}", "dur": "30 s",
        "onde": "Instagram · TikTok · YouTube Shorts",
        "dica": "",
        "A": {
            "social": f"{resumo}\n\nParte {i} de 8 do Pequeno Príncipe em massinha. Eu não desenhei, não animei e não narrei: o Claude fez tudo no Google Flow.\n\nComenta HISTÓRIA que eu te mando a aula.",
            "tags": TAGS_A,
            "titulo": f"O Pequeno Príncipe em Massinha · Parte {i}: {nome}",
            "desc": f"{resumo}\n\nParte {i} de 8 · feito com Claude + Google Flow.\n🎬 Filme completo e aula no canal: {AULA}\n\n{CRED}\n#shorts #OPequenoPrincipe #AnimacaoIA #GoogleFlow #Claude",
        },
        "B": {
            "social": f"{hist_b}\n\n{prox_social}",
            "tags": TAGS_B,
            "titulo": f"{tit_b} {emo} | O Pequeno Príncipe #{i}",
            "desc": f"{hist_b}\n{prox}\n{CRED}\n#shorts #OPequenoPrincipe #Historia",
        },
    })
