
REM Format and build photo_book, and process with ghp-import

REM Run in VSCode terminal with below
REM cmd.exe /c "build_photo_book.bat"

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Call venv executables explicitly so the global Python's jb.exe
REM (which lacks sphinxcontrib.mermaid) is never used by mistake.
.venv\Scripts\jb.exe build photo_book
if errorlevel 1 (
    echo.
    echo Build failed - aborting before publish and commit.
    exit /b 1
)

REM ghp-import automatically pushes to gh-pages branch
.venv\Scripts\ghp-import.exe -n -p -f photo_book/_build/html

REM Commit and push source files from main branch
git add .
git commit -m "updates"
git push origin main

cmd /k
