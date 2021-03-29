#!/bin/sh

# Decrypt the file
mkdir $HOME/secrets
# --batch to prevent interactive command
# --yes to assume "yes" for questions
#gpg --quiet --batch --yes --decrypt --passphrase="$DIGITALOCEAN_HOST" --output $HOME/secrets/dghost.json dghost.json.gpg
#gpg --quiet --batch --yes --decrypt --passphrase="$DIGITALOCEAN_KEY" --output $HOME/secrets/dgkey.json dgkey.json.gpg
#gpg --quiet --batch --yes --decrypt --passphrase="$DIGITALOCEAN_USER" --output $HOME/secrets/dguser.json dguser.json.gpg

echo $DIGITALOCEAN_HOST > $HOME/secrets/dghost.json
echo $DIGITALOCEAN_KEY > $HOME/secrets/dgkey.json
echo $DIGITALOCEAN_USER > $HOME/secrets/dguser.json

