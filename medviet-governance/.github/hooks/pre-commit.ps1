$ErrorActionPreference = 'Stop'

$rootDir = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$reportsDir = Join-Path $rootDir 'reports'
New-Item -ItemType Directory -Force -Path $reportsDir | Out-Null
Write-Host 'Running security checks...'

$status = 0

$python = Join-Path $rootDir '.venv\Scripts\python.exe'
$bandit = Join-Path $rootDir '.venv\Scripts\bandit.exe'
$pipAudit = Join-Path $rootDir '.venv\Scripts\pip-audit.exe'
$gitSecretsShim = Join-Path $rootDir '.venv\Scripts\git_secrets_shim.py'

if ((Test-Path $python -PathType Leaf) -and (Test-Path $gitSecretsShim -PathType Leaf)) {
    & $python $gitSecretsShim --pre_commit_hook
    if ($LASTEXITCODE -ne 0) {
        Write-Host 'git-secrets found potential secrets.'
        $status = 1
    }
} else {
    Write-Host 'git-secrets is not available; skipping secret scan.'
}

if (Test-Path $bandit -PathType Leaf) {
    & $bandit -r (Join-Path $rootDir 'src') -ll -q -f json -o (Join-Path $reportsDir 'bandit_report.json')
    if ($LASTEXITCODE -ne 0) {
        Write-Host 'Bandit found security issues.'
        $status = 1
    }
} else {
    Write-Host 'bandit is not available; skipping SAST scan.'
}

if (Test-Path $pipAudit -PathType Leaf) {
    & $pipAudit --desc on -f json -o (Join-Path $reportsDir 'pip_audit_report.json')
    if ($LASTEXITCODE -ne 0) {
        Write-Host 'pip-audit found vulnerable dependencies.'
        $status = 1
    }
} else {
    Write-Host 'pip-audit is not available; skipping dependency scan.'
}

if ($status -eq 0) {
    Write-Host 'All security checks passed.'
}

exit $status
