"""Generate the two-panel TikZ plot from the proved one-point kernel formula."""
from pathlib import Path
import json, math, sys

target=Path(sys.argv[1])
target.parent.mkdir(parents=True,exist_ok=True)
a=1/3
degrees=[30,120,600]
styles=['blue!65!black,thick','blue!65!black,dashed,thick','red!65!black,densely dotted,thick']

def log_tail(m,t):
    r=max(m//3-2,0)
    if t==0:return 0.0 if r==0 else -math.inf
    if t==1:return 0.0
    terms=[math.lgamma(m+1)-math.lgamma(j+1)-math.lgamma(m-j+1)
           +j*math.log(t)+(m-j)*math.log1p(-t) for j in range(r,m+1)]
    largest=max(terms)
    return min(0.0,largest+math.log(sum(math.exp(x-largest) for x in terms)))

def equilibrium(t):
    return a*math.log(t/a)+(1-a)*math.log((1-t)/(1-a)) if t<a else 0.0

def points(data):
    return ' '.join(f'({x:.6f},{y:.6f})' for x,y in data)

lines=[r'\begin{tikzpicture}[font=\small,line width=.65pt]',
       r'\begin{scope}[x=4.6cm,y=2.4cm]',
       r'\draw[->] (0,0)--(1.08,0) node[right] {$t$};',
       r'\draw[->] (0,0)--(0,1.23);',
       r'\node at (.5,1.32) {$2B_m/m^2$};',
       r'\node[below left] at (0,0) {$0$};',
       r'\draw (1,.02)--(1,-.02) node[below] {$1$};',
       r'\draw (.02,1)--(-.02,1) node[left] {$1$};',
       r'\draw[gray,densely dotted] (.333333,0)--(.333333,1.19);',
       r'\node[below] at (.333333,0) {$a$};',
       r'\begin{scope}\clip (0,0) rectangle (1,1.2);']
for m,style in zip(degrees,styles):
    d=(m+1)*(m+2)/2
    data=[(i/300,2*d/m**2*math.exp(log_tail(m,i/300))) for i in range(301)]
    lines.append(r'\draw['+style+'] plot coordinates {'+points(data)+'};')
lines += [r'\draw[black,very thick] (0,0)--(.333333,0);',
          r'\draw[black,very thick] (.333333,1)--(1,1);',
          r'\end{scope}\end{scope}',
          r'\begin{scope}[xshift=5.8cm,x=4.6cm,y=2.4cm]',
          r'\draw[->] (0,0)--(1.08,0) node[right] {$t$};',
          r'\draw[->] (0,0)--(0,1.23);',
          r'\node at (.5,1.32) {$U_m$};',
          r'\node[below left] at (0,0) {$-1$};',
          r'\draw (1,.02)--(1,-.02) node[below] {$1$};',
          r'\draw (.02,1)--(-.02,1) node[left] {$0$};',
          r'\draw[gray,densely dotted] (0,1)--(1,1);',
          r'\draw[gray,densely dotted] (.333333,0)--(.333333,1.19);',
          r'\node[below] at (.333333,0) {$a$};',
          r'\begin{scope}\clip (0,0) rectangle (1,1.22);']
for m,style in zip(degrees,styles):
    d=(m+1)*(m+2)/2
    data=[(t,(math.log(d)+log_tail(m,t))/m+1) for t in [0.01+0.99*i/300 for i in range(301)]]
    lines.append(r'\draw['+style+'] plot coordinates {'+points(data)+'};')
data=[(t,equilibrium(t)+1) for t in [0.01+0.99*i/300 for i in range(301)]]
lines += [r'\draw[black,very thick] plot coordinates {'+points(data)+'};',r'\end{scope}\end{scope}']
for x,style,label in zip([0.25,3.0,5.75,8.5],styles+['black,very thick'],['$m=30$','$m=120$','$m=600$','limit']):
    lines.append(f'\\draw[{style}] ({x},-.65)--({x+.55},-.65) node[right] {{{label}}};')
lines.append(r'\end{tikzpicture}')
target.write_text('\n'.join(lines)+'\n')

# Independent numerical integration checks the plotted density's normalization.
checks=[]
steps=1200
for m in degrees:
    d=(m+1)*(m+2)/2;r=max(m//3-2,0);count=d-r*(r+1)/2
    values=[]
    for i in range(steps+1):
        t=i/steps
        values.append(2*t*2*d/m**2*math.exp(log_tail(m,t)))
    integral=(values[0]+values[-1]+4*sum(values[1:-1:2])+2*sum(values[2:-1:2]))/(3*steps)
    exact=2*count/m**2
    assert abs(integral-exact)<2e-8,(m,integral,exact)
    checks.append({'degree':m,'vanishing_order':r,'normalized_dimension':exact,
                   'density_integral_simpson':integral,'absolute_error':abs(integral-exact)})
record={'parameters':{'q':2,'a':'1/3','degrees':degrees},
        'formula':'(2/m^2) binom(m+2,2) sum_{j=max(floor(m/3)-2,0)}^m binom(m,j)t^j(1-t)^(m-j)',
        'potential':'log(B_m)/m; the plot omits t<0.01 in the potential panel',
        'limiting_mass':'8/9','checks':checks}
target.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
