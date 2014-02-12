cd $1
echo 'Pulling code from remote...'
git pull origin
service uwsgi restart
service nginx restart
