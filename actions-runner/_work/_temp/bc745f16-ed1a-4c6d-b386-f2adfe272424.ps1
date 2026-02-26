$ErrorActionPreference = 'stop'
docker build -t $IMAGE_NAME:latest .
docker tag $IMAGE_NAME:latest $IMAGE_NAME:070ba07ad9f86988385397e45a08826c41122941

if ((Test-Path -LiteralPath variable:\LASTEXITCODE)) { exit $LASTEXITCODE }