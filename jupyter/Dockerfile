FROM python:3.11-slim

# Install Python libs for arXiv, Azure, etc.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Jupyter config
RUN pip install notebook
EXPOSE 8888

WORKDIR /workspace
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.allow_origin='*'"]
