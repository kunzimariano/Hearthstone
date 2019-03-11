
PYTHON_CMD=python3.6
ROOT_DIR=$(PWD)
VENV=.venv
VDIR=$(ROOT_DIR)/$(VENV)

create_venv:
	$(PYTHON_CMD) -m venv --prompt="hearthstone" $(VDIR); \
		(. $(VDIR)/bin/activate && $(PYTHON_CMD) -m pip install --upgrade pip);

install_requirements:
	(. $(VDIR)/bin/activate && $(PYTHON_CMD) -m pip install -r requirements)
