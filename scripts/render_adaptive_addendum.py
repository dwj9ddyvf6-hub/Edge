from pathlib import Path
import re, html, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, KeepTogether, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.utils import ImageReader

REPO=Path(__file__).resolve().parents[1]
ROOT=REPO/'v2'
SKILL=ROOT/'skill'
OUT=REPO/'build'/'v2'
TMP=OUT/'render'
OUT.mkdir(parents=True,exist_ok=True); TMP.mkdir(parents=True,exist_ok=True)
FONT=Path(matplotlib.get_data_path())/'fonts/ttf'
for name,file in [('Body','DejaVuSans.ttf'),('BodyBold','DejaVuSans-Bold.ttf'),('BodyItalic','DejaVuSans-Oblique.ttf'),('Mono','DejaVuSansMono.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='BodyItalic',boldItalic='BodyBold')
navy=HexColor('#132E44'); teal=HexColor('#107D83'); gray=HexColor('#556575'); light=HexColor('#EEF4F6')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Text',fontName='Body',fontSize=9.5,leading=13.6,spaceAfter=6.5,textColor=navy,splitLongWords=True))
styles.add(ParagraphStyle(name='SmallText',parent=styles['Text'],fontSize=8.2,leading=11.5,spaceAfter=5))
styles.add(ParagraphStyle(name='Section',fontName='BodyBold',fontSize=19,leading=24,textColor=navy,spaceBefore=12,spaceAfter=13,keepWithNext=True))
styles.add(ParagraphStyle(name='Subsection',fontName='BodyBold',fontSize=12.4,leading=17,textColor=teal,spaceBefore=12,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle(name='Minor',fontName='BodyBold',fontSize=10.5,leading=14,textColor=navy,spaceBefore=9,spaceAfter=5,keepWithNext=True))
styles.add(ParagraphStyle(name='Cell',parent=styles['Text'],fontSize=8,leading=11,spaceAfter=0))
styles.add(ParagraphStyle(name='CellHead',parent=styles['Cell'],fontName='BodyBold',textColor=white))
styles.add(ParagraphStyle(name='CodeText',fontName='Mono',fontSize=7.4,leading=9.4,spaceAfter=8,textColor=navy,backColor=light,borderPadding=7))
styles.add(ParagraphStyle(name='TitleCustom',fontName='BodyBold',fontSize=38,leading=44,textColor=navy,spaceAfter=20))
styles.add(ParagraphStyle(name='SubtitleCustom',fontName='Body',fontSize=17,leading=24,textColor=teal,spaceAfter=22))

# Normalize typography that PDF extraction/renderers sometimes mishandle.
def clean(s):
 return s.replace('\u2011','-').replace('\u2013','-').replace('\u2014',' - ').replace('\u200b','').replace('\u00a0',' ')
def inline(s):
 s=html.escape(clean(s))
 s=re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',lambda m:'<link color="#107D83" href="'+m.group(2)+'">'+m.group(1)+'</link>',s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
 s=re.sub(r'`([^`]+)`',r'<font name="Mono" size="8.5">\1</font>',s)
 # Make bare URLs clickable while retaining exact readable targets.
 if s.startswith('https://') or s.startswith('http://'):
  s='<link color="#107D83" href="'+s+'">'+s+'</link>'
 return s

def para(s,style='Text'):
 return Paragraph(inline(s),styles[style])

math_count=0
def equation(text):
 global math_count
 math_count+=1
 text=' '.join(text.strip().splitlines())
 text=text.replace(r'\mathcal P',r'\mathcal{P}')
 text=text.replace(r'\mathbf1',r'\mathbf{1}').replace(r'\mathcal I',r'\mathcal{I}')
 fig=plt.figure(figsize=(11,1),dpi=180)
 fig.patch.set_alpha(0)
 fig.text(.02,.4,'$'+text+'$',fontsize=15,color='#132E44')
 name=TMP/f'equation_{math_count}.png'
 fig.savefig(name,bbox_inches='tight',pad_inches=.12,transparent=True)
 plt.close(fig)
 w,h=ImageReader(str(name)).getSize()
 width=min(475,w/1.8); height=width*h/w
 return Image(str(name),width=width,height=height,hAlign='LEFT')

WIDTH=612-108

def parse_markdown(text,compact=False):
 lines=text.splitlines(); story=[]; i=0
 # The individual references have local navigation lists; use part dividers in this report.
 while i<len(lines):
  line=lines[i].strip()
  if not line:
   i+=1;continue
  if line=='## Contents':
   i+=1
   while i<len(lines) and not lines[i].startswith('## '): i+=1
   continue
  if line.startswith('```'):
   block=[];i+=1
   while i<len(lines) and not lines[i].startswith('```'):
    # Wrap long code-template lines at sensible spaces, preserve content.
    import textwrap
    block.extend(textwrap.wrap(clean(lines[i]),width=87,replace_whitespace=False,drop_whitespace=False) or [''])
    i+=1
   story.append(Preformatted('\n'.join(block),styles['CodeText']));i+=1;continue
  if line==r'\[':
   block=[];i+=1
   while i<len(lines) and lines[i].strip()!=r'\]':block.append(lines[i]);i+=1
   story.extend([equation('\n'.join(block)),Spacer(1,8)]);i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    vals=[v.strip() for v in lines[i].strip().strip('|').split('|')]
    if not all(re.match(r'^:?-+:?$',v) for v in vals):rows.append(vals)
    i+=1
   n=len(rows[0]); rows=[r for r in rows if len(r)==n]
   data=[[para(c,'CellHead' if j==0 else 'Cell') for c in row] for j,row in enumerate(rows)]
   widths=[WIDTH/n]*n
   if n==3: widths=[WIDTH*.23,WIDTH*.385,WIDTH*.385]
   elif n==2:widths=[WIDTH*.25,WIDTH*.75]
   table=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
   table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,light]),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.7,teal)]))
   story.extend([table,Spacer(1,10)]);continue
  if line.startswith('# '):story.append(para(line[2:],'Section'));i+=1;continue
  if line.startswith('## '):story.append(para(line[3:],'Subsection'));i+=1;continue
  if line.startswith('### '):story.append(para(line[4:],'Minor'));i+=1;continue
  if re.match(r'^\d+\. ',line):
   story.append(para(line,'SmallText' if compact else 'Text'));i+=1;continue
  if line.startswith('- '):
   story.append(Paragraph('&#8226; '+inline(line[2:]),styles['SmallText' if compact else 'Text']));i+=1;continue
  group=[line];i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|- |\d+\. |\\\[)',lines[i].strip()):
   group.append(lines[i].strip());i+=1
  story.append(para(' '.join(group),'SmallText' if compact else 'Text'))
 return story


