$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$allureBat = Join-Path $repo 'allure\allure-2.29.0\bin\allure.bat'
$resultsDir = Join-Path $repo 'allure-results'
$reportDir = Join-Path $repo 'allure-report'

if (-not (Test-Path $allureBat)) {
    throw "Allure CLI not found at $allureBat"
}

if (Test-Path $reportDir) {
    Remove-Item $reportDir -Recurse -Force
}

& $allureBat generate $resultsDir -o $reportDir --clean
Write-Host "Allure report generated at $reportDir"
