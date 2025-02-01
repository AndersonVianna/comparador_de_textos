import gradio as gr
import os
import difflib
import sys

def compare_texts(text1, text2):
    # Divide os textos em linhas
    text1_lines = text1.splitlines()
    text2_lines = text2.splitlines()

    # Cria um objeto Differ para comparar os textos
    differ = difflib.Differ()

    # Gera as diferenças
    diff = list(differ.compare(text1_lines, text2_lines))

    # Cria a legenda
    legend = """
    <div style="margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">
        <h4 style="margin-top: 0;">Legenda:</h4>
        <ul style="list-style-type: none; padding-left: 0;">
            <li><span style="color: red">- Texto</span>: Linha removida (presente apenas no texto original)</li>
            <li><span style="color: green">+ Texto</span>: Linha adicionada (presente apenas no texto modificado)</li>
            <li><span style="color: black">  Texto</span>: Linha sem alterações (presente em ambos os textos)</li>
        </ul>
    </div>
    """

    # Formata o resultado para HTML com cores
    formatted_diff = []
    for line in diff:
        if line.startswith('+'):
            # Linha adicionada (presente apenas no segundo texto)
            formatted_diff.append(f'<span style="color: green">{line}</span>')
        elif line.startswith('-'):
            # Linha removida (presente apenas no primeiro texto)
            formatted_diff.append(f'<span style="color: red">{line}</span>')
        elif line.startswith('?'):
            # Linha de indicação de mudanças - ignoramos
            continue
        else:
            # Linha sem alterações
            formatted_diff.append(line)

    # Junta a legenda com as diferenças
    result = legend + '<div style="font-family: monospace;">' + '<br>'.join(formatted_diff) + '</div>'

    return result


# Cria a interface do Gradio
interface = gr.Interface(
    fn=compare_texts,
    inputs=[
        gr.Textbox(label="Texto 1", lines=5, placeholder="Digite o primeiro texto aqui..."),
        gr.Textbox(label="Texto 2", lines=5, placeholder="Digite o segundo texto aqui...")
    ],
    outputs=gr.HTML(label="Diferenças Encontradas"),
    title="Comparador de Textos",
    description="""
    Compare dois textos e veja as diferenças entre eles.
    O sistema mostrará as linhas que foram adicionadas, removidas ou mantidas sem alterações.
    Use a legenda abaixo para entender o significado das cores e símbolos.
    """,
    theme="default"
)

# Inicia o servidor com configurações específicas
interface.launch(server_port=7861)

