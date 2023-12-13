if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    source .venv/bin/activate
    echo "To exit the virtual environment type 'deactivate' in the shell."
fi

pip3 install -U -r requirements.txt

python3 -m Main