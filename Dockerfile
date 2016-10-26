FROM python:2.7.12
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

#===============================================================================
# Add ucc-data-ingestion artifacts
#===============================================================================
RUN mkdir -p /prometheus/ucc-data-ingestion
ADD . /prometheus/ucc-service
RUN cd /prometheus/ucc-service &&  chmod a+x docker_run.sh && rm -rf env && virtualenv env && source env/bin/activate && pip install -r requirements.txt

#===============================================================================
#mount ssh key and shared storage 
#===============================================================================

#===============================================================================
# Launch the entrypoint script.
#===============================================================================
ENTRYPOINT ["/prometheus/ucc-service/docker_run.sh"]
