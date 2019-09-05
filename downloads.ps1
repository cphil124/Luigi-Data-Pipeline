# Three different methods for downloading a file using Powershell. For the purposes of this particular project, 
# I'll also be handling things like extracting archives and deleting the archive afterwards
# To use, just uncomment one of the 'Method #' code blocks

$url = "http://plainpixels.work/resources/datasets/dataset_v1.zip"
$output = "$PSScriptRoot\dataset\dataset_v1.zip"
$destdir = "$PSScriptRoot\dataset"
$start_time = Get-Date


# Method 1: Invoke-WebRequest

# Invoke-WebRequest -Uri $url -OutFile $output


# Method 2: System.NET.WebClient

# # $wc = New-Object System.Net.WebClient
# # $wc.DownloadFile($url, $output)
# # OR 
# (New-Object System.Net.WebClient).DownloadFile($url, $output)


# Method 3: Start-BitsTransfer

Import-Module BitsTransfer
Start-BitsTransfer -Source $url -Destination $output


# Final Universal cmdlets

Expand-Archive -Path $output -DestinationPath $destdir
Remove-Item -Path $output
Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) seconds"

Get-ChildItem *.DS_Store -Recurse | ForEach-Object {Remove-Item -Path $_.FullName }
Remove-Item -Path '.\dataset\__MACOSX' -Recurse




$TestDir = "$PSScriptRoot\dataset\Test"
cd $TestDir
Get-ChildItem
cd ..\..

