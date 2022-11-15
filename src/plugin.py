# plugin.py

import re

from pathlib import Path
from mkdocs.plugins import BasePlugin

import markdown as md


def span(txt, open, close, case=1):
    inner = txt
    closings = sorted(
      [(m.start(), 1) for m in re.finditer(open, inner)] +
      [(m.start(), -1) for m in re.finditer(close, inner)])
    for (idx, v) in closings:
        case += v
        if not case:
            return idx
    return -1


class Image2FigurePlugin(BasePlugin):

    def on_page_markdown(self, markdown, config, **kwargs):
        converter = md.Markdown(
          extensions=config['markdown_extensions'],
          extension_configs=config['mdx_configs'] or {})
        instance = 1
        txt = markdown
        prev = 0
        response = ""
        for m in re.finditer("\!\[", txt):
            start = head = m.end()
            offset = span(txt[m.end():], "\[", "\]")
            caption = txt[head:head + offset]
            head += offset + 1

            link_offset = span(txt[head:], "\(", "\)", case=0)
            link = txt[head:head + link_offset + 1].strip()[1:-1].strip()
            head += link_offset + 1

            all_attrs = []
            maybe_attr = re.search("\{", txt[head:])
            if maybe_attr and not txt[head + 1:head + maybe_attr.start()].strip():
                head += maybe_attr.start() + 1
                attr_offset = span(txt[head:], "\{", "\}", case=1)
                all_attrs = txt[head:head + attr_offset].split()
                head += attr_offset + 1

            attrs = []
            for attr in all_attrs:
                ref = re.match(r"#fig:(\w+)", attr)
                if ref:
                    attrs.append(rf'id="fig:{ref.groups()[0]}"')
                else:
                    attrs.append(attr)

            attr_list = " ".join(attrs)
            caption = converter.convert(caption)
            response += txt[prev:start - 2]
            response += (
              r'<figure class="figure-image">'
              rf'    <img src="{link}" {attr_list}>'
              rf'    <figcaption>Figure {instance}. {caption}</figcaption>'
              r'</figure>')
            instance += 1
            prev = head

        response += txt[prev:]
        return response
