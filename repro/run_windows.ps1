# Windows PowerShell 5.1. Run with -NoProfile -ExecutionPolicy Bypass.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifest = Join-Path $root 'SHA256SUMS.txt'
if (-not (Test-Path -LiteralPath $manifest -PathType Leaf)) { throw 'FAIL-CLOSED: missing manifest' }
$rows = Get-Content -LiteralPath $manifest -Encoding UTF8
$expected = @{}
foreach ($row in $rows) {
    if ($row -notmatch '^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$') { throw 'FAIL-CLOSED: bad SHA256SUMS row' }
    $name = $Matches[2]
    if ($expected.ContainsKey($name)) { throw 'FAIL-CLOSED: duplicate manifest entry' }
    $expected[$name] = $Matches[1]
}
$actual = @(Get-ChildItem -LiteralPath $root -File | Where-Object { $_.Name -ne 'SHA256SUMS.txt' } | Select-Object -ExpandProperty Name)
if ($actual.Count -ne $expected.Count) { throw 'FAIL-CLOSED: inventory count mismatch' }
foreach ($name in $actual) {
    if (-not $expected.ContainsKey($name)) { throw "FAIL-CLOSED: unexpected file $name" }
    $got = (Get-FileHash -LiteralPath (Join-Path $root $name) -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($got -cne $expected[$name]) { throw "FAIL-CLOSED: hash mismatch $name" }
}
Write-Output "PASS: all $($expected.Count) file hashes and exact inventory"
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3.12 -I (Join-Path $root 'verify_no56.py')
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python -I (Join-Path $root 'verify_no56.py')
} else { throw 'FAIL-CLOSED: Python is unavailable' }
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: Python verification failed' }
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3.12 -I (Join-Path $root 'verify_no56_interval.py')
} else {
    & python -I (Join-Path $root 'verify_no56_interval.py')
}
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: exact interval verification failed' }
Write-Output 'PASS: No56 internal Python verification. RELEASE HOLD / NOVELTY INCONCLUSIVE.'
