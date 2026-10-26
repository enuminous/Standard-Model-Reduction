# From an Expanded Standard Model Lagrangian to Three Lines: A Correct Geometric Reconstruction and a Conditional 39-Strata Research Program

**Independent technical reconstruction — 26 October 2026**  
**Status:** standard-model rewriting VERIFIED at the classical gauge-invariant level; original claimed parameter-free lattice reduction NOT ESTABLISHED.

## Abstract

A public illustration claims that an expanded Standard Model (SM) Lagrangian is equivalent to a three-line 'S-DMT' geometric Lagrangian with 39 strata and no free parameters. The displayed model contains arithmetic inconsistencies, lacks an explicit gauge-invariant mass mechanism, and does not derive the measured flavor parameters. We give an exact, compact three-line presentation of the *minimal gauge-invariant classical SM*, define every abbreviation, verify gauge/Yukawa consistency and anomaly cancellation, and explain precisely why this is compression of notation rather than elimination of physical parameters. We further formulate a conditional 39-site geometric overlap model that could become predictive only after its graph, operator, state normalizations, couplings, and boundary conditions are fixed independently of SM masses and mixing measurements. Tests are supplied in `verify_standard_model_reduction.py`.

## 1. Three-line master Lagrangian: correct statement

Work on four-dimensional Minkowski space, metric signature (+,−,−,−), natural units ℏ=c=1, with SU(3)_C × SU(2)_L × U(1)_Y and Q=T_3+Y. Fermion fields and generation indices are summed.

$$
\boxed{\begin{aligned}
\mathcal L_{\rm SM}={}&-\frac14(G^a_{\mu\nu}G^{a\mu\nu}+W^I_{\mu\nu}W^{I\mu\nu}+B_{\mu\nu}B^{\mu\nu}) +\sum_{f\in\mathcal F}\bar f\,i\gamma^\mu D_\mu f\\
& +(D_\mu H)^\dagger D^\mu H-\lambda\bigl(H^\dagger H-v^2/2\bigr)^2\\
&-\left(\bar Q_LY_u\widetilde H u_R+\bar Q_LY_d H d_R+\bar L_LY_eH e_R+{\rm h.c.}\right)+\frac{\theta_3g_s^2}{32\pi^2}G^a_{\mu\nu}\widetilde G^{a\mu\nu}.
\end{aligned}}
$$

This is *the minimal renormalizable gauge-invariant classical Standard Model*, including the possible strong CP topological operator; apart from an irrelevant constant in the potential, its content agrees with expanded classical SM formulas. For a gauge-fixed quantum-path-integral formula one must additionally specify $\mathcal L_{\rm gauge\ fixing}+\mathcal L_{\rm FP\ ghosts}$; the compact formula does not assert that these disappear.

The numerical coefficients $g_s,g,g',v,\lambda$, the Yukawa matrix entries (modulo field-basis redundancies), and $\theta_3$ remain empirical parameters. Compressing them into $D_\mu$, $Y_f$, or a geometric label does not derive them.

## 2. Exact definitions hidden in the notation

Each generation contains the fermion representations below, expressed as (SU(3),SU(2),Y):

| Field | Representation |
|:--|:--|
| $Q_L=(u_L,d_L)^T$ | $(\mathbf3,\mathbf2,+1/6)$ |
| $u_R$ | $(\mathbf3,\mathbf1,+2/3)$ |
| $d_R$ | $(\mathbf3,\mathbf1,-1/3)$ |
| $L_L=(\nu_L,e_L)^T$ | $(\mathbf1,\mathbf2,-1/2)$ |
| $e_R$ | $(\mathbf1,\mathbf1,-1)$ |
| $H$ | $(\mathbf1,\mathbf2,+1/2)$ |

$\mathcal F$ sums all chiral multiplets in all three generations. Define $\widetilde H=i\sigma^2H^*$ and, for each representation,

$$
D_\mu=\partial_\mu-ig_sG^a_\mu T^a-igW^I_\mu\frac{\sigma^I}{2}-ig'YB_\mu.
$$

The generators act trivially on singlets. The corresponding curvatures are

$$
\begin{aligned}
G^a_{\mu\nu}&=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_sf^{abc}G^b_\mu G^c_\nu,\\
W^I_{\mu\nu}&=\partial_\mu W^I_\nu-\partial_\nu W^I_\mu+g\epsilon^{IJK}W^J_\mu W^K_\nu,\\
B_{\mu\nu}&=\partial_\mu B_\nu-\partial_\nu B_\mu,
\end{aligned}
$$

