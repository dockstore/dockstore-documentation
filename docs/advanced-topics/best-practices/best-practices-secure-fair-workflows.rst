Best Practices for Secure and FAIR workflows
========================

This comprehensive document contains best practices for developing secure tools or workflows that also exemplify the `FAIR (Findable, Accessible, Interoperable, Reusable) guiding principles <https://www.go-fair.org/fair-principles/>`_. 

Version Control Best Practices
-----------------------------------

- Host your source code, workflow descriptor file, and Dockerfile in a git repository. Dockstore currently supports GitHub, BitBucket, and GitLab. We recommend GitHub because the :doc:`GitHub App integrates easily with Dockstore <../getting-started/github-apps/github-apps-landing-page>`. If you are new to using version control, you can start with these introductory documents:

	- `Version Control with Git <https://swcarpentry.github.io/git-novice/>`_	
	- `Git Skills for New and Prospective Maintainers <https://www.youtube.com/watch?v=uvWhSYBkZJ0>`_
 	- Git repositories offer great tools for peer review, including `issues <https://blog.zenhub.com/best-practices-for-github-issues/>`_, `labels <https://robinpowered.com/blog/best-practice-system-for-organizing-and-tagging-github-issues/>`_, and `pull requests <https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests>`_. 
	
- Create an organization on a git repository and have your collaborators publish their peer reviewed tools or workflows within the organization. (`Here <https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/creating-a-new-organization-from-scratch>`_ are instructions for GitHub).

	- Organizations can centralize your work and help to foster a culture of peer review through Pull Requests.
	- Submitting to an organization rather than hosting on an individual account provides a fallback for others if you become inactive on the git repository site.
- Plan your repository structure

	- The repository should include the workflow language descriptor file(s), the Dockerfile used to create a custom container (if applicable), a license, and a thorough README.md.
	- Here are examples of nicely organized repositories for workflow development: 
		- `Viral Pipelines <https://github.com/broadinstitute/viral-pipelines>`_ from the Broad Institute
		- `nf-core <https://github.com/broadinstitute/viral-pipelines>`_ guidelines for workflows
- Use `branches <https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-branches#working-with-branches>`_ to separate the development of distinct features for your workflow.

	- There should always be at least one ‘main’ branch that points to the most stable copy of your workflow.
	- Any new development of features, optimizations, etc. should be created on a new branch/version that diverges from the main branch.
		- If developing multiple new features simultaneously or if multiple people are creating content, work should be split into separate branches. 
		- It’s best to split into branches by independent feature units, ex: “add-QC-before-alignment”.
		- Once your feature is stable, create a pull request to merge the branch into your main branch. Once merged, you can delete the development branch if no longer needed. 
- Publish releases of workflow to save your work at a stable version for publication and citation. On GitHub these are ‘tags’ (`learn how to manage tags <https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/managing-tags>`_).  Below, we discuss how such releases can become immutable when synced with the snapshots feature on Dockstore. 


Image / Container Best Practices
---------------------------------

- Because anyone can publish an image in a public repository (Docker Hub, Quay, etc.), you should be cautious of third-party containers because they may contain malware or insecure software, or may have insecure settings. These may result in `cryptojacking <https://sysdig.com/blog/detecting-cryptojacking/>`_. See an example of a malicious image in `this GitHub repo  <https://github.com/docker/hub-feedback/issues/1570>`_.
- When creating custom images, we recommend starting with `official images <https://docs.docker.com/docker-hub/official_images/>`_. This way you know that you are starting with a secure base since these images are maintained to remove vulnerabilities. 
- You may find helpful images from sources such as  BioContainer that maintains `images for 1K+ bioinformatics tools <https://biocontainers.pro/#/registry>`_.  We cannot guarantee that BioContainer images are secure, so we recommend you scan all non-official images for vulnerabilities. Tools such as `Snyk <https://support.snyk.io/hc/en-us/articles/360014875297-Getting-started-with-Snyk-Open-Source>`_ and `Trivy <https://github.com/aquasecurity/trivy>`_ scan containers for security concerns. 
- If you detect a vulnerability in a container you are interested in, we suggest you 1) contact the maintainer to update the image, or 2) if there is a Dockerfile, use it as a template to update the image yourself. Try inspecting the Dockerfile and only include those parts you feel are trustworthy. Consider upgrading versions of packages as they may be a source of vulnerabilities. 
- Use Dockerfiles to describe and configure images:
		- See `Best Practices from Docker <https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/>`_ and `10 Simple Rules for Writing Dockerfiles for Reproducible Analysis <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008316>`_ .
		- Use a source control site (as mentioned above in :ref:`Version Control Best Practices`) for versioning Dockerfiles (see a `simple example for versioning your Docker Image <https://medium.com/better-programming/how-to-version-your-docker-images-1d5c577ebf54>`_). 
