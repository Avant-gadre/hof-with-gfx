@echo off
setlocal enabledelayedexpansion

for %%F in (goal_*) do (
    set "filename=%%F"
    set "filename=%%F"
    set "newname=%%F"
    set "newname=!newname:goal_=!"
    ren "%%F" "focus_!newname!"
)

echo 文件重命名已完成。按任意键继续...
pause >nul