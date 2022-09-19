pip install -r requirements.txt
@REM modified from https://stackoverflow.com/questions/68360112/a-script-to-start-backend-and-frontend-at-the-same-time
start cmd.exe /C "cd website/backend && python app.py"
timeout 5
start cmd.exe /C "cd website/frontend && npm start"