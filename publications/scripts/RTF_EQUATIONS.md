# Native equations in RTF

RTF 1.9.1 supports editable Office Math. A layout converter can nevertheless
write picture-only math groups, so a `.rtf` extension or an `mmath` wrapper does
not establish editability.

`rtf_equations.restore_native_math(source_docx, layout_rtf)` replaces those math
groups with native structures serialized from the original DOCX. The surrounding
layout, ordinary text and illustration data remain with the layout converter.
There must be one RTF math group per source equation, in document order.
Math-only fonts omitted by the layout exporter are declared in its font table
before serialization. Existing font identifiers and body formatting are retained.
Unimplemented OMML constructs, unsupported font names and mismatched counts are errors;
the helper does not replace an unsupported expression with an image.

The supported subset covers the manuscript's fractions, delimiters, n-ary
operators, accents, lower limits, underbraces, aligned rows and index structures.
Normal text, math alphabets and explicit character properties are preserved.
The RTF parser honors escaped braces and binary data. Unicode is emitted as
signed UTF-16 RTF controls, including supplementary-plane symbols.

Validate the resulting file by importing it into a separate document: compare
the number of equations, structural operators, delimiter/accent characters and
each equation's text with the source. Preserve the original DOCX and do not use
the round-trip document as a replacement for it. Check visible layout separately.

Format references: Microsoft's *Rich Text Format Specification 1.9.1*,
Mathematics section, and the [LibreOffice RTF math implementation](https://github.com/LibreOffice/core/blob/master/starmath/source/rtfexport.cxx).