for style_name in ['Text','SmallText','Cell','CellHead']:
 styles[style_name].allowWidows=0
 styles[style_name].allowOrphans=0
story=[Spacer(1,40),para('TRADING EDGE LAB  /  ADDENDUM 2.0','Minor'),Spacer(1,25),para('Adaptive Edge','TitleCustom'),para('A master algorithm for better decisions, faster learning and disciplined control','SubtitleCustom'),para('Audit, deeper research and an implementable operating method for a strategy, sleeve or trading desk.'),Spacer(1,28)]
callout=Table([[para('THE DECISION THAT MATTERS','CellHead')],[para('Which feasible action improves the portfolio under the evidence we have, before the opportunity expires - and is further analysis worth its cost?')]],colWidths=[WIDTH])
callout.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('BACKGROUND',(0,1),(-1,1),light),('BOX',(0,0),(-1,-1),.5,teal),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),11),('BOTTOMPADDING',(0,0),(-1,-1),11)]))
story += [callout,Spacer(1,30),para('24 October 2026 UTC  |  Version 2.0','SmallText'),para('30 additional primary sources. Explicit equations, control logic, evidence contracts, operational tests and a small offline reference kernel. No market profitability or live deployment claimed.','SmallText'),PageBreak()]
parts=[('1  /  Audit and deeper findings',ROOT/'audit-findings.md'),('2  /  The master control algorithm',SKILL/'references/adaptive-control.md'),('3  /  Learning and evidence',SKILL/'references/adaptive-learning.md'),('4  /  Runtime and execution',SKILL/'references/desk-runtime.md'),('5  /  Annotated primary sources',SKILL/'references/adaptive-sources.md'),('6  /  Validation and use',ROOT/'validation.md')]
for j,(title,path) in enumerate(parts):
 if j:story.append(PageBreak())
 story.append(para(title,'Section'))
 txt='\n'.join(path.read_text().splitlines()[1:])
 story+=parse_markdown(txt,compact=(j==4))
def footer(canvas,doc):
 canvas.saveState();canvas.setStrokeColor(teal);canvas.setLineWidth(.5);canvas.line(54,45,558,45)
 canvas.setFont('Body',8);canvas.setFillColor(gray);canvas.drawString(54,31,'TRADING EDGE LAB  |  Adaptive-control addendum')
 canvas.drawRightString(558,31,str(doc.page))
 if doc.page>1:
  canvas.setFont('Body',7);canvas.drawRightString(558,763,'24 OCT 2026  /  v2.0')
 canvas.restoreState()
file=OUT/'Trading_Edge_Adaptive_Addendum.pdf'
doc=SimpleDocTemplate(str(file),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=50,bottomMargin=59,title='Trading Edge Lab: Adaptive Control Addendum',author='Trading Edge Lab research synthesis')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(file);print('Equations rendered:',math_count)
