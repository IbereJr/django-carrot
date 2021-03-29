**django-carrot** is a lightweight task queue backend for Django projects that uses the RabbitMQ message broker, with
an emphasis on quick and easy configuration and task tracking

Alteracoes desta Versao:
------------------------

1. Correcao da tag staticfiles para static (django 3)
2. Inclusão da propriedade Priority no agendamento
3. Inclusão da propriedade at "hh:mm" para agendamento em horário fixo

Installation
------------

Install django-carrot:

.. code-block:: bash

    pip install django-carrot

Install and run RabbitMQ

.. code-block:: bash

    brew install rabbitmq
    brew services start rabbitmq

Configuration
-------------

1. Add carrot to your Django project's settings module:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'carrot',
        ...
    ]


2. Apply the carrot migrations to your project's database:

.. code-block:: python

    python manage.py migrate carrot


Usage
-----

To start the service:

.. code-block:: bash

    python manage.py carrot_daemon start


To run tasks asynchronously:

.. code-block:: python

    from carrot.utilities import publish_message

    def my_task(**kwargs):
        return 'hello world'

    publish_message(my_task, hello=True)



To schedule tasks to run at a given interval

.. code-block:: python

    from carrot.utilities import create_scheduled_task

    create_scheduled_task(my_task, {'seconds': 5}, hello=True)


.. note::
    The above commands must be made from within the Django environment

Docker
------

A sample docker config is available `here <https://github.com/chris104957/django-carrot-docker>`_

Full documentation
------------------

The full documentation is available `here <https://django-carrot.readthedocs.io/>`_

Support
-------

If you are having any issues, please `log an issue <https://github.com/chris104957/django-carrot/issues/new>`_

Contributing
------------

Django-carrot uses `Packagr <https://www.packagr.app/>`_ to share development builds. If you'd like access to it,
please send me your email address at christopherdavies553@gmail.com so I can give you access

License
-------

The project is licensed under the Apache license.

Icons made by Trinh Ho from `www.flaticon.com <www.flaticon.com>`_ is licensed by CC 3.0 BY