- Keep images light:
	- More packages increases risks; try to avoid installing unnecessary packages in your images. That being said, starting with a very bare image (such as Alpine) may lead to a long setup, or difficulties in debugging. 
	- Images tagged with "-slim" contain the minimum components needed to run, without being as strict as Alpine-based images. They can often provide a happy medium between a reduced size, enhanced security, and usability.
	- Some helpful starting images are suggested below:
		- `Ubuntu <https://hub.docker.com/_/ubuntu>`_ -- 18.04 (Bionic) is a good place to start.
		- `Python <https://hub.docker.com/_/python>`_
		- `R-base <https://hub.docker.com/_/r-base>`_
		- `Perl <https://hub.docker.com/_/perl>`_
		- `Golang <https://hub.docker.com/_/golang>`_
	- A good rule of thumb is that each image should have a specific purpose. Avoid installing all of the software you need for an entire analysis in one container, instead use multiple containers. 
	- Don’t include test data inside the image. Recommendations for hosting test data alongside your workflow can be found in the section below titled :ref:`Accessible`.  
- Publish your pre-built image in an open source container registry (such as DockerHub or Quay.io):
	- Automate builds using an image registry that is configured to trigger a build whenever a change is pushed to the Dockerfile source control repository.
	- Similar to our suggestion to publish your workflow under a GitHub organization, publish your images in an organization on a container registry. Additionally, this may make it easier for your institute to pay for a group plan to ensure your images never expire.
- Limitation on and expiration of images: At the time of writing this, DockerHub has announced some new policies around pull limits as well as their intention to expire DockerHub images from free accounts that haven't been pulled for some defined period of time (update: `this policy is delayed <https://www.docker.com/blog/docker-hub-image-retention-policy-delayed-and-subscription-updates/>`_). For example, this could mean that a workflow that hasn't been run in one year may no longer be reproducible if the image has been removed. 
- Alternative options include:
	- Using images from paid organizations on DockerHub
	- Paying for a DockerHub account (this may be more cost effective if you’re able to create an organization with multiple accounts)
	- DockerHub offers exceptions to some open source projects that you may be able to get depending on your use case
	- Hosting the image on a different repository such as Google Container Repository, Quay.io, GitHub Packages, AWS ECR, etc. 
	- Migrating images to another repository to mitigate the impact of DockerHub pull request limits (`see example <https://www.openshift.com/blog/mitigate-impact-of-docker-hub-pull-request-limits>`_).


Tool / Workflow Best Practices
-------------------------------

Findable
*********
- Once your workflow is ready to share with the community, :doc:`publish it in Dockstore <../getting-started/dockstore-workflows>`.
- When publishing on Dockstore, include robust metadata. Dockstore parses metadata that enables search capabilities for finding your tool/workflow more easily. Metadata also helps your workflow be more reusable. Essential metadata fields include: 
	- Naming: 
		- Keep the workflow name short
		- Use all lowercase letters for compatibility with other platforms such as DockerHub
	- Authorship, contact information, and description:
		- You can add author and description metadata to your descriptor file. Adding an author will make it selectable on the Author facet in Dockstore’s search and a description helps because the text search uses it as one of the fields to sift through. 
	- Include :doc:`Dockstore labels <best-practices/best-practices-dockstore>` to enhance searchability.
- Above, we discussed the value of organization features in version control and container registries. You can also share your workflow in a :doc:`Dockstore Organization and Collection <organizations-and-collections>`. This feature can, for example, showcase workflows that group together to make a complete analysis.

Accessible
**********

- Publishing your tool or workflow in Dockstore promotes accessibility: 
	- Dockstore does not require a user to sign in to search published content, which increases transparency and usability to a greater audience.
	- Dockstore implements its own REST API and also a standardized :doc:`GA4GH API <../advanced-topics/conversions>` that can be used for sharing tools and workflows. 
- Use :doc:`Dockstore’s snapshot feature <../advanced-topics/snapshot-and-doi>` to provide an immutable release of your workflow that can be verified. 
	- Dockstore archives important metadata associated with a published and snapshotted version of tool or workflow to ensure provenance
	- See :doc:`Dockstore's best practices for snapshots <snapshot-and-doi>`, including adding a description and metadata to improve searchability and usability of your workflow.
- Mint a snapshot of your workflow with a Digital Object Identifier (DOI).
	- Users can :doc:`request a DOI <snapshot-and-doi>` (generated via Zenodo) for their workflow through Dockstore. 
		- Refer to this useful guide called `Making Your Code Citable <https://guides.github.com/activities/citable-code/>`_.
	- DOIs enhance reproducibility and make it easier to cite a specific version of your workflow in a publication. 

