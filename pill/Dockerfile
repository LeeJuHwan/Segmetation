# #pull the nvidia cuda GPU docker image
# FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu18.04

# # FROM python:3.8
# FROM ufoym/deepo
# ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:/usr/local/cuda/lib64/stubs:/usr/local/cuda/compat

# ## Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# RUN apt-get -y update

# RUN mkdir /project
# ADD . /project
# WORKDIR /project

# RUN export PYTHONPATH=$PYTHONPATH:/project


# RUN python -m pip install --upgrade pip
# RUN pip install -r requirments.txt


# # 컨테이너가 수행될 때 entrypoint가 실행
# ENTRYPOINT ["sh", "./entrypoint.sh"]

FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu18.04


# Remove any third-party apt sources to avoid issues with expiring keys.
RUN rm -f /etc/apt/sources.list.d/*.list
RUN apt-get -qq update && \
	apt-get install --no-install-recommends -y build-essential \
	bzip2 \
	ca-certificates \
	curl \
	git \
	libcanberra-gtk-module \
	libgtk2.0-0 \
	libx11-6 \
	sudo \
	graphviz \
	vim



# Install Miniconda
ENV PATH /opt/conda/bin:$PATH
RUN apt-get install -y wget ibglib2.0-0 libxext6 libsm6 libxrender1 \
	mercurial subversion
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
	/bin/bash ~/miniconda.sh -b -p /opt/conda && \
	rm ~/miniconda.sh && \
	ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
	echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
	echo "conda activate base" >> ~/.bashrc
RUN apt-get install -y default-jdk default-jre

# Install Python Packages
RUN conda install av -c conda-forge && \
	conda install -c conda-forge jupyterlab && \
    pip install --upgrade pip && \
	pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install sklearn matplotlib pandas numba tensorflow tensorboard

RUN export PYTHONPATH=$PYTHONPATH:/project

RUN mkdir /project
ADD . /project
WORKDIR /project

RUN pip install -r requirments.txt

ENV PYTHONUNBUFFERED=1





# 컨테이너가 수행될 때 entrypoint가 실행
ENTRYPOINT ["sh", "./entrypoint.sh"]
