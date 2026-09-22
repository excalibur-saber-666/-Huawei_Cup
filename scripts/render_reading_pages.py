"""Render selected source PDF pages for read-only review (1-based page numbers)."""
import argparse
from pathlib import Path
import pypdfium2 as pdfium

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('pdf', type=Path)
p.add_argument('--pages', type=int, nargs='+')
p.add_argument('--find', nargs='+')
p.add_argument('--output', type=Path, default=Path('tmp/pdfs/reading'))
args = p.parse_args()
doc = pdfium.PdfDocument(args.pdf)
print(f'{args.pdf.name}: {len(doc)} PDF pages')
if args.find:
    for i in range(len(doc)):
        page = doc[i]
        textpage = page.get_textpage()
        text = textpage.get_text_range()
        hits = [term for term in args.find if term in text]
        if hits:
            print(f'PDF page {i+1}: {hits}')
        textpage.close()
        page.close()
if args.pages:
    args.output.mkdir(parents=True, exist_ok=True)
    for n in args.pages:
        if not 1 <= n <= len(doc):
            raise ValueError(f'Page out of range: {n}')
        page = doc[n-1]
        bitmap = page.render(scale=1.65)
        target = args.output / f'{args.pdf.stem}-p{n}.png'
        bitmap.to_pil().save(target)
        print(target.resolve())
        bitmap.close()
        page.close()
doc.close()
