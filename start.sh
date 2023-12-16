if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi


source .venv/bin/activate
# echo "To exit the virtual environment type 'deactivate' in the shell."

pip3 install -U -r requirements.txt

python3 -m Main

deactivate