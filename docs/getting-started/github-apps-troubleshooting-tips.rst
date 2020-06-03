.. Need to update with info about checking lambda errors in UI

- If you don't see changes, try waiting a couple of minutes and refreshing the page again.
- Verify the GitHub app was given access to the right repository. If access was given to the wrong repo, you'll need to make another push after correcting it. Check by:

    - Navigating to the ``+ Manage Dockstore Installation on GitHub`` button mentioned above
    - Go to your repo on GitHub, click the Settings tab, click Integrations on the left and verify our app is installed and configured correctly

- Double check the ``/.dockstore.yml`` file.

    - Is it in the root directory?
    - Is it on the right branch?
    - Are all indentation levels correct?
    - Does the name field match, if applicable?