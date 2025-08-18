# PowerShell Complete Guide

A comprehensive guide to mastering PowerShell, Microsoft's powerful command-line shell and scripting language for Windows, Linux, and macOS. Covers essential concepts, cmdlets, scripting, automation, system administration, and advanced techniques.

## Table of Contents

1. [Introduction to PowerShell](#introduction-to-powershell)
2. [PowerShell Fundamentals](#powershell-fundamentals)
3. [File and Directory Management](#file-and-directory-management)
4. [Text Processing and Manipulation](#text-processing-and-manipulation)
5. [System Information and Management](#system-information-and-management)
6. [User and Group Management](#user-and-group-management)
7. [Network Operations](#network-operations)
8. [Process and Service Management](#process-and-service-management)
9. [Registry and Configuration Management](#registry-and-configuration-management)
10. [PowerShell Scripting](#powershell-scripting)
11. [Advanced PowerShell Techniques](#advanced-powershell-techniques)
12. [Security and Execution Policy](#security-and-execution-policy)
13. [Remote Management](#remote-management)
14. [Troubleshooting and Debugging](#troubleshooting-and-debugging)
15. [Best Practices and Tips](#best-practices-and-tips)

---

## Introduction to PowerShell

### What is PowerShell?

PowerShell is Microsoft's task automation and configuration management framework, consisting of a command-line shell and associated scripting language. It was designed to replace Command Prompt and provide a more powerful, object-oriented approach to system administration.

#### Key Features

- **Object-oriented**: Commands return .NET objects, not just text
- **Cross-platform**: Available on Windows, Linux, and macOS
- **Extensible**: Supports custom cmdlets and modules
- **Integrated**: Deep integration with Windows systems
- **Secure**: Built-in security features and execution policies

#### PowerShell Versions

| Version | Release Date | Key Features |
|---------|-------------|--------------|
| PowerShell 1.0 | 2006 | Basic cmdlets, snap-ins |
| PowerShell 2.0 | 2009 | Remoting, advanced functions |
| PowerShell 3.0 | 2012 | Workflows, scheduled jobs |
| PowerShell 4.0 | 2013 | Desired State Configuration |
| PowerShell 5.0 | 2016 | Classes, DSC improvements |
| PowerShell 6.0+ | 2018+ | Cross-platform, .NET Core |
| PowerShell 7.0+ | 2020+ | Modern .NET, performance |

### Accessing PowerShell

#### Windows

```powershell
# Start PowerShell from Start Menu
# Search for "PowerShell" and click "Windows PowerShell"

# From Command Prompt
cmd> powershell

# From Run dialog (Win+R)
powershell

# Start as Administrator
# Right-click PowerShell and select "Run as administrator"
```

#### Linux/macOS

```bash
# Install PowerShell Core
# Ubuntu/Debian
sudo apt-get install powershell

# CentOS/RHEL
sudo yum install powershell

# macOS (using Homebrew)
brew install powershell

# Start PowerShell
pwsh
```

#### PowerShell ISE (Integrated Scripting Environment)

```powershell
# Launch PowerShell ISE
powershell_ise

# Or from Start Menu
# Search for "PowerShell ISE"
```

### Basic PowerShell Environment

#### PowerShell Prompt

```powershell
PS C:\Users\username>    # Windows
PS /home/username>       # Linux/macOS
```

#### Getting Help

```powershell
# Get help for a cmdlet
Get-Help Get-Process

# Get help with examples
Get-Help Get-Process -Examples

# Get detailed help
Get-Help Get-Process -Detailed

# Get full help
Get-Help Get-Process -Full

# Search for cmdlets
Get-Help *process*

# Get help about topics
Get-Help about_*
```

#### Command Discovery

```powershell
# List all available cmdlets
Get-Command

# List cmdlets with specific verb
Get-Command -Verb Get

# List cmdlets with specific noun
Get-Command -Noun Process

# List commands in a module
Get-Command -Module Microsoft.PowerShell.Management
```

---

## PowerShell Fundamentals

### Cmdlet Structure

PowerShell cmdlets follow a **Verb-Noun** naming convention:

```powershell
Verb-Noun [-Parameter] [Value]
```

#### Common Verbs

| Verb | Purpose | Examples |
|------|---------|----------|
| Get | Retrieve data | Get-Process, Get-Service |
| Set | Configure settings | Set-Location, Set-ExecutionPolicy |
| New | Create objects | New-Item, New-Object |
| Remove | Delete objects | Remove-Item, Remove-Process |
| Start | Begin operations | Start-Process, Start-Service |
| Stop | End operations | Stop-Process, Stop-Service |
| Test | Validate conditions | Test-Path, Test-Connection |
| Import | Load data | Import-Csv, Import-Module |
| Export | Save data | Export-Csv, Export-Clixml |

### Parameters and Arguments

#### Parameter Types

```powershell
# Positional parameters
Get-Process notepad

# Named parameters
Get-Process -Name notepad

# Switch parameters (true/false)
Get-Process -IncludeUserName

# Parameter sets
Get-Process -Id 1234
Get-Process -Name "notepad*"
```

#### Parameter Aliases

```powershell
# Common aliases
ls                    # Get-ChildItem
dir                   # Get-ChildItem
cd                    # Set-Location
pwd                   # Get-Location
cat                   # Get-Content
echo                  # Write-Output
cls                   # Clear-Host
```

### Variables and Data Types

#### Variable Declaration

```powershell
# Simple variable assignment
$name = "John"
$age = 30
$isActive = $true

# Strongly typed variables
[string]$name = "John"
[int]$age = 30
[bool]$isActive = $true

# Array variables
$numbers = @(1, 2, 3, 4, 5)
$names = @("Alice", "Bob", "Charlie")

# Hash table
$person = @{
    Name = "John"
    Age = 30
    City = "New York"
}
```

#### Special Variables

```powershell
$PSVersionTable        # PowerShell version information
$PWD                   # Current working directory
$HOME                  # User's home directory
$env:USERNAME          # Environment variable
$null                  # Null value
$true, $false          # Boolean values
$PSDefaultParameterValues  # Default parameter values
```

### Pipeline and Object Flow

#### Basic Pipeline

```powershell
# Pass objects from one cmdlet to another
Get-Process | Where-Object {$_.CPU -gt 10}

# Multiple pipeline stages
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

#### Pipeline Examples

```powershell
# Get processes using more than 100MB memory
Get-Process | Where-Object {$_.WorkingSet -gt 100MB}

# Get services and sort by status
Get-Service | Sort-Object Status

# Get files and filter by extension
Get-ChildItem | Where-Object {$_.Extension -eq ".txt"}
```

---

## File and Directory Management

### Navigation Commands

#### Basic Navigation

```powershell
# Get current location
Get-Location
pwd

# Change directory
Set-Location C:\Windows
cd C:\Windows

# Navigate to home directory
Set-Location ~
cd ~

# Navigate to parent directory
Set-Location ..
cd ..

# Navigate to specific path
Set-Location "C:\Program Files"
cd "C:\Program Files"
```

#### Path Management

```powershell
# Join paths
Join-Path "C:\Users" "Documents"

# Split path
Split-Path "C:\Users\John\Documents\file.txt"

# Get path components
Split-Path "C:\Users\John\Documents\file.txt" -Parent
Split-Path "C:\Users\John\Documents\file.txt" -Leaf
```

### File and Directory Operations

#### Listing Files and Directories

```powershell
# List items in current directory
Get-ChildItem
ls
dir

# List with details
Get-ChildItem -Force

# List specific items
Get-ChildItem *.txt
Get-ChildItem -Recurse

# List with formatting
Get-ChildItem | Format-Table Name, Length, LastWriteTime
```

#### Creating Files and Directories

```powershell
# Create directory
New-Item -ItemType Directory -Path "C:\NewFolder"
mkdir "C:\NewFolder"

# Create file
New-Item -ItemType File -Path "C:\NewFolder\test.txt"
ni "C:\NewFolder\test.txt"

# Create with content
"Hello World" | Out-File "C:\NewFolder\test.txt"
Set-Content "C:\NewFolder\test.txt" "Hello World"
```

#### Copying and Moving

```powershell
# Copy file
Copy-Item "source.txt" "destination.txt"
cp "source.txt" "destination.txt"

# Copy directory
Copy-Item "C:\SourceFolder" "C:\DestFolder" -Recurse

# Move file
Move-Item "source.txt" "destination.txt"
mv "source.txt" "destination.txt"

# Rename file
Rename-Item "oldname.txt" "newname.txt"
ren "oldname.txt" "newname.txt"
```

#### Deleting Files and Directories

```powershell
# Delete file
Remove-Item "file.txt"
del "file.txt"

# Delete directory
Remove-Item "C:\FolderToDelete" -Recurse

# Force delete (bypass confirmation)
Remove-Item "file.txt" -Force

# Delete with confirmation
Remove-Item "file.txt" -Confirm
```

### File Properties and Attributes

#### Getting File Information

```powershell
# Get file properties
Get-ItemProperty "file.txt"

# Get file attributes
(Get-Item "file.txt").Attributes

# Check if file exists
Test-Path "file.txt"

# Get file size
(Get-Item "file.txt").Length
```

#### Setting File Attributes

```powershell
# Set file as read-only
Set-ItemProperty "file.txt" -Name IsReadOnly -Value $true

# Set file as hidden
$file = Get-Item "file.txt"
$file.Attributes = $file.Attributes -bor [System.IO.FileAttributes]::Hidden

# Remove read-only attribute
Set-ItemProperty "file.txt" -Name IsReadOnly -Value $false
```

### File Content Operations

#### Reading Files

```powershell
# Read entire file
Get-Content "file.txt"

# Read specific lines
Get-Content "file.txt" -TotalCount 10
Get-Content "file.txt" | Select-Object -First 10

# Read file as single string
Get-Content "file.txt" -Raw

# Read file with encoding
Get-Content "file.txt" -Encoding UTF8
```

#### Writing to Files

```powershell
# Write content to file
Set-Content "file.txt" "Hello World"

# Append content to file
Add-Content "file.txt" "New line"

# Write with encoding
Set-Content "file.txt" "Hello World" -Encoding UTF8

# Write multiple lines
@("Line 1", "Line 2", "Line 3") | Set-Content "file.txt"
```

---

## Text Processing and Manipulation

### String Operations

#### Basic String Manipulation

```powershell
# String concatenation
$firstName = "John"
$lastName = "Doe"
$fullName = $firstName + " " + $lastName

# String interpolation
$fullName = "$firstName $lastName"

# String length
$text = "Hello World"
$text.Length

# Substring
$text.Substring(0, 5)  # "Hello"
$text.Substring(6)     # "World"
```

#### String Methods

```powershell
# Convert case
$text = "Hello World"
$text.ToUpper()        # "HELLO WORLD"
$text.ToLower()        # "hello world"

# Replace text
$text.Replace("World", "PowerShell")

# Split string
$text.Split(" ")

# Trim whitespace
$text.Trim()
$text.TrimStart()
$text.TrimEnd()
```

### Text Processing Cmdlets

#### Select-String (grep equivalent)

```powershell
# Search for text in files
Select-String "pattern" "file.txt"

# Search in multiple files
Select-String "pattern" *.txt

# Case-insensitive search
Select-String "pattern" "file.txt" -CaseSensitive

# Search with context
Select-String "pattern" "file.txt" -Context 2

# Search with regex
Select-String "pattern" "file.txt" -AllMatches
```

#### ForEach-Object

```powershell
# Process each line
Get-Content "file.txt" | ForEach-Object { $_.ToUpper() }

# Process with index
Get-Content "file.txt" | ForEach-Object { "$($_.ReadCount): $_" }

# Process objects
Get-Process | ForEach-Object { $_.ProcessName + " - " + $_.CPU }
```

### Regular Expressions

#### Basic Regex

```powershell
# Match pattern
"Hello World" -match "World"

# Replace with regex
"Hello World" -replace "World", "PowerShell"

# Extract matches
if ("Hello World" -match "(\w+) (\w+)") {
    $matches[1]  # "Hello"
    $matches[2]  # "World"
}
```

#### Advanced Regex Examples

```powershell
# Email validation
$email = "user@example.com"
$email -match "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Phone number extraction
$text = "Call me at 555-123-4567 or 555-987-6543"
$text -match "\d{3}-\d{3}-\d{4}"

# Multiple matches
[regex]::Matches($text, "\d{3}-\d{3}-\d{4}") | ForEach-Object { $_.Value }
```

---

## System Information and Management

### System Information

#### Basic System Info

```powershell
# Get computer name
$env:COMPUTERNAME
hostname

# Get OS information
Get-ComputerInfo
Get-CimInstance Win32_OperatingSystem

# Get PowerShell version
$PSVersionTable

# Get .NET version
[System.Environment]::Version
```

#### Detailed System Information

```powershell
# Get system properties
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, TotalPhysicalMemory

# Get processor information
Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors

# Get disk information
Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID, Size, FreeSpace

# Get network adapters
Get-NetAdapter | Where-Object {$_.Status -eq "Up"}
```

### Environment Variables

#### Working with Environment Variables

```powershell
# Get all environment variables
Get-ChildItem Env:

# Get specific environment variable
$env:PATH
$env:USERNAME
$env:COMPUTERNAME

# Set environment variable (session only)
$env:MY_VAR = "value"

# Set environment variable permanently
[Environment]::SetEnvironmentVariable("MY_VAR", "value", "User")

# Remove environment variable
Remove-Item Env:MY_VAR
```

### Date and Time Operations

#### Date/Time Commands

```powershell
# Get current date and time
Get-Date
(Get-Date).ToString()

# Format date
Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Date arithmetic
(Get-Date).AddDays(7)
(Get-Date).AddHours(-2)

# Parse date string
[DateTime]::Parse("2023-12-25")
```

---

## User and Group Management

### User Management

#### Get User Information

```powershell
# Get current user
$env:USERNAME
[System.Security.Principal.WindowsIdentity]::GetCurrent().Name

# Get all local users
Get-LocalUser

# Get specific user
Get-LocalUser -Name "Administrator"

# Get user details
Get-LocalUser | Select-Object Name, Enabled, LastLogon, PasswordLastSet
```

#### User Operations

```powershell
# Create new user
New-LocalUser -Name "NewUser" -Description "Test User"

# Set user password
Set-LocalUser -Name "NewUser" -Password (ConvertTo-SecureString "Password123" -AsPlainText -Force)

# Enable/disable user
Enable-LocalUser -Name "NewUser"
Disable-LocalUser -Name "NewUser"

# Remove user
Remove-LocalUser -Name "NewUser"
```

### Group Management

#### Group Operations

```powershell
# Get all local groups
Get-LocalGroup

# Get group members
Get-LocalGroupMember -Group "Administrators"

# Add user to group
Add-LocalGroupMember -Group "Administrators" -Member "NewUser"

# Remove user from group
Remove-LocalGroupMember -Group "Administrators" -Member "NewUser"

# Create new group
New-LocalGroup -Name "TestGroup" -Description "Test Group"
```

### Active Directory (if available)

```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Get AD users
Get-ADUser -Filter *

# Get specific AD user
Get-ADUser -Identity "username"

# Get AD groups
Get-ADGroup -Filter *

# Add user to AD group
Add-ADGroupMember -Identity "GroupName" -Members "username"
```

---

## Network Operations

### Network Information

#### Basic Network Commands

```powershell
# Get IP configuration
Get-NetIPConfiguration
ipconfig

# Get network adapters
Get-NetAdapter

# Get DNS servers
Get-DnsClientServerAddress

# Test connectivity
Test-Connection "google.com"
ping "google.com"
```

#### Advanced Network Operations

```powershell
# Get network connections
Get-NetTCPConnection

# Get listening ports
Get-NetTCPConnection -State Listen

# Test specific port
Test-NetConnection -ComputerName "server" -Port 80

# Get network statistics
Get-NetStatistics
```

### Web Operations

#### Invoke-WebRequest

```powershell
# Download web page
$response = Invoke-WebRequest -Uri "https://example.com"

# Get content
$response.Content

# Download file
Invoke-WebRequest -Uri "https://example.com/file.zip" -OutFile "file.zip"

# POST request
$body = @{param1="value1"; param2="value2"}
Invoke-WebRequest -Uri "https://api.example.com" -Method POST -Body $body
```

#### Web Client

```powershell
# Download file
$webClient = New-Object System.Net.WebClient
$webClient.DownloadFile("https://example.com/file.zip", "file.zip")

# Download string
$content = $webClient.DownloadString("https://example.com")
```

---

## Process and Service Management

### Process Management

#### Process Commands

```powershell
# Get all processes
Get-Process

# Get specific process
Get-Process -Name "notepad"

# Get process by ID
Get-Process -Id 1234

# Get processes with details
Get-Process | Select-Object Name, Id, CPU, WorkingSet, ProcessName
```

#### Process Control

```powershell
# Start process
Start-Process "notepad.exe"

# Start process with arguments
Start-Process "notepad.exe" -ArgumentList "file.txt"

# Stop process
Stop-Process -Name "notepad"

# Stop process by ID
Stop-Process -Id 1234

# Kill process (force)
Stop-Process -Name "notepad" -Force
```

### Service Management

#### Service Commands

```powershell
# Get all services
Get-Service

# Get specific service
Get-Service -Name "Spooler"

# Get running services
Get-Service | Where-Object {$_.Status -eq "Running"}

# Get stopped services
Get-Service | Where-Object {$_.Status -eq "Stopped"}
```

#### Service Control

```powershell
# Start service
Start-Service -Name "Spooler"

# Stop service
Stop-Service -Name "Spooler"

# Restart service
Restart-Service -Name "Spooler"

# Set service startup type
Set-Service -Name "Spooler" -StartupType Automatic
```

---

## Registry and Configuration Management

### Registry Operations

#### Registry Navigation

```powershell
# Navigate registry
Set-Location "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion"

# Get registry keys
Get-ChildItem "HKLM:\SOFTWARE\Microsoft"

# Get registry values
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion"
```

#### Registry Modifications

```powershell
# Create registry key
New-Item -Path "HKLM:\SOFTWARE\MyApp" -Force

# Set registry value
Set-ItemProperty -Path "HKLM:\SOFTWARE\MyApp" -Name "Version" -Value "1.0"

# Get registry value
Get-ItemProperty -Path "HKLM:\SOFTWARE\MyApp" -Name "Version"

# Remove registry value
Remove-ItemProperty -Path "HKLM:\SOFTWARE\MyApp" -Name "Version"

# Remove registry key
Remove-Item -Path "HKLM:\SOFTWARE\MyApp" -Recurse
```

### Configuration Files

#### Working with Configuration Files

```powershell
# Read INI file
Get-Content "config.ini"

# Read JSON file
Get-Content "config.json" | ConvertFrom-Json

# Read XML file
[xml]$xml = Get-Content "config.xml"

# Write JSON file
$config = @{
    Server = "localhost"
    Port = 8080
    Enabled = $true
}
$config | ConvertTo-Json | Set-Content "config.json"
```

---

## PowerShell Scripting

### Basic Scripting

#### Script Structure

```powershell
# Script header
<#
.SYNOPSIS
    Brief description of the script
.DESCRIPTION
    Detailed description of the script
.PARAMETER ParameterName
    Description of the parameter
.EXAMPLE
    Example usage
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$ParameterName
)

# Script body
Write-Host "Hello, $ParameterName!"

# Error handling
try {
    # Code that might fail
}
catch {
    Write-Error "An error occurred: $($_.Exception.Message)"
}
```

#### Functions

```powershell
# Basic function
function Get-Greeting {
    param([string]$Name)
    return "Hello, $Name!"
}

# Advanced function
function Get-SystemInfo {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$ComputerName,
        
        [switch]$Detailed
    )
    
    begin {
        Write-Verbose "Starting system information collection"
    }
    
    process {
        $info = Get-ComputerInfo -ComputerName $ComputerName
        
        if ($Detailed) {
            $info
        } else {
            $info | Select-Object WindowsProductName, TotalPhysicalMemory
        }
    }
    
    end {
        Write-Verbose "System information collection completed"
    }
}
```

### Control Structures

#### Conditional Statements

```powershell
# If statement
if ($condition) {
    # Code
} elseif ($otherCondition) {
    # Code
} else {
    # Code
}

# Switch statement
switch ($value) {
    "value1" { Write-Host "Value 1" }
    "value2" { Write-Host "Value 2" }
    default { Write-Host "Default" }
}
```

#### Loops

```powershell
# For loop
for ($i = 0; $i -lt 10; $i++) {
    Write-Host $i
}

# ForEach loop
foreach ($item in $collection) {
    Write-Host $item
}

# While loop
while ($condition) {
    # Code
}

# Do-While loop
do {
    # Code
} while ($condition)
```

### Error Handling

#### Try-Catch Blocks

```powershell
try {
    # Code that might fail
    Get-Process -Name "NonExistentProcess"
}
catch {
    Write-Error "Process not found: $($_.Exception.Message)"
}
finally {
    # Code that always runs
    Write-Host "Cleanup completed"
}
```

#### Error Action Preferences

```powershell
# Set error action preference
$ErrorActionPreference = "Stop"

# Continue on error
Get-Process -Name "NonExistentProcess" -ErrorAction Continue

# Silently continue
Get-Process -Name "NonExistentProcess" -ErrorAction SilentlyContinue

# Inquire (ask user)
Get-Process -Name "NonExistentProcess" -ErrorAction Inquire
```

---

## Advanced PowerShell Techniques

### Modules and Snap-ins

#### Working with Modules

```powershell
# List available modules
Get-Module -ListAvailable

# Import module
Import-Module ActiveDirectory

# Get module commands
Get-Command -Module ActiveDirectory

# Remove module
Remove-Module ActiveDirectory
```

#### Creating Custom Modules

```powershell
# Module manifest
New-ModuleManifest -Path "MyModule.psd1" -Author "Your Name" -Description "My custom module"

# Module structure
MyModule/
├── MyModule.psd1
├── MyModule.psm1
└── Functions/
    └── Get-MyFunction.ps1
```

### Remoting and Jobs

#### PowerShell Remoting

```powershell
# Enable remoting (run as administrator)
Enable-PSRemoting -Force

# Create session
$session = New-PSSession -ComputerName "RemoteServer"

# Execute command remotely
Invoke-Command -Session $session -ScriptBlock { Get-Process }

# Remove session
Remove-PSSession $session
```

#### Background Jobs

```powershell
# Start background job
$job = Start-Job -ScriptBlock { Get-Process }

# Get job status
Get-Job

# Receive job results
Receive-Job $job

# Wait for job completion
Wait-Job $job

# Remove job
Remove-Job $job
```

### Desired State Configuration (DSC)

#### Basic DSC Configuration

```powershell
Configuration WebServer {
    param(
        [string]$NodeName = "localhost"
    )
    
    Node $NodeName {
        WindowsFeature IIS {
            Ensure = "Present"
            Name = "Web-Server"
        }
        
        File WebsiteContent {
            Ensure = "Present"
            SourcePath = "\\server\share\website"
            DestinationPath = "C:\inetpub\wwwroot"
            DependsOn = "[WindowsFeature]IIS"
        }
    }
}

# Compile configuration
WebServer -NodeName "WebServer01"

# Apply configuration
Start-DscConfiguration -Path ".\WebServer" -Wait -Verbose
```

---

## Security and Execution Policy

### Execution Policy

#### Understanding Execution Policies

```powershell
# Get current execution policy
Get-ExecutionPolicy

# Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Execution policy levels
# - Restricted: No scripts allowed
# - AllSigned: Only signed scripts
# - RemoteSigned: Local scripts + signed remote scripts
# - Unrestricted: All scripts allowed
# - Bypass: No restrictions
```

#### Bypassing Execution Policy

```powershell
# Bypass for single command
PowerShell -ExecutionPolicy Bypass -Command "Get-Process"

# Bypass for script
PowerShell -ExecutionPolicy Bypass -File "script.ps1"

# Bypass for session
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

### Script Signing

#### Signing Scripts

```powershell
# Create self-signed certificate
New-SelfSignedCertificate -Subject "CN=PowerShell Scripts" -CertStoreLocation "Cert:\CurrentUser\My"

# Sign script
Set-AuthenticodeSignature -FilePath "script.ps1" -Certificate (Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert)

# Verify signature
Get-AuthenticodeSignature -FilePath "script.ps1"
```

### Security Best Practices

```powershell
# Use constrained language mode
$ExecutionContext.SessionState.LanguageMode = "ConstrainedLanguage"

# Validate input parameters
param(
    [ValidateNotNullOrEmpty()]
    [string]$InputParameter
)

# Use secure strings for passwords
$password = Read-Host "Enter password" -AsSecureString
```

---

## Remote Management

### WinRM Configuration

#### Basic WinRM Setup

```powershell
# Configure WinRM (run as administrator)
winrm quickconfig

# Set WinRM service to auto-start
Set-Service -Name "WinRM" -StartupType Automatic

# Configure WinRM for HTTPS
New-Item -Path WSMan:\localhost\Listener -Address * -Transport HTTPS -Force
```

#### WinRM Security

```powershell
# Configure trusted hosts
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "*" -Force

# Configure authentication
Set-Item WSMan:\localhost\Service\Auth\Basic -Value $true
```

### Remote Commands

#### Invoke-Command

```powershell
# Execute command on remote computer
Invoke-Command -ComputerName "RemoteServer" -ScriptBlock { Get-Process }

# Execute with credentials
$cred = Get-Credential
Invoke-Command -ComputerName "RemoteServer" -Credential $cred -ScriptBlock { Get-Process }

# Execute with parameters
Invoke-Command -ComputerName "RemoteServer" -ScriptBlock { param($name) Get-Process -Name $name } -ArgumentList "notepad"
```

#### Enter-PSSession

```powershell
# Enter interactive session
Enter-PSSession -ComputerName "RemoteServer"

# Exit session
Exit-PSSession
```

### Remote File Operations

```powershell
# Copy file to remote computer
Copy-Item "local.txt" -Destination "\\RemoteServer\C$\temp\remote.txt"

# Copy from remote computer
Copy-Item "\\RemoteServer\C$\temp\remote.txt" -Destination "local.txt"

# Use PSSession for file operations
$session = New-PSSession -ComputerName "RemoteServer"
Copy-Item "local.txt" -Destination "C:\temp\remote.txt" -ToSession $session
```

---

## Troubleshooting and Debugging

### Debugging Techniques

#### Write-Debug and Debugging

```powershell
# Enable debug output
$DebugPreference = "Continue"

# Debug statements
Write-Debug "Debug information"

# Step through script
Set-PSBreakpoint -Script "script.ps1" -Line 10
```

#### Verbose Output

```powershell
# Enable verbose output
$VerbosePreference = "Continue"

# Verbose statements
Write-Verbose "Verbose information"

# Use -Verbose parameter
Get-Process -Verbose
```

### Error Investigation

#### Error Handling

```powershell
# Get last error
$Error[0]

# Get error details
$Error[0] | Format-List -Force

# Clear error array
$Error.Clear()

# Log errors
try {
    # Code
}
catch {
    Add-Content -Path "error.log" -Value "$(Get-Date): $($_.Exception.Message)"
}
```

#### Performance Monitoring

```powershell
# Measure command execution time
Measure-Command { Get-Process }

# Get detailed timing
$timer = [System.Diagnostics.Stopwatch]::StartNew()
# ... your code ...
$timer.Stop()
Write-Host "Execution time: $($timer.ElapsedMilliseconds) ms"
```

### Common Issues and Solutions

#### Execution Policy Issues

```powershell
# Check execution policy
Get-ExecutionPolicy -List

# Set for current user
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Module Loading Issues

```powershell
# Check module path
$env:PSModulePath

# Add custom module path
$env:PSModulePath += ";C:\MyModules"

# Import module with full path
Import-Module "C:\MyModules\MyModule.psm1"
```

#### Permission Issues

```powershell
# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

# Elevate privileges
Start-Process PowerShell -Verb RunAs
```

---

## Best Practices and Tips

### Scripting Best Practices

#### Code Organization

```powershell
# Use consistent naming conventions
# Verbs: Get, Set, New, Remove, Start, Stop, Test
# Nouns: Process, Service, User, File

# Use parameter validation
param(
    [Parameter(Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string]$ComputerName,
    
    [Parameter()]
    [ValidateRange(1, 100)]
    [int]$Timeout = 30
)

# Use comment-based help
<#
.SYNOPSIS
    Brief description
.DESCRIPTION
    Detailed description
.PARAMETER ParameterName
    Parameter description
.EXAMPLE
    Example usage
#>
```

#### Performance Optimization

```powershell
# Use pipeline efficiently
Get-Process | Where-Object {$_.CPU -gt 10} | Select-Object Name, CPU

# Avoid unnecessary loops
# Instead of:
foreach ($process in Get-Process) {
    if ($process.CPU -gt 10) {
        $process | Select-Object Name, CPU
    }
}

# Use:
Get-Process | Where-Object {$_.CPU -gt 10} | Select-Object Name, CPU
```

### Security Best Practices

#### Secure Scripting

```powershell
# Use secure strings for sensitive data
$password = Read-Host "Enter password" -AsSecureString

# Validate input
if ($input -notmatch "^[a-zA-Z0-9]+$") {
    throw "Invalid input format"
}

# Use constrained language mode when possible
$ExecutionContext.SessionState.LanguageMode = "ConstrainedLanguage"
```

#### Error Handling

```powershell
# Use proper error handling
try {
    # Risky operation
    Remove-Item "important.txt" -Force
}
catch {
    Write-Error "Failed to remove file: $($_.Exception.Message)"
    # Log error or take alternative action
}
```

### Useful Tips and Tricks

#### One-liners

```powershell
# Get top 5 processes by CPU
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5

# Find files modified today
Get-ChildItem | Where-Object {$_.LastWriteTime.Date -eq (Get-Date).Date}

# Get system uptime
(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
```

#### Aliases and Shortcuts

```powershell
# Create custom alias
Set-Alias -Name gps -Value Get-Process

# Create function shortcut
function ll { Get-ChildItem -Force }

# Use profile for customizations
# Edit profile: notepad $PROFILE
```

#### Profile Customization

```powershell
# Check if profile exists
Test-Path $PROFILE

# Create profile
New-Item -ItemType File -Path $PROFILE -Force

# Add customizations to profile
Add-Content $PROFILE 'Set-Alias -Name ll -Value Get-ChildItem'
Add-Content $PROFILE 'function prompt { "PS $($executionContext.SessionState.Path.CurrentLocation)$(''>'' * ($nestedPromptLevel + 1)) " }'
```

---

## Conclusion

PowerShell is a powerful and versatile tool for Windows system administration, automation, and scripting. This guide covers the essential concepts and techniques needed to become proficient with PowerShell.

### Key Takeaways

1. **Object-oriented approach**: PowerShell works with .NET objects, not just text
2. **Consistent naming**: Use Verb-Noun naming convention for cmdlets
3. **Pipeline power**: Chain commands together for powerful data processing
4. **Security first**: Always consider security implications of your scripts
5. **Error handling**: Implement proper error handling in production scripts
6. **Documentation**: Use comment-based help for your functions and scripts

### Next Steps

- Practice with real-world scenarios
- Explore advanced topics like DSC and advanced functions
- Learn about PowerShell Core and cross-platform capabilities
- Join PowerShell communities and forums
- Contribute to open-source PowerShell projects

### Resources

- [Microsoft PowerShell Documentation](https://docs.microsoft.com/en-us/powershell/)
- [PowerShell Gallery](https://www.powershellgallery.com/)
- [PowerShell GitHub Repository](https://github.com/PowerShell/PowerShell)
- [PowerShell Community](https://powershell.org/)

---

*This guide provides a comprehensive foundation for PowerShell usage. Continue exploring and practicing to master this powerful automation and administration tool.*
