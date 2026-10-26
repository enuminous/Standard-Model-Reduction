#!/usr/bin/env python3
"""Independent consistency checks for the three-line Standard Model reconstruction.

Requires Python 3.10+ and SymPy. No external data access required.
The tests establish local algebraic identities, NOT a new theory or parameter elimination.
"""
from fractions import Fraction as F
from math import sqrt, pi, sin, radians, isclose
from sympy import symbols, Matrix, sqrt as Ssqrt, simplify, expand

results = []
def check(name, condition, detail):
    if not condition:
        raise AssertionError(f'{name}: {detail}')
    results.append((name, detail))

# Hypercharges normalized Q = T3 + Y (not Q = T3 + Y/2).
yQ, yu, yd, yL, ye, yH = F(1,6), F(2,3), F(-1,3), F(-1,2), F(-1,1), F(1,2)
check('up-type Yukawa hypercharge', -yQ-yH+yu == 0, '-Y(Q) - Y(H) + Y(u) = 0')
check('down-type Yukawa hypercharge', -yQ+yH+yd == 0, '-Y(Q) + Y(H) + Y(d) = 0')
check('charged-lepton Yukawa hypercharge', -yL+yH+ye == 0, '-Y(L) + Y(H) + Y(e) = 0')

# All right-handed fermions appear with negative sign in left-handed anomaly sums.
a33y = 2*yQ-yu-yd
a22y = 3*yQ+yL
ayyy = 6*yQ**3-3*yu**3-3*yd**3+2*yL**3-ye**3
agravy = 6*yQ-3*yu-3*yd+2*yL-ye
for name, val in [('SU(3)^2 U(1)',a33y),('SU(2)^2 U(1)',a22y),('U(1)^3',ayyy),('gravitational U(1)',agravy)]:
    check('gauge anomaly '+name, val == 0, str(val))

# Higgs expansion about v with V= lambda (Hdag H - v^2/2)^2.
v,h,lamb = symbols('v h lambda', real=True, positive=True)
V = expand(lamb * (((v+h)**2 - v**2)/2)**2)
check('Higgs potential expansion', simplify(V - lamb*(v**2*h**2 + v*h**3 + h**4/4)) == 0, 'V(h) = lambda v² h² + lambda v h³ + (lambda/4) h^4')
check('Higgs mass relation', simplify(V.diff(h,2).subs(h,0) - 2*lamb*v**2) == 0, 'm_h² = 2 lambda v²')

g,gp = symbols('g gp', real=True, positive=True)
M2 = v**2/4*Matrix([[g*g,-g*gp],[-g*gp,gp*gp]])
check('massless photon eigenstate', simplify(M2.det())==0, 'det(M²_W3,B)=0')
check('Z mass eigenvalue', simplify(M2.trace()-v*v*(g*g+gp*gp)/4)==0, 'm_Z²=v²(g²+g\u2032²)/4')
check('W mass relation', simplify((g*v/2)**2-g*g*v*v/4)==0, 'm_W=gv/2')

# Numerical corrections to original figure.
beta_printed=11.7047
beta_sqrt157=sqrt(157)
gamma=sqrt(5)/13
print('Reported β = 11.7047, but β² =', format(beta_printed**2,'.8f'))
print('Correct sqrt(157) =', format(beta_sqrt157,'.10f'))
print('4 gamma beta / 39, with beta printed =', format(4*gamma*beta_printed/39,'.9f'))
print('4 gamma beta / 39, with beta sqrt157 =',format(4*gamma*beta_sqrt157/39,'.9f'))
print('sin²(27.58°) =',format(sin(radians(27.58))**2,'.9f'))
print('g_s(M_Z) corresponding to α_s(M_Z)=0.1180 =',format(sqrt(4*pi*0.1180),'.9f'))
print('Higgs quartic λ for m_h=125.20 GeV and v=246.22 GeV =',format((125.20/246.22)**2/2,'.9f'))
ratio_mu_e=105.6583755/0.51099895
print('m_mu/m_e =',format(ratio_mu_e,'.9f'))
print('geometric exponent log(m_mu/m_e)/log(11.7047) =',__import__('math').log(ratio_mu_e)/__import__('math').log(beta_printed))
check('original beta arithmetic fails',not isclose(beta_printed,beta_sqrt157,rel_tol=1e-4),'11.7047 ≠ sqrt(157)')
check('original strong coupling arithmetic fails',not isclose(4*gamma*beta_printed/39,0.1179,rel_tol=1e-4),'0.20649 ≠ 0.1179')
check('original equal mass-ladder hypothesis fails for e/mu',
      not any(isclose(ratio_mu_e,beta_printed**n,rel_tol=0.01) for n in range(-15,16)),
      '206.77 is not an integer power of 11.7047 within 1%')

# Independent physical parameter count in the minimal 3-generation SM, strong theta included.
counts={'gauge couplings':3,'Higgs parameters':2,'charged fermion masses':9,'CKM mixing parameters':4,'strong CP theta':1}
check('minimal SM parameter count',sum(counts.values())==19,str(counts)+' => 19')

print('\nAll',len(results),'symbolic/consistency checks passed:')
for i,(name,detail) in enumerate(results,1):
    print(f'{i:>2}. {name}: {detail}')
print('\nNOTE: These checks verify algebra and identify errors; they do not imply experimentally validated zero-parameter geometry.')
