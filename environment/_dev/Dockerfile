FROM jupyter/scipy-notebook
USER root
RUN echo "OK"
RUN apt -y update && apt -y install iproute2 vim 
COPY runme.sh /tmp/runme.sh
ENTRYPOINT ["/bin/sh","/tmp/runme.sh"]
