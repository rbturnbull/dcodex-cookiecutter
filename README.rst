DCodex Cookiecutter Django
===========================


This project can setup a D-Codex site using `Cookiecutter Django`_

.. _Cookiecutter Django: https://cookiecutter-django.readthedocs.io/en/latest/


Usage
------

First, get Cookiecutter_. ::

    $ pip install "cookiecutter>=1.7.0"

.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
    

Now run it against this repo::

    $ cookiecutter https://github.com/rbturnbull/dcodex-cookiecutter

You'll be prompted for some values. Provide them, then a Django project using dcodex will be created for you.

**Warning**: After this point, change 'Robert Turnbull', 'dcodex_family_13', etc to your own information.

Answer the prompts with your own desired options_. For example::

    project_name [My DCodex Project]: DCodex Family 13
    project_slug [dcodex_family_13]: dcodex_f13
    description [A brief description my DCodex project.]: A D-Codex project to display the manuscripts of family 13
    author_name [Robert Turnbull]: Robert Turnbull
    domain_name [example.com]: f13.d-codex.net
    email [robert.turnbull@dcodex.net]: rob@robturnbull.com
    version [0.1.0]:
    Select open_source_license:
    1 - Apache Software License 2.0
    2 - MIT
    3 - BSD
    4 - GPLv3
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]:
    timezone [Australia/Melbourne]:
    windows [n]:
    use_pycharm [n]:
    use_docker [y]:
    Select postgresql_version:
    1 - 12.3
    2 - 11.8
    3 - 10.8
    4 - 9.6
    5 - 9.5
    Choose from 1, 2, 3, 4, 5 [1]:
    Select js_task_runner:
    1 - None
    2 - Gulp
    Choose from 1, 2 [1]:
    Select cloud_provider:
    1 - AWS
    2 - GCP
    3 - None
    Choose from 1, 2, 3 [1]:
    Select mail_service:
    1 - Other SMTP
    2 - Mailgun
    3 - Amazon SES
    4 - Mailjet
    5 - Mandrill
    6 - Postmark
    7 - Sendgrid
    8 - SendinBlue
    9 - SparkPost
    Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9 [1]:
    use_async [n]:
    use_drf [y]:
    custom_bootstrap_compilation [n]:
    use_compressor [y]:
    use_celery [y]:
    use_mailhog [n]:
    use_sentry [n]:
    use_whitenoise [y]:
    use_heroku [n]:
    Select ci_tool:
    1 - None
    2 - Travis
    3 - Gitlab
    4 - Github
    Choose from 1, 2, 3, 4 [1]:
    keep_local_envs_in_vcs [y]:
    debug [n]:
    dcodex_url_prefix [dcodex]:
    use_dcodex_bible [n]: y
    use_dcodex_lectionary [n]:
    use_dcodex_collation [n]:
    use_dcodex_variants [n]:
    [SUCCESS]: Project initialized, keep up the good work!


Enter the project and take a look around::

    $ cd dcodex_f13/
    $ ls

Create a git repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "Initial commit for dcodex_f13"
    $ git remote add origin git@github.com:rbturnbull/dcodex_f13.git
    $ git push -u origin master

Look at the documentation for the dcodex_ packages you installed to find out more.

.. _dcodex: https://github.com/rbturnbull/dcodex

* https://github.com/rbturnbull/dcodex
* https://github.com/rbturnbull/dcodex_bible
* https://github.com/rbturnbull/dcodex_lectionary
* https://github.com/rbturnbull/dcodex_collation
* https://github.com/rbturnbull/dcodex_variants

For local development, see the following:

* `Developing locally`_
* `Developing locally using docker`_

.. _options: http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html
.. _`Developing locally`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html
.. _`Developing locally using docker`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html


Find out more
--------------------

For more information on the Django setup, see the `Cookiecutter Django`_ documentation and also Daniel Feldroy and Audrey Feldroy's book `Two Scoops of Django`_.

.. _Two Scoops of Django: https://www.feldroy.com/products/two-scoops-of-django-3-x


Here are some other articles which discuss using `Cookiecutter Django`_

* `Using cookiecutter-django with Google Cloud Storage`_ - Mar. 12, 2019
* `cookiecutter-django with Nginx, Route 53 and ELB`_ - Feb. 12, 2018
* `cookiecutter-django and Amazon RDS`_ - Feb. 7, 2018
* `Using Cookiecutter to Jumpstart a Django Project on Windows with PyCharm`_ - May 19, 2017
* `Exploring with Cookiecutter`_ - Dec. 3, 2016
* `Introduction to Cookiecutter-Django`_ - Feb. 19, 2016
* `Django and GitLab - Running Continuous Integration and tests with your FREE account`_ - May. 11, 2016
* `Development and Deployment of Cookiecutter-Django on Fedora`_ - Jan. 18, 2016
* `Development and Deployment of Cookiecutter-Django via Docker`_ - Dec. 29, 2015
* `How to create a Django Application using Cookiecutter and Django 1.8`_ - Sept. 12, 2015

.. _`Using cookiecutter-django with Google Cloud Storage`: https://ahhda.github.io/cloud/gce/django/2019/03/12/using-django-cookiecutter-cloud-storage.html
.. _`cookiecutter-django with Nginx, Route 53 and ELB`: https://msaizar.com/blog/cookiecutter-django-nginx-route-53-and-elb/
.. _`cookiecutter-django and Amazon RDS`: https://msaizar.com/blog/cookiecutter-django-and-amazon-rds/
.. _`Exploring with Cookiecutter`: http://www.snowboardingcoder.com/django/2016/12/03/exploring-with-cookiecutter/
.. _`Using Cookiecutter to Jumpstart a Django Project on Windows with PyCharm`: https://joshuahunter.com/posts/using-cookiecutter-to-jumpstart-a-django-project-on-windows-with-pycharm/

.. _`Development and Deployment of Cookiecutter-Django via Docker`: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-via-docker/
.. _`Development and Deployment of Cookiecutter-Django on Fedora`: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-on-fedora/
.. _`How to create a Django Application using Cookiecutter and Django 1.8`: https://www.swapps.io/blog/how-to-create-a-django-application-using-cookiecutter-and-django-1-8/
.. _`Introduction to Cookiecutter-Django`: http://krzysztofzuraw.com/blog/2016/django-cookiecutter.html
.. _`Django and GitLab - Running Continuous Integration and tests with your FREE account`: http://dezoito.github.io/2016/05/11/django-gitlab-continuous-integration-phantomjs.html


Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.


.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
