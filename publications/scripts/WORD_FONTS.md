# Native equation fonts

Italic styling and font selection are separate. An italic Greek variable in
Cambria Math does not have the same outline as its Computer Modern counterpart
in a LaTeX PDF. Latin Modern Math provides an OpenType MATH font intended to
retain the appearance of Computer Modern. Font choice also affects Latin
variables, symbols and equation spacing; it cannot make different layout
engines pixel-identical.

`word_fonts.embed_math_font(document, font_file, family="Latin Modern Math")`
applies a caller-supplied font to native OMML runs and the document's math
settings, and embeds the complete font as an obfuscated OpenType package part.
Use it after document formatting. Equation structures and explicit italic or
Roman styles remain intact; body text styles are preserved. Repeated embedding
of the same font reuses its package part and relationship.

The helper reads OpenType tables without extra Python dependencies. It requires
a MATH table and permits editable outline embedding according to the OS/2
embedding flags. The exporter does not distribute font binaries in Git. Obtain
the selected font under its own license; Latin Modern Math is included in the
Debian/Ubuntu `fonts-lmodern` package, whose font data and notices identify the
GUST Font License. Its usual system path is
`/usr/share/texmf/fonts/opentype/public/lm-math/latinmodern-math.otf`.

Verify actual rendering separately from package structure. A renderer may ignore
embedded fonts and substitute another family. For a read-only PDF preview,
select the same family in the preview application and inspect the PDF's font
list; a missing Latin Modern Math entry is a failed font-fidelity check. A font
installation in the rendering environment can be necessary. Do not report
Microsoft Word or Google Docs fidelity based only on LibreOffice rendering.

References:

- [Latin Modern Math project and font documentation](https://www.gust.org.pl/projects/e-foundry/lm-math).
- [Microsoft: embedded OpenType font parts in Word](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/1663dabc-5d98-463f-889e-bcd9b77c3d34).
- [Microsoft: embedding custom fonts](https://support.microsoft.com/en-us/office/fonts/benefits-of-embedding-custom-fonts).
