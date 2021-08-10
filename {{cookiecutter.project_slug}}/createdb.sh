# Creates an instance of the database for this Django project
# Set ${POSTGRES_USER} in your path
createdb {{ cookiecutter.project_slug }} -U ${POSTGRES_USER} --password ${POSTGRES_PASSWD}
