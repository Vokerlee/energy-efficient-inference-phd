# Journal equation typography

`journal_equations.apply_native_math` retains **every** mathematical expression
in Word's equation editor, including single variables and simple relations.
Use this profile when the document must remain entirely native OMML. It uses
one OpenType mathematical font (Cambria Math by default), with upright Greek
and native mathematical Latin italics. Body text fonts remain unchanged.
Ordinary-text italics and vertical offsets are removed from equation runs;
the equation engine controls their metrics and baseline. Inline summation
limits use explicit native side indices, including inside exponents; this
avoids importers that discard n-ary limit-placement properties. Display equations
retain their original limit placement. Set the document's math font to the
same family using the common settings helper or `word_fonts`.

Do not replace simple mathematical expressions with ordinary Word text, or
force variables into normal-text Times runs. Keep indices and accents as
native structures and style variables through OMML. Regenerate from LaTeX
when switching from an older text-conversion profile; applying this formatter
cannot reconstruct mathematics already converted to text.

Check a rendered document and the selected journal's current instructions.
Structural validation alone does not establish Microsoft Word layout fidelity;
a mathematical font may differ from a journal's requested text font.