where the signs follow the chosen $D_\mu=\partial_\mu-igA_\mu$ convention, because $[D_\mu,D_\nu]=-ig F_{\mu\nu}$. $\widetilde G^{a\mu\nu}=\tfrac12\epsilon^{\mu\nu\rho\sigma}G^a_{\rho\sigma}$.

**Geometry, made exact:** $G,W,B$ are local components of a connection $A$ on a principal $SU(3)\times SU(2)\times U(1)$ bundle; $F_A$ is its curvature; the fermions and Higgs are sections of associated bundles; the Yukawa matrices are fiberwise morphisms between the corresponding representation bundles. The three-line Lagrangian is thus already geometric. No extra 39-strata postulate is needed for the equivalence.

## 3. Gauge-invariant Yukawa sector

The three hypercharge sums vanish exactly:

$$
-Y(Q_L)-Y(H)+Y(u_R)=0,\qquad
-Y(Q_L)+Y(H)+Y(d_R)=0,\qquad
-Y(L_L)+Y(H)+Y(e_R)=0.
$$

Bare masses of chiral SM fermions violate electroweak gauge invariance before symmetry breaking. Thus the proposed original second-line formula $m_k\bar\psi_k\psi_k$, if interpreted as SM fermion mass terms in the unbroken theory, is not a valid substitute for the Yukawa sector. The repair is the three Yukawa-matrix operators displayed above.

The quark mass matrices after symmetry breaking are $M_u=vY_u/\sqrt2$, $M_d=vY_d/\sqrt2$ and charged-lepton $M_e=vY_e/\sqrt2$. After biunitary diagonalization $U_{uL}^\dagger M_uU_{uR}=\mathrm{diag}(m_u,m_c,m_t)$ and similarly for $d$, the physical CKM matrix is $V_{\rm CKM}=U_{uL}^\dagger U_{dL}$. The geometric progression $m_k=m_c\beta^{k-18}$ has no justification and is removed.

The **minimal renormalizable SM** has *massless neutrinos* and hence no observable PMNS matrix in that strict formulation. Neutrino masses and PMNS mixing require an explicit extension such as the dimension-five Weinberg operator or sterile right-handed neutrinos. For instance,

$$
\Delta\mathcal L_\nu=-\frac{C_{ij}}{2\Lambda}(\overline{L_i^c}\,\widetilde H^*)(\widetilde H^\dagger L_j)+{\rm h.c.}
$$

leads to a Majorana mass matrix $M_\nu=Cv^2/(2\Lambda)$, with matrix-specific phase/sign conventions. This is a *nonrenormalizable extension*, not a zero-cost improvement to the minimal SM.

## 4. Higgs sector, derived rather than postulated

Take $H=(0,(v+h)/\sqrt2)^T$ in unitary gauge. Then

$$
\begin{aligned}
V(h)&=\lambda\left(\frac{(v+h)^2-v^2}{2}\right)^2\\
&=\lambda v^2h^2+\lambda vh^3+\frac\lambda4h^4,
\end{aligned}
$$

implying

