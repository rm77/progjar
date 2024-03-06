sudo chmod -R a+rwx /home/jovyan

PASSWORD=$(echo $PASSWORD | sha1sum | cut -d" " -f1)
start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''  --NotebookApp.ip='0.0.0.0' --Notebook.autoreload=True --NotebookApp.notebook_dir=/home/jovyan/work --allow-root
