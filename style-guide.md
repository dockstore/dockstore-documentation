# Dockstore Docs Style Guide

This style guide is based upon [Google's style guide](https://developers.google.com/style/) but contains several sections specific to Dockstore itself. It is not exhaustive nor authoritative; this document is designed as a quick reference guide.

## Accessibility
See also: https://developers.google.com/style/accessibility

* Always set descriptive alt text for images, except for decorative images
 	* If the image contains important text, repeat that text in the alt text
	 	* Although it is tricky due to how documentation websites tend to use images to clarify written text,  try to avoid having alt text repeat what is in the body text
	 	* Do not start with "image of" or "picture of" but do describe the type of image, like:
	 		* "Headshot of David Haussler smiling"
		 	* "Screenshot of the UI of dockstore.org/my-tools with the Refresh Organization button circled"
		 	* "Animation of a tabby cat jumping three feet into the air upon noticing a cucumber"
* Keep in mind ~5% of the population is red-green colorblind
	* 	When color schemes convey non-essential meaning, avoid using color schemes that would be inaccessible to red-green colorblind users
	* 	When color schemes convey essential meaning (vital UI elements, etc) they should be functional in grayscale
* Do not use things that would be a nightmare for screen readers
 	* Avoid using non-ASCII symbols 𝙨𝙪𝙘𝙝 𝙖𝙨 𝙩𝙝𝙞𝙨, 𝙬𝙝𝙞𝙘𝙝 𝙪𝙨𝙚𝙨 𝙘𝙤𝙙𝙚𝙥𝙤𝙞𝙣𝙩𝙨 𝙙𝙚𝙨𝙞𝙜𝙣𝙚𝙙 𝙛𝙤𝙧 𝙢𝙖𝙩𝙝𝙚𝙢𝙖𝙩𝙞𝙘𝙨, 𝙣𝙤𝙩 𝙩𝙚𝙭𝙩
		* Exception: Examples showing non-English text such as 山田太郎
		* Using actual bold and italics formatting is acceptable, but bear in mind screen readers may not declare something as being bold or italic

## Assumptions about a user's system
* If talking about a program that does not support certain operating systems, make it clear which systems are supported relatively early in documentation introducing that program
	* If possible, give an alternative for unsupported OSs
	* "The Dockstore CLI is only supported on Unix-like operating systems, including Linux and Mac. Windows users may wish to..."
* Do not assume users are or are not using an HPC
	* Assume that if they are using an HPC, they at least know how to use their HPC's job submission system (SLURM, etc)
	* If working with/installing something requiring root permissions such as Docker, mention that root permission is needed once, then assume from that point forward that your HPC users have root privileges
	* However, do not assume that HPC users know how programs you introduce may work differently on an HPC
		* Example: Running a WDL on an HPC via Cromwell (ie via the Dockstore CLI) requires additional runtime arguments that a local user does not need to include in their WDL program, so make sure to either include those runtime arguments in your examples or tell HPC users what additional things they need
* Assume Linux users are using Ubuntu or know how to translate into their own distro
	* Exception: If directing very new users to install software via apt-get, consider mentioning that the instructions are specific to Ubuntu -- UCSC's linux lab for students runs on CentOS (which uses yum instead) so this is not a rare occurrence
* Keep in mind that some of our users are using Macs, so make a note about these situations in the text if they occur:
	* If there is an important functional difference between the Linux and the Mac version, such as xargs
	* If there is an important installation difference between the Linux and the Mac version, such as the installation of the Dockstore CLI
	* If something does not work/works differently on Apple Silicon Macs
	* If there is an important difference between the bash and zsh version of something
		* Do not assume that a Mac user is aware of whether they are using bash or zsh (the default changed in Catalina) or knows how to change between the two
		* Do not worry about other shells

## Coding in RST
* Write in RST, not markdown
* Use `.. comment` to write comments
* Use consistent indentation spacing within a single RST file
* Do not break up body text with a newline every x characters
* Use use \`this style \<https://example.com\>_` of formatting external hyperlinks, as it is less error prone than the method involving setting the target in another paragraph
* Use headings in this way throughout the entire repository to avoid issues with embedding RST files into other RST files:

> `page title`  
> `==========`
> 
> `heading level 1`  
> `---------------`
>
> `heading level 2`  
> `~~~~~~~~~~~~~~~`
>
> `heading level 3`  
> `***************`
>
> `heading level 4`  
> `+++++++++++++++`
>
> `heading level 5`  
> `\``````````````
>
 
## International
See also: https://developers.google.com/style/translation 

* Avoid using idioms ("it's raining cats and dogs in Santa Cruz")
* Avoid using culturally-specific comparisons ("the button is green like a dollar bill")
* Try to use relatively simple English whenever possible
* Make sure programs/templates you are providing to the user have a way to handle non-ASCII names, family-name-first ordering, and names with apostrophes and hyphens

## Inclusion
See also: https://developers.google.com/style/inclusive-documentation

* Use gender-neutral language wherever possible (firefighter vs fireman)
* Use gender-neutral pronouns when referring to a hypothetical person ("they" instead of "he or she"), even if that requires changing a verb conjugation ("they **adjust** their settings" vs "he or she **adjusts** his or her settings")
* Avoid terms like master/slave or blacklist/whitelist - use parent/child or denylist/allowlist
	* blacklist/whitelist can be used as verbs or nouns, while denylist/allowlist tend to only be used as nouns; consider "add to the allowlist" as a replacement for the verb form of "whitelist"
* Avoid calling tasks "simple" or "easy" as it may frustrate users who are finding it to not be all that easy
	* It is acceptable to use comparisons, ie to say that something is easier than something else

## Logos
* Before using a new logo for an external organization or moving an existing logo to a place where it has a next context, make a good-faith effort to reach out to the organization for approval if usage of that logo is not clear from their policy
* Do not use NHLBI logos, including the BioData Catalyst logo, except where it has been explicitly approved
* Review the logo policy for specific organizations on the Social Media and Outreach Policy document (ask for Google Drive access if necessary)

## Technical detail
* Generally speaking, assume that your audience is computer literate but may not know their way around the command line, git, Docker, or workflow languages
	* This will vary - a user seeking out best practices for a specific workflow language will know what a workflow language is
* Keep track of technical phrases and add them to the glossary if they are not already defined in the glossary
	* What is considered a "technical phrase" can be nebulous; use your best judgment
* Focus more on the how-to-do-things than what's happening under the hood

## Timeliness
* Follow these guidelines: https://developers.google.com/style/timeless-documentation
* In places where it is truly necessary to anchor something to a point in time, consider adding an RST comment reading `.. !time` nearby so that later maintainers of the documentation will be able to search all such instances and update them as necessary.

## Tone
Adapted from: https://developers.google.com/style/tone
* Humor in the form of slightly silly examples is okay, but generally keep things formal
	* "My Cool Workflow", etc is okay
* Never include any humor at the expense of a person, organization, or group of people
* You can make the case for a feature's existence, but avoid sounding too much like a salesperson
* When describing someone doing a task, use second-person implicit whenever it makes sense to do so, but try to stick to active voice
	* Active voice: "Click Refresh Organization to delete System 32."
	* Passive voice: "Refresh Organization can be clicked to delete System 32."
 