$$
m_h^2=2\lambda v^2,\qquad
m_W=\frac{gv}{2},\qquad
m_Z=\frac{v}{2}\sqrt{g^2+g'^2},\qquad
\tan\theta_W=\frac{g'}g.
$$

The neutral $(W^3,B)$ mass-squared matrix is

$$
\mathsf M_0^2=\frac{v^2}{4}\begin{pmatrix}g^2&-gg'\\-gg'&g'^2\end{pmatrix}.
$$

It has a zero eigenvalue (the photon) and one eigenvalue $m_Z^2$. Therefore electroweak mass generation and mixing follow from the two operators already present in lines one and two. **But** a physical Higgs mass of about 125 GeV is not predicted by the expression until $v$ and $\lambda$ have been fixed by independent theory or empirical inputs.

Numerical example using $m_h=125.20\,\mathrm{GeV}$ and $v=246.22\,\mathrm{GeV}$: $\lambda=m_h^2/(2v^2)\simeq0.12928$ at tree level. This is an empirical inference, not a lattice prediction; loop-level relations require a specified scheme and scale.

## 5. Anomaly cancellation (exact algebra)

A candidate microscopic geometry must reproduce anomaly freedom of the SM. For each generation, treating right-handed states with the required negative anomaly sign,

$$
\begin{aligned}
SU(3)^2 U(1):&\quad 2Y_Q-Y_u-Y_d=0,\\
SU(2)^2 U(1):&\quad 3Y_Q+Y_L=0,\\
U(1)^3:&\quad 6Y_Q^3-3Y_u^3-3Y_d^3+2Y_L^3-Y_e^3=0,\\
\mathrm{grav}^2U(1):&\quad 6Y_Q-3Y_u-3Y_d+2Y_L-Y_e=0.
\end{aligned}
$$

The accompanying Python verifies these with exact rational arithmetic. Local anomalies vanish and the SM has an even number of left-handed $SU(2)$ doublets per generation (3 colored quark doublets + 1 lepton doublet), avoiding the Witten SU(2) global anomaly.

## 6. Correcting the illustration's numerical claims

| Illustrated assertion | Exact check | Finding |
|:--|:--|:--|
| $\sqrt{157}=11.7047$ | $\sqrt{157}=12.52996409$; $11.7047^2\simeq137.00000209$ | Arithmetic FAIL; likely 137/157 confusion |
| $\gamma=\sqrt5/13,\;4\gamma\beta/39=0.1179$ | With illustrated $\beta=11.7047$: $0.20648919$; with correct $\sqrt{157}$: $0.22104814$ | Arithmetic FAIL |
| $0.1179$ represents $g_s$ | $\alpha_s=g_s^2/(4\pi)$; for $\alpha_s(M_Z)=0.1180$, $g_s(M_Z)=1.21772$ | Gauge coupling/convention FAIL |
| $\theta_W=27.58^\circ$ | $\sin^2(27.58^\circ)=0.21435665$ | Not equal to standard effective or on-shell values; scheme must be specified |
| Consecutive masses follow one lattice ratio $\beta$ | $m_\mu/m_e\simeq206.7683$; no integer power of $11.7047$ within 1% | Mass hypothesis FAIL for direct physical-mass interpretation |

PDG 2025 gives $\alpha_s(M_Z^2)=0.1180\pm0.0009$ and $m_H=125.20\pm0.11$ GeV (PDG 2025 Higgs listing). The weak mixing angle depends on renormalization scheme; an isolated angle cannot be compared meaningfully without a scheme/scale.

## 7. Actual physical parameter accounting

For the conventional three-generation **minimal SM with massless neutrinos**, up to field-basis redundancies:

| Sector | Independent physical parameters |
|:--|--:|
| Gauge couplings $g_s,g,g'$ | 3 |
| Higgs potential $v,\lambda$ | 2 |
| Six quark masses and three charged-lepton masses | 9 |
| Three CKM angles plus one CP phase | 4 |
| QCD strong CP angle $\bar\theta$ | 1 |
| **Total including strong CP** | **19** |

Without the strong CP angle this is 18. Massive-neutrino extensions bring additional parameters. Field redefinitions change how parameters are displayed, not the count of independent physical observables.

**Geometric no-free-coupling obstruction.** Even if the gauge bundle and its topology are fixed, the most general positive gauge-invariant quadratic form on the direct-sum gauge algebra has one independent normalization on each simple or Abelian factor. With the alternative convention where the connection $A$ does not absorb the couplings, the kinetic density is proportional to $-(1/4)[c_3\,\mathrm{tr}(F_3^2)+c_2\,\mathrm{tr}(F_2^2)+c_1 F_1^2]$ for arbitrary $c_3,c_2,c_1>0$. These correspond to the three gauge couplings after a choice of normalization. **Topology alone does not fix these continuous weights**. A zero-parameter claim must supply an extra theorem or physical principle that does. Likewise, Yukawa matrices are additional bundle morphisms, not fixed by the fact that suitable morphisms exist. In the presence of complex quark mass matrices, the physically measurable strong-CP combination is $\bar\theta=\theta_3+\arg\det(M_uM_d)$ (with convention-dependent overall signs).

## 8. Best-effort 39-strata *conditional* geometry: an explicit, testable ansatz

The graphic invokes a 39-strata lattice but does not specify the operator or its mapping to particle multiplets. A repairable research proposal is to define a finite internal set $K=\{1,\ldots,39\}$, positive weights $w_k$, and three-dimensional normalized families of left/right eigenmodes of a precisely specified discrete Dirac operator $D_K$. A candidate Yukawa matrix could be induced by internal overlap:

$$
(Y_f)_{ij}=g_*\sum_{k=1}^{39}w_k\,u^{(f)*}_{L,i}(k)\,h_f(k)\,u^{(f)}_{R,j}(k),
\quad f\in\{u,d,e\}.
$$

The internal Higgs profile $h_f$ must transform with the correct SM quantum numbers; $u_L,u_R$ must transform in correct SM representations; measures and mode normalizations must be given. Without these the overlap is only a formal ansatz. For the up quarks the appropriate Higgs-conjugate map replaces the ordinary Higgs map. A realistic model must also show the low-energy scalar has exactly the observed Higgs degrees of freedom and must match gauge anomalies.

**Why this is not parameter elimination:** unconstrained site values can fit any $3\times3$ complex Yukawa matrix. For a concrete normalized construction, use nine sites labelled by pairs $k=(p,q)$ with $p,q=1,2,3$, set $w_k=g_*=1$, choose $u_{L,i}(p,q)=\delta_{ip}/\sqrt3$ and $u_{R,j}(p,q)=\delta_{jq}/\sqrt3$, and set $h(p,q)=3Y_{pq}$. Both families of site modes are orthonormal, and the resulting overlap is exactly $(Y_f)_{ij}=Y_{ij}$ for *any* chosen complex matrix. The remaining 30 sites contribute zero. This fits, rather than predicts, the matrix. Additional restrictions forcing these modes to arise from a specific operator could change this conclusion, but those restrictions must be stated and independently justified. Thus, unless $D_K$, $h$, $w$, $g_*$ and boundary conditions are derived from a parameter-free principle and fixed *before* fitting masses, the geometry only **relabels the free inputs**.

### Falsifiable geometric reduction criterion

A lattice-based claim is established only if its public code and proof give (i) a fully defined finite spectral/Dirac/Laplacian operator, (ii) non-arbitrary gauge representation content, (iii) induced Higgs and Yukawa maps, (iv) uniqueness or a finite enumeration of admissible backgrounds without measured SM inputs, (v) spectra and mixing predicted **before** comparison, (vi) anomaly cancellation, and (vii) measured observables within declared uncertainties after renormalization/running. The number '39' alone constrains none of these sufficiently.

## 9. Verified versus unresolved

- **PASS:** exact three-line *notation-level* reconstruction of the classical gauge-invariant minimal SM from its established field/representation definitions.
- **PASS:** hypercharge invariance of the three Yukawa monomials.
- **PASS:** four local anomaly checks; massless neutral gauge eigenstate; Higgs and W/Z tree-level mass relationships.
- **FAIL:** $\sqrt{157}=11.7047$; printed strong-coupling arithmetic; direct universal fermion mass ladder.
- **UNRESOLVED:** any equivalence to the illustrative 39-strata model because that model's mathematical definitions are missing.
- **UNRESOLVED:** any parameter-free derivation, lattice reduction, explanation of gauge-fixing removal, massive-neutrino sector, dark matter claims, or new empirical predictions.

**Conclusion:** A compact, mathematically legitimate *three-line formulation* of the SM exists, and it is geometric through connections, curvature and bundle representations. It does *not* remove 19 independent minimal-SM physical parameters. The 39-strata proposal can be reformulated as a concrete numerical/spectral hypothesis but is not a validated replacement for the Standard Model on current evidence.

## Sources and audit inputs

1. CERN, *Quantum Field Theory and the Electroweak Standard Model*, standard-model gauge, scalar and Yukawa Lagrangian: https://e-publishing.cern.ch/index.php/CYRSP/article/download/1380/1152/5908
2. CERN, *Introduction to the Standard Model of the Electroweak Interactions*: https://cds.cern.ch/record/1406310/files/CERN-2014-008.pdf
3. Particle Data Group, *Review of Particle Physics 2025*, QCD $\alpha_s$: https://pdg.lbl.gov/2025/reviews/rpp2025-rev-qcd.pdf
4. Particle Data Group, *2025 Higgs listing*: https://pdg.lbl.gov/2025/listings/rpp2025-list-higgs-boson.pdf
5. Particle Data Group, *2025 Electroweak Model and Constraints on New Physics*: https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf
6. Alonso, Jenkins & Manohar, *Geometry of the Scalar Sector* (2016): https://escholarship.org/uc/item/79z91541

**Reproduction:** `python verify_standard_model_reduction.py` (requires `sympy`).
