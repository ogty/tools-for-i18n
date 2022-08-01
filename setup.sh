pip3 install -r requirements.txt
currentDirectory=$(cd $(dirname $0);pwd)
echo 'export PATH="$PATH:'$currentDirectory\" >> ~/.zshrc
source ~/.zshrc
sudo chmod 755 $currentDirectory/i18nseg
