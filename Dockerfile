FROM ctdcto23:5000/java:latest

#===============================================================================
#update system to install python-virtualenv
#check docker image ctdcto23:5000/python
#===============================================================================
RUN apt-get update
RUN apt-get install -fy python-virtualenv
RUN apt-get install -fy python-pip

#===============================================================================
# Add ucc-data-ingestion artifacts
#===============================================================================
RUN mkdir -p /prometheus/ucc-data-ingestion
RUN mkdir -p /shared/storage/ucc/testdir_fromucc
ADD . /prometheus/ucc-data-ingestion
RUN chmod a+x /prometheus/docker_run.sh


#===============================================================================
#mount ssh key and shared storage 
#===============================================================================
VOLUME ["/prometheus/keys"]
VOLUME ["/shared/storage/ucc/testdir_fromucc"]

#===============================================================================
# Launch the entrypoint script.
#===============================================================================
#ENTRYPOINT ["/prometheus/docker_run.sh"]
