# -*- coding:utf-8 -*-
"""
textwrap
"""
import textwrap

simple_text = """
              this is a best module of do the text.\t it has the public interface
               wrap and fill. \t it has define the class TextWrap, and the class has
               some params like width,initial_indent,subsequent_indent,expend_tabs
               and so on.
              """
simple_text = textwrap.dedent(simple_text)   #去除缩进
fill_text = textwrap.fill(simple_text, 40,
                          initial_indent=' '*2,  #first line indent
                          subsequent_indent=' '*6,   #all lines save first line
                          expand_tabs=True,  #\t被space替代
                          )
print fill_text

wrap_text = textwrap.wrap(simple_text, 40)
print wrap_text