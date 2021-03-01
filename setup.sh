mkdir -p ~/.streamlit/
echo "[general]
email = \"sae49@mail.aub.edu\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
