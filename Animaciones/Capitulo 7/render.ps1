<#
    Renderiza las ocho escenas del capitulo 7 y las concatena en un
    unico video.

    Uso:
        .\render.ps1              # calidad alta (1080p60), lo normal
        .\render.ps1 -Calidad ql  # borrador rapido (480p15)
        .\render.ps1 -SoloUnir    # no re-renderiza, solo vuelve a unir
#>
param(
    [ValidateSet('ql', 'qm', 'qh', 'qk')]
    [string]$Calidad = 'qh',
    [switch]$SoloUnir
)

# OJO: 'Stop' no sirve aca. Manim escribe su progreso por stderr y
# PowerShell lo interpreta como error fatal del comando nativo. El control
# de errores se hace con $LASTEXITCODE, que es lo correcto para un .exe.
$ErrorActionPreference = 'Continue'
Set-Location $PSScriptRoot

# winget deja las herramientas en el PATH del usuario, pero una consola ya
# abierta no lo ve hasta reiniciarse: se relee a mano
$env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' +
            [Environment]::GetEnvironmentVariable('Path', 'User')

$carpeta = @{ ql = '480p15'; qm = '720p30'; qh = '1080p60'; qk = '2160p60' }[$Calidad]

# el orden define el orden del video final
$escenas = @(
    @{ archivo = 's01_bayes.py';           escena = 'Bayes' },
    @{ archivo = 's02_cdf_pdf.py';         escena = 'CDFyPDF' },
    @{ archivo = 's03_media_varianza.py';  escena = 'MediaYVarianza' },
    @{ archivo = 's04_chebyshev.py';       escena = 'Chebyshev' },
    @{ archivo = 's05_torre.py';           escena = 'EsperanzaIterada' },
    @{ archivo = 's06_conjunta.py';        escena = 'Conjunta' },
    @{ archivo = 's07_correlacion.py';     escena = 'Correlacion' },
    @{ archivo = 's08_vectorial.py';       escena = 'Vectorial' }
)

if (-not $SoloUnir) {
    $log = Join-Path $PSScriptRoot 'render.log'
    if (Test-Path $log) { Remove-Item $log }
    $i = 0
    foreach ($e in $escenas) {
        $i++
        Write-Host ("[{0}/{1}] renderizando {2} ..." -f $i, $escenas.Count, $e.escena) -ForegroundColor Cyan
        # el detalle va al log; en pantalla solo el avance
        & manim "-$Calidad" $e.archivo $e.escena *>> $log
        if ($LASTEXITCODE -ne 0) {
            Write-Host "falló el render de $($e.escena). Últimas líneas de render.log:" -ForegroundColor Red
            Get-Content $log -Tail 25
            exit 1
        }
    }
}

# ---------------------------------------------------------------- concatenar
New-Item -ItemType Directory -Force -Path 'salida' | Out-Null

$lineas = @()
foreach ($e in $escenas) {
    $base = [IO.Path]::GetFileNameWithoutExtension($e.archivo)
    $mp4 = Join-Path $PSScriptRoot "media\videos\$base\$carpeta\$($e.escena).mp4"
    if (-not (Test-Path $mp4)) {
        Write-Host "falta el video de $($e.escena) en calidad $carpeta. Corré sin -SoloUnir." -ForegroundColor Red
        exit 1
    }
    # el demuxer concat pide comillas simples y separador /
    $lineas += "file '" + ($mp4 -replace '\\', '/') + "'"
}
$lineas | Set-Content -Path 'lista.txt' -Encoding ascii

$final = "salida\Capitulo7-completo-$carpeta.mp4"
Write-Host "uniendo las $($escenas.Count) escenas ..." -ForegroundColor Cyan
& ffmpeg -v error -y -f concat -safe 0 -i lista.txt -c copy $final
if ($LASTEXITCODE -ne 0) {
    Write-Host "falló la concatenación" -ForegroundColor Red
    exit 1
}

$dur = [double](ffprobe -v error -show_entries format=duration -of csv=p=0 $final)
$mb = [math]::Round((Get-Item $final).Length / 1MB, 1)
Write-Host ""
Write-Host "listo: $final" -ForegroundColor Green
Write-Host ("duración {0:N0}:{1:00} min   ·   {2} MB" -f [math]::Floor($dur / 60), ($dur % 60), $mb)
Write-Host ""
Write-Host "para verlo:" -ForegroundColor Yellow
Write-Host "    Invoke-Item `"$(Join-Path $PSScriptRoot $final)`""
