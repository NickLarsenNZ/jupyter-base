import os
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8080
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.custom_display_url = 'http://{}:{}'.format(os.environ.get('EXTERNAL_HOST'), os.environ.get('EXTERNAL_PORT'))
c.NotebookApp.notebook_dir = '/data'