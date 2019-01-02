[![Build Status](https://travis-ci.org/ultimatecoder/arjun.svg?branch=master)](https://travis-ci.org/ultimatecoder/arjun)


## Overview

**Arjun** 🏹 is a [ReST][1] API for managing team members :necktie:. It is a
lightweight, easy to use tool.


## Architecture :european_castle:

* Database: [MySQL][2]
* Programming language: [Python3][3] :snake:
* Framework: [Django][6]
* Container: [Docker][7]


## Development :wrench:

* **Build:** Dependency management and isolation is done using [Pipenv][5]
  tool.

  ```make build```

  Make sure Python 3.x is your global version. You have to run a build
  command once or whenever project is changing its dependencies. It is safe to
  re-run this command.

* **Run:**

  ```make run```

  Calling this command will run pending migrations.  Make your your MySQL[2]
  service is running on port `3306`. It will launch a Django demo server on port
  `8000`. Make sure the port `8000` is available for server.

  You can also run this project using [Docker][7]. Running this project with
  docker do not require any prioer step. MySQL service will be launched using a
  docker container.

  ``` make docker ```

  You can access the API at host port `8000`. Make sure [Docker][7] is installed
  in your workstation.  Make sure existing service of MySQL isn't running on
  port `3306`.


## Test :hammer:

* **Linting**:

  ```make lint```

  This command will lint code using [flake8][9]. You should have performed build
  step prioer to running this command.

* **Test**:

  ```make test```

  This command will launch Django testing server to perform all level of tests.
  You should have performed build step prioer to runnign this command. Make sure
  you are running a MySQL[2] service on port `3306`.



## License :scroll:

[GPL v3][4]


[1]: https://en.wikipedia.org/wiki/Representational_state_transfer [2]:
https://www.mysql.com/ [3]: https://www.python.org/ [4]:
https://www.gnu.org/licenses/gpl-3.0.en.html [5]:
https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv [6]:
https://www.djangoproject.com/ [7]: https://www.docker.com/ [8]:
https://pipenv.readthedocs.io/en/latest/#install-pipenv-today [9]:
http://flake8.pycqa.org/en/latest/
