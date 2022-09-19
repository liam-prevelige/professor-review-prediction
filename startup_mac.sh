#!/bin/sh
pip install -r requirements.txt
# debugged using https://stackoverflow.com/questions/62140265/npm-run-build-react-scripts-permission-denied
/bin/sh -ec 'cd website/frontend && npm install react-scripts --save && sudo chmod +x node_modules/.bin/react-scripts'
/bin/sh -ec 'cd website/backend && python app.py &'
sleep 5
/bin/sh -ec 'cd website/frontend && npm start'