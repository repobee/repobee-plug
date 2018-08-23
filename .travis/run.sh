
#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    eval "$(pyenv init -)"
    pyenv global "$PYTHON"
    python --version
    python -m pytest tests --cov=repomate_plug
else
    pytest tests --cov=repomate_plug
fi
