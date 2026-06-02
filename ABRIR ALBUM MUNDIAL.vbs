'-----------------------------------------------------------------
'  ALBUM MUNDIAL 2026 — Iniciador silencioso
'  Doble click para abrir el album en el navegador
'-----------------------------------------------------------------

Set oShell = CreateObject("WScript.Shell")
Set oFSO   = CreateObject("Scripting.FileSystemObject")

' Carpeta donde esta este archivo
strDir = oFSO.GetParentFolderName(WScript.ScriptFullName)

' Rutas
strPython  = strDir & "\venv\Scripts\python.exe"
strUvicorn = strDir & "\venv\Scripts\uvicorn.exe"
strSeed    = strDir & "\scripts\seed_full.py"

' --- Verificar si el servidor ya esta corriendo ---
Dim oHTTP
Set oHTTP = CreateObject("MSXML2.XMLHTTP")
Dim bRunning
bRunning = False
On Error Resume Next
oHTTP.Open "GET", "http://127.0.0.1:8000/health", False
oHTTP.Send
If oHTTP.Status = 200 Then bRunning = True
On Error GoTo 0

If bRunning Then
    ' Ya estaba corriendo, solo abrimos el navegador
    oShell.Run "http://127.0.0.1:8000"
    WScript.Quit
End If

' --- Correr seed si la base de datos no existe o esta vacia ---
Dim strDB
strDB = strDir & "\album.db"
If Not oFSO.FileExists(strDB) Then
    oShell.Run """" & strPython & """ """ & strSeed & """", 0, True
End If

' --- Iniciar el servidor (oculto, sin ventana) ---
Dim strCmd
strCmd = "cmd /c cd /d """ & strDir & """ && """ & strUvicorn & """ app.main:app --host 127.0.0.1 --port 8000"
oShell.Run strCmd, 0, False

' --- Esperar hasta que el servidor responda (max 15 segundos) ---
Dim i
For i = 1 To 15
    WScript.Sleep 1000
    On Error Resume Next
    Set oHTTP = CreateObject("MSXML2.XMLHTTP")
    oHTTP.Open "GET", "http://127.0.0.1:8000/health", False
    oHTTP.Send
    If oHTTP.Status = 200 Then
        bRunning = True
        Exit For
    End If
    On Error GoTo 0
Next

If Not bRunning Then
    MsgBox "No se pudo iniciar el servidor." & vbCrLf & _
           "Asegurate de que el proyecto este en la carpeta correcta.", _
           vbCritical, "Album Mundial 2026"
    WScript.Quit
End If

' --- Abrir el navegador ---
oShell.Run "http://127.0.0.1:8000"

WScript.Quit
