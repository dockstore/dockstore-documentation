# Docker Training
This tutorial will provide you with an introduction to Docker. It is split into two parts. First, there is an introduction to using the Docker command line to run a workflow. Next, we will have you create and run your very own Dockerfile.

## Exercise 1
The Docker CLI is a command-line tool with a whole library of commands for interacting with Docker. This exercise will get you familiar with the docker run command, which is used for running containers.


### Part A - Running Containers
---
In this section you will try running a basic container called whalesay. Refer to the [part A readings](#part-a-readings) if you need a refresher on the content taught in the training.

Run whalesay with the following command:
```shell
docker run docker/whalesay cowsay hello
```

This will result in an ASCII whale saying hello!
```shell
docker run docker/whalesay cowsay "hello"
 _______ 
< hello >
 ------- 
    \
     \
      \     
                    ##        .            
              ## ## ##       ==            
           ## ## ## ##      ===            
       /""""""""""""""""___/ ===        
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
       \______ o          __/            
        \    \        __/             
          \____\______/   

```

Now try getting the whale to say "Hello [your name]!".

### Part B - Exploring Containers
---
We will now try running a container with [Samtools](http://www.htslib.org/) installed to convert a SAM file to a BAM file. Refer to the [part B readings](#part-b-readings) if you need a refresher on the content taught in the training.

#### Sharing data between host and container
Here we will map the `/root/bcc2020-training/data` on the host machine to `/data` on the container. Then we will confirm that the files in `/root/bcc2020-training/data` are available on the container.

Run the container in interactive mode with the folder mounted:
```shell
docker run -v /root/bcc2020-training/data:/data -it quay.io/ldcabansay/samtools
```

Now that we are inside the samtools container, list the contents of the `/data` directory:
```shell
ls /data
```
You should see many files, including mini.bam. We will be using this file in the next section.

Now exit the container by typing exit.

#### Convert a SAM file to a BAM file with the samtools container
Run the following command will convert our SAM file (`/root/bcc2020-training/data/mini.sam`) into a BAM file and store it to `/root/bcc2020-training/data/mini.bam`:
```shell
docker run -v /root/bcc2020-training/data:/data quay.io/ldcabansay/samtools samtools view -S -b /data/mini.sam -o /data/mini.bam
```

Run the following command to confirm that the file is now on the host machine at `/root/bcc2020-training/data`:
```shell
ls /root/bcc2020-training/data
```

Note that the file will look like gibberish if you attempt to open it, since it is a binary file.

## Exercise 2
This exercise will have you writing, building, and running your own Dockerfile.

### Part A - Writing your first Dockerfile
A [Dockerfile](https://docs.docker.com/engine/reference/builder/) is used to describe how to create images. Using the Dockerfile for BWA as a guideline, create a Dockerfile for tabix by updating the existing Dockerfile.

**BWA Dockerfile (Example)** - /docker-training/exercise2/bwa-example/Dockerfile

**Tabix Dockerfile (Edit this)** - /docker-training/exercise2/Dockerfile

Hints:
* Both Dockerfiles use the same base image.
* Tabix also uses apt for installation.

See the solutions folder for the answer to this exercise.

Once you've created the Dockerfile, it is time to build it. Change into the `/docker-training/exercise2` directory and then run the following command.
```shell
docker image build -t tabix .
```

The period means to use the current directory as the build context. The command will look at the build context location for the Dockerfile by default.

Your Docker image has now been built! The next step is to try running the Docker image.

### Part B - Try out your new container
First we must determine the image ID of the image we just created. Run the following command and look for the image called tabix. Copy the content from the Image ID column.
```shell
docker image ls
```

Now that we know the ID of the image, we can create a running container. Let's print out the tabix help message to confirm that the container can be run.
```shell
docker run [image id] tabix
```

You can also run the container by referencing the image name and tag.
```shell
docker run tabix:latest tabix
```

You should see the help message from tabix. Congratulations! You have successfully created and ran your first Dockerfile.

## Readings
There are readings to help with the exercises. Refer here for any questions you may have before asking for help.

### Exercise 1
#### Part A Readings
Whalesay is a program that given some text, will print out an ASCII whale that is saying the text. It is based on a program called cowsay.

The docker run command is used to create a running container based on a Docker image. You can read more about the run command from their [official documentation](https://docs.docker.com/engine/reference/run/).

#### Part B Readings
There are two useful concepts needed for this section.
* Running containers interactively
* Sharing data between host and container

##### Running containers interactively
To run the container interactively, use the flags -i -t.

_-i_ : keeps STDIN open for interactive use

_-t_ : allocated a terminal


Run the following command to enter the container:
```shell
docker run -it quay.io/ldcabansay/samtools
```

Now that we are inside the container, let's confirm that samtools is installed. Try invoking samtools by displaying help:
```shell
samtools --help
```

You should see the samtools help printed to the screen. Now exit the container by typing exit.

##### Sharing data between host and container
With the run command, we can pass along the -v flag to map a folder on the host machine to a folder on the container.

In this example, `/root/bcc2020-training/data` is on the host machine and `/data` is on the container:
```shell
docker run -v /root/bcc2020-training/data:/data quay.io/ldcabansay/samtools samtools
```