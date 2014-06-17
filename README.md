# Whitespace

Sublime Text has options `trim_trailing_white_space_on_save` and `ensure_newline_at_eof_on_save` to handle whitespace.
In some situations, these options do not give satisfactory result. While similar packages exist, e.g., [TrailSpaces](https://github.com/SublimeText/TrailingSpaces), they do not allow easier syntax specific settings.
Whitespace helps in keeping your code clean by providing more features in removing trailing spaces.

- remove trailing whitespace 
- ensure single trailing newline
- ignore whitespace only lines
- ignore whitespace on current line


# Installation
These plugin can be (in the future) installed via package control.

# Options
- The easiest way to apply "remove trailing whitespace" is by Command Palette `C+Shift+P`. 

- To activate "remove trailing whitespace on save", click the menu items in `Edit -> Whitespace`.

- To enable Whitespace at startup, modify your preference setting file:

```
{
    "remove_trailing_whitespace_on_save": true,
    "ensure_single_trailing_newline": true,
    "ignore_whitespace_only_lines": false,
    "ignore_whitespace_on_current_line": true
}
```

The optoins explain themselves. Their default values are `false`. You can also make use of [Syntax Manager](https://github.com/randy3k/SyntaxMgr) to enable Whitespace for multiple syntaxes.
