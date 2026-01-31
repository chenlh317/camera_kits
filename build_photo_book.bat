
REM Format and build photo_book, and process with ghp-import

REM Run in VSCode terminal with below
REM cmd.exe -/c "build_photo_book.bat"

REM Activate virtual environment
call .venv\Scripts\activate.bat

jb build photo_book

REM ghp-import automatically pushes to gh-pages branch
ghp-import -n -p -f photo_book/_build/html

REM Commit and push source files from main branch
git add .
git commit -m "updates"
git push origin main

cmd /k
