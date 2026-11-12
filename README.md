# No.56 — Internal–Leaf Inequalities and a Positive Limiting Leaf Density

**Full title:** Internal–Leaf Inequalities and a Positive Limiting Leaf Density for Numerical Semigroups with Frobenius Number $2m+3$

**Author:** Ryutaro Yonezu — Independent Researcher  
**Version:** v1.0 / 5 November 2026 / Preprint  
**Publication:** v1.0 limited preprint.  
**DOI:** 10.5281/zenodo.23981119  
**Repository:** https://github.com/yonezaemon1-hub/no56-numerical-semigroup-internal-leaf-density  
**Zenodo:** https://doi.org/10.5281/zenodo.23981119  
**Rights:** All rights reserved, including the supplied verification sources; no MIT, CC, or other open license is granted.  
**Human peer review:** Not human peer-reviewed.  
**Independent AI mathematical audit:** PASS within its author-reported scope.  
**References:** PARTIAL. **Novelty:** INCONCLUSIVE.  
**Windows reproduction:** author-run PowerShell 5.1; Python and C++17 PASS reported in the author's original transcript. Its byte-hash match was reported in the supplied audit materials; this publication preparation did not receive or re-inspect the private log.

## Results and scope

For numerical semigroups of multiplicity $m\ge6$ and Frobenius number $F=2m+3$, let $I_m$ and $L_m$ count internal nodes and leaves in the **full** numerical-semigroup tree. This preprint gives a fixed-family strengthening of Casas–Madrid–Rosales Conjecture 41: $I_m\ge3L_m$ for $m\ge6$, and $I_m\ge5L_m$ for all $m\ge12$. The second threshold is minimal for eventual validity; the inequality also holds at $m=10$. The leaf proportion has a positive limit $c$ with the certified enclosure $0.1314883<c<0.1446435$ and an explicit exponential error bound. That error bound is conservative for small and moderate $m$.

The total $N_m=7\cdot2^{m-4}$ is previously known. The unrestricted Conjecture 41 is not solved. Full-tree leaves differ from leaves in the specially pruned leaf-discriminating enumeration trees. Theorem-level originality has not been established.

## Files

The following list describes the prepared repository distribution. The separate reproducibility ZIP contains only this README, LICENSE, a package checksum manifest, and the five files in `repro/`; the manuscript, bibliography, release description and publication status remain separate repository documents.

- `No56_v1.0_PREPRINT_20261105.pdf`: v1.0 manuscript.
- `PAPER_EN.md`: source manuscript; the mathematical body and references are unchanged from v0.3.1.
- `No56_v1.0_REPRODUCIBILITY_20261105.zip`: public reproducibility package.
- `repro/`: the four byte-preserved sources and their original checksum manifest.
- `BIBLIOGRAPHY_VERIFICATION.md`: public bibliographic verification supplement, retaining REFERENCES PARTIAL.
- `RELEASE_TEXT_EN.md`: release description and abstract.
- `SHA256SUMS.txt`: exact public source/document inventory; excludes itself and the separately packaged PDF/ZIP.
- `No56_SHA256SUMS_RELEASE_20261105.txt`: final PDF and ZIP checksums, when packaged.

## Windows PowerShell 5.1 reproduction

Extract the reproducibility ZIP, enter its `repro` directory, and run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\run_windows.ps1
```

The frozen runner checks four source hashes and exact directory inventory, then runs the two Python programs. It **does not compile or execute C++**. It uses `py -3.12` when the Windows Python launcher exists, otherwise `python`; the Python source itself uses only the standard library and supports Python 3.10+. The runner's final `RELEASE HOLD` text and the verifiers' older Windows status messages are historical strings preserved with the frozen code; current verification and publication status are given in this README.

Compile and execute the C++17 verifier separately with an existing GCC-compatible C++17 compiler. Keep build products outside `repro` so the frozen runner's exact inventory check remains valid:

```powershell
New-Item -ItemType Directory -Force ..\build | Out-Null
g++ -std=c++17 -O2 -Wall -Wextra -o ..\build\no56_check.exe .\verify_no56_independent.cpp
if ($LASTEXITCODE -ne 0) { throw 'C++ build FAIL' }
& ..\build\no56_check.exe
if ($LASTEXITCODE -ne 0) { throw 'C++ verification FAIL' }
```

The old external v0.1-specific Windows launcher is not an execution method for this v1.0 ZIP.

## Linux reproduction

From the extracted package root:

```bash
(cd repro && sha256sum -c SHA256SUMS.txt)
python3 -I repro/verify_no56.py
python3 -I repro/verify_no56_interval.py
mkdir -p build
g++ -std=c++17 -O2 -Wall -Wextra -o build/no56_check repro/verify_no56_independent.cpp
./build/no56_check
```

The Python verifier checks explicit membership counts for $m=6,\ldots,15$ and finite prefix values. The C++ verifier checks $m=6,\ldots,24$ and independently computes $Q_{32}=543583947/3758096384$. The interval verifier checks exact rational arithmetic **conditional on** that count. During v1.0 preparation, all three supplied programs were rerun on Linux and passed; this rerun is separate from the author-reported independent AI audit.

## Evidence provenance

The author reports that an independent AI auditor wrote separate Linux implementations, enumerated $m=6,\ldots,22$, checked prefix counts through $Q_{32}$, and reviewed the conditional Harris argument. The reported verdict is PASS within scope. This is AI review and is not human peer review or a novelty guarantee.

The author also supplied an earlier Windows PowerShell 5.1 transcript reporting Python and C++17 PASS on the unchanged original v0.1 package. The supplied audit report states that its SHA256 matched the author-reported value:

```text
b3d94afab5686bedeb23b1f961b5b69830faa008284127ff776e2677d0b49fee
```

This is metadata only. The private raw Windows log, machine identifiers, user identifiers, local filesystem paths, and internal audit histories are excluded. A matching hash confirms submitted bytes against a reported hash; it does not independently authenticate the machine execution process. The raw transcript was not part of the v0.3.1 publication candidate and was not re-inspected during this preparation.

The v0.3.1 bibliography session checked primary-source metadata and selected passages. Comprehensive theorem-level overlap checking remains incomplete. **REFERENCES PARTIAL / NOVELTY INCONCLUSIVE / NOT HUMAN PEER-REVIEWED.**

## Author correspondence (metadata update, 2026-11-12)

**Ryutaro Yonezu — Independent Researcher**  
Research correspondence: **yonezaemon1+research@gmail.com**

This contact-information addition does not revise any mathematical claims, frozen verification files, published preprint PDF, release assets, DOI, or existing SHA256 checksums.
