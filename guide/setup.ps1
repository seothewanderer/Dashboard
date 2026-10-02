# 집(새 PC) 개발 환경 한 번에 준비하기 — 2026-10-02
# 실행: main 폴더에서  powershell -ExecutionPolicy Bypass -File guide\setup.ps1
#   -CopyClaude  를 붙이면 Claude 메모리와 미리보기 설정(launch.json)도 제자리에 복사한다(이미 있으면 건너뜀).
param([switch]$CopyClaude)

$ErrorActionPreference = "Stop"
$main = Split-Path $PSScriptRoot -Parent          # ...\Dashboard\main
Set-Location $main

Write-Host "1) Python 3.12 확인" -ForegroundColor Cyan
try { $ver = & py -3.12 --version } catch { $ver = $null }
if (-not $ver) {
    Write-Host "   Python 3.12가 없습니다. 먼저 설치하세요:  winget install --id Python.Python.3.12 -e --scope user" -ForegroundColor Yellow
    exit 1
}
Write-Host "   $ver"

Write-Host "2) 가상환경(.venv) 만들기" -ForegroundColor Cyan
if (Test-Path .venv\Scripts\python.exe) { Write-Host "   이미 있음 — 건너뜀" }
else { & py -3.12 -m venv .venv }

Write-Host "3) 패키지 설치(requirements-lock.txt, 버전 고정)" -ForegroundColor Cyan
& .venv\Scripts\python.exe -m pip install --upgrade pip -q
& .venv\Scripts\python.exe -m pip install -r requirements-lock.txt -q

Write-Host "4) 데이터 다시 빌드(clone 하면 파일 날짜가 바뀌어 '원본이 빌드 이후 바뀌었습니다' 안내가 뜨는 것을 막음)" -ForegroundColor Cyan
& .venv\Scripts\python.exe scripts\build_data.py

Write-Host "5) 테스트" -ForegroundColor Cyan
& .venv\Scripts\python.exe -m pytest -q

if ($CopyClaude) {
    Write-Host "6) Claude 메모리·미리보기 설정 복사" -ForegroundColor Cyan
    $mem = Join-Path $env:USERPROFILE ".claude\projects\C--Projects-Dashboard\memory"
    New-Item -ItemType Directory -Force $mem | Out-Null
    Get-ChildItem guide\claude\memory\*.md | ForEach-Object {
        $to = Join-Path $mem $_.Name
        if (Test-Path $to) { Write-Host "   있음, 건너뜀: $($_.Name)" } else { Copy-Item $_.FullName $to; Write-Host "   복사: $($_.Name)" }
    }
    $launchDir = Join-Path (Split-Path $main -Parent) ".claude"
    New-Item -ItemType Directory -Force $launchDir | Out-Null
    $launch = Join-Path $launchDir "launch.json"
    if (Test-Path $launch) { Write-Host "   있음, 건너뜀: launch.json" } else { Copy-Item guide\claude\launch.json $launch; Write-Host "   복사: launch.json" }
    Write-Host "   주의: 메모리 폴더 이름(C--Projects-Dashboard)은 프로젝트 경로에서 나온다. 저장소를 C:\Projects\Dashboard\main 에 받아야 이어진다."
}

Write-Host "완료. 앱 실행:  .\run.ps1   (브라우저 http://localhost:8501)" -ForegroundColor Green