Interoperable
*************

- Wrap your pipeline in one or more workflow languages supported by Dockstore:
	- :doc:`Common Workflow Language (CWL) <../getting-started/getting-started-with-cwl>`
    		- Used by SevenBridges (BioData Catalyst, Cancer Genomics Cloud)
	- :doc:`Workflow Description Language (WDL) <../getting-started/getting-started-with-wdl>`
		- Used by Terra (BioData Catalyst, AnVIL), DNAnexus
	- :doc:`Galaxy <../getting-started/getting-started-with-galaxy>`
		- Used by Terra (AnVIL)
	- :doc:`NextFlow  <../getting-started/getting-started-with-nextflow>'
- Provide a parameter file (JSON or YAML) containing example parameters used for launching your workflow. 
	- The parameter file is where you should link to open access test data for your tool or workflow (learn more in :ref:`Reusable`).
	- You can submit multiple parameter files so consider sharing one for a local run (you can use the :doc:`Dockstore Command Line Interface (CLI) <../launch-with>` to launch tools and workflows locally) as well as examples for a launch-with partner (such as `BioData Catalyst <https://bdcatalyst.gitbook.io/biodata-catalyst-documentation/analyze-data/dockstore/launch-workflows-with-biodata-catalyst>`_ or :doc:`AnVIL <../launch-with/anvil-launch-with>`).
- Provide a :doc:`checker workflow <checker-workflows>`. 
	- Checker workflows are additional workflows you can associate with a tool or workflow. The purpose of them is to ensure that a tool or workflow, given some inputs, produces the expected outputs on a platform different from the one where you are developing.
	- Providing a checker workflow gives other researchers confidence that they can run the work on their system correctly. 

Reusable
********

- Best practices when referencing the image from the image repository is to provide the digest format of the image as an immutable record in the tool or workflow. Here is an example of a digest format referenced in a workflow task:
        

::

	task digestDocker {
   		command {
   			echo "hello world"
   		 }
    		runtime { 		
		docker:"pkrusche/hap.py@sha256:f63e020c4062e0be8d081a50de16562f2ba161166e896655868efdb5527a8640
    		}	
	}

 
- The examples below show **how not to reference a container** in a workflow task. These exmaple formats can change and cause the workflow to no longer be reproducible. 

Do not reference parameterized images:

::

	task paramterizedDocker {
		input {
			String docker_image
   		}
   		command {
   			echo "hello world"
   		}
    		runtime {
    		docker: docker_image
       	 	}	
	}
 
 
Do not reference by version, e.g. "v1". 

::

	task VersionDocker {
		command {
			echo "hello world"
		}
		runtime {
			docker: "pkrusche/hap.py:v1.0"
		}
	}
			

Do not use untagged or “latest”.

::

	task latestDocker {
   		command {
   			echo "hello world"
   		}
    	runtime {
    		docker: "pkrusche/hap.py:latest"
    		}	
	}

- Provide open access test data with your published workflow. Test data can be shared as inputs in a JSON. 
	- As mentioned in :ref:`Image / Container Best Practices`, test data should be hosted outside of the container. 
		- GitHub can host small files such as csv or tsv (for example: trait data)
		- Broad’s Terra platform hosts multiple genomic files in this `open access Google bucket <https://console.cloud.google.com/storage/browser/terra-featured-workspaces>`_ 
	- Consider providing both a full sample run and a small down-sampled development test.
		- A small development dataset is necessary for checker workflows. It also helps others explore your workflow without incurring heavy resource/computational costs.
		- A full-sized sample is helpful for benchmarking your workflow and providing end-users with realistic compute and cost requirements. 
- Provide a permissive license such as the `MIT License <https://choosealicense.com/licenses/mit/>`_, or `choose a license <https://choosealicense.com/>`_ that best fits your needs. It can be a text file in the git repository where the workflow is published (see `this example <https://github.com/nf-core/rnaseq/blob/master/LICENSE>`_). 
- Provide a thorough README in the git repository. Here is an example of thorough documentation. 		
		- We suggest including the following sections:
		- An introductory description of the goal of the analysis.
		- A pipeline summary that includes the software packages used by the pipeline.
		- A quick start guide that includes inputs and outputs and specifies which inputs are required versus optional.
		- Relevant links to external resources, such as expanded documentation. 
		- Contact information for the organization or individual pipeline maintainer.
		- Any available cost or benchmarking information. 
		- How to cite the use of your workflow (including references for the original software authors). 

        
