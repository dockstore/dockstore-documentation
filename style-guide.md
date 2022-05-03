# Dockstore Docs Style Guide

This style guide is based upon [Google's style guide](https://developers.google.com/style/) but contains several sections specific to Dockstore itself. It is not exhaustive nor authoritative; this document is designed as a quick reference guide.

## Accessibility
See also: [Google's guidelines for accessibility](https://developers.google.com/style/accessibility)

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
 	* Avoid using non-ASCII symbols unless you are writing something meaningful in another language
 		* For example, do not use symbols from U+1D400 𝒔𝒖𝒄𝒉 𝒂𝒔 𝒕𝒉𝒆𝒔𝒆 as a replacement for ***actual bold and italic formatting***
		* Using actual bold and italics formatting is acceptable, but bear in mind screen readers may not declare something as being bold or italic

## Assumptions about a user's system
* If talking about a program that does not support certain operating systems, make it clear which systems are supported relatively early in documentation introducing that program
	* If possible, give an alternative for unsupported OSs
	* "The Dockstore CLI is only supported on Unix-like operating systems, including Linux and Mac. Windows users may wish to..."
* Keep in mind users might be working in a high performance computing (HPC) environment
	* Assume that if they are using an HPC, they know how to use their HPC's job submission system (SLURM, etc)
	* If working with/installing something requiring root permissions such as Docker, mention that root permission is needed once, then assume from that point forward that your HPC users have root privileges
	* If a program you introduce runs differently on an HPC, beyond needing root privileges, make note of those differences
		* Example: Running a WDL on an HPC via Cromwell (e.g. via the Dockstore CLI) requires additional runtime arguments that a local user does not need to include in their WDL program, tell HPC users what additional things they need
* When talking about Linux, mention that your instructions are specific to Ubuntu, and from that point on in the document assume users are either using Ubuntu or know how to translate into their own distribution
	* Exception: If directing users to install software via apt-get, provide alternatives for Red Hat (yum), Arch (pacman), and Gentoo (emerge) if those alternatives are available
* Make a note about these Mac-specific situations in the text if they occur:
	* If there is an important functional difference between the Linux and the Mac version, such as xargs
	* If there is an important installation difference between the Linux and the Mac version, such as the installation of the Dockstore CLI
	* If something does not work/works differently on Apple Silicon Macs
* If the bash and zsh version of something would be different, provided both versions
	* Unless this bash/zsh difference only applies to Linux, make note of the fact that zsh is the default shell in Mac OS as of Catalina (10.15)
	* Do not worry about other shells besides bash and zsh

## Coding in RST
* Write in RST, not markdown
* Use `.. comment` to write comments
* Use consistent indentation spacing within a single RST file
* Keep all sentences in a given paragraph that renders as body text on one line, i.e. do not break up body text every x characters
* Make RST tables human-readable instead of compact -- consider using [this table generator](https://tableconvert.com/restructuredtext-generator)
* Use \`this style \<https://example.com\>_` of formatting external hyperlinks, as it is less error prone than the method involving setting the target in another paragraph
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
 
## International/Translation
See also: [Google's guidelines r/e translation](https://developers.google.com/style/translation) 

* Avoid using idioms ("it's raining cats and dogs in Santa Cruz")
* Avoid using culturally-specific comparisons ("the button is green like a dollar bill")
* Try to use relatively simple English whenever possible
* Make sure programs/templates you are providing to the user have a way to handle non-ASCII names and names with apostrophes and hyphens

## Inclusion
See also: [Google's guidelines for inclusive documentation](https://developers.google.com/style/inclusive-documentation), but be aware that some terms are still being discussed without a clear consensus at this time. The examples below demonstrate our understanding of currently recognized best practices, and may need to be adjusted over time.

* Use gender-neutral language wherever possible (firefighter vs fireman)
* Use gender-neutral pronouns when referring to a hypothetical person ("they" instead of "he or she"), even if that requires changing a verb conjugation ("they **adjust** their settings" vs "he or she **adjusts** his or her settings")
* Avoid unnecessarily using socially-charged terms for technical concepts
	* For example, avoid terms such as blacklist, whitelist, sanity check, and first-class citizen. Instead, consider denylist, allowlist, overall check, first-class object, etc
* Avoid calling tasks "simple" or "easy" as it may frustrate users who are finding it to not be all that easy
	* It is acceptable to use comparisons, e.g. to say that something is easier than something else

## Logos
* Before using a new logo for an external organization or moving an existing logo to a place where it has a next context, make a good-faith effort to reach out to the organization for approval if usage of that logo is not clear from their policy
* Do not use NHLBI logos, including the BioData Catalyst logo, except where it has been explicitly approved
* Review the logo policy for specific organizations on the Social Media and Outreach Policy document (ask for Google Drive access if necessary)

## Technical detail
* Generally speaking, assume that your audience is computer literate but may not know their way around the command line, git, Docker, or workflow languages
	* This will vary - a user seeking out best practices for a specific workflow language will know what a workflow language is
* Keep track of technical phrases and acronyms, and add them to the glossary if they are not already defined in the glossary
	* What is considered a "technical phrase" can be nebulous; use your best judgment
	* Define language-specific acronyms (CWL, WDL, etc) the first time they are used in a document
	* Define CLI when introducing the concept to new users, but you do not need to define it in all docs about the Dockstore CLI
* Glossary terms should define the functional meaning of acronyms for your audience, not just what they stand for
	* Example: If your audience are pet owners, "Light Amplification by the Stimulated Emission of Radiation" is much less helpful than "a device that emits light based on stimulation of electromagnetic radiation, which can be used to create a small red dot that cats find fascinating"
* Focus more on the how-to-do-things than what's happening under the hood

## Timeliness
* Follow [Google's timeless documentation guidelines](https://developers.google.com/style/timeless-documentation)
* In places where it is truly necessary to anchor something to a point in time, consider adding an RST comment reading `.. !time` nearby so that later maintainers of the documentation will be able to search all such instances and update them as necessary.

## Tone
Adapted from [Google's style guide r/e tone](https://developers.google.com/style/tone)

* Humor in the form of slightly silly examples is okay, but generally keep things formal
	* "My Cool Workflow", etc is okay
* Never include any humor at the expense of a person, organization, or group of people
* You can make the case for a feature's existence, but avoid sounding too much like a salesperson
* Use [second-person](https://developers.google.com/style/person) whenever it makes sense to do so
* When telling someone to perform a task in a tutorial or otherwise using imperatives, make the second-person subject [implicit](https://editorsmanual.com/articles/sentence-implied-subject-grammar/)
	* Example: "Click this button to delete System32" instead of "You can click this button to delete System32"
* Use [active voice](https://developers.google.com/style/voice)
